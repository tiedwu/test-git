
__version__ = '0.6'

from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from os.path import exists
import json
import random

Builder.load_file("layout.kv")
Builder.load_file("manage_page.kv")
Builder.load_file("building_page.kv")
Builder.load_file("military_page.kv")
Builder.load_file("war_page.kv")
Builder.load_file("store_page.kv")
Builder.load_file("news_page.kv") 

class MainInfo(BoxLayout):
    nickname = 'Admin'
    userid = '999999'
    crystal = 99999
    resources = 0
    resources_increase = 0
    residents = 0
    residents_increase = 0

    def update(self):
        self.ids["_nickname"].text = u'%s' % self.nickname
        self.ids["_userid"].text = self.userid
        self.ids["_crystal"].text = str(format(self.crystal, ","))
        self.ids["_resources"].text = str(format(self.resources, ","))
        self.ids["_resources_increase"].text = '%s/s' % str(format(self.resources_increase, ","))
        self.ids["_residents"].text = str(format(self.residents, ","))
        self.ids["_residents_increase"].text = '%s/m' % str(format(self.residents_increase, ","))

class MultiPage(ScreenManager):
    pass

class FuncMenu(BoxLayout):
    def switch_screen(self,  name):
        self.parent.ids["_multipage"].current = name

class RootWidget(BoxLayout):
	counter = 0
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__()
		self.userid = kwargs["userid"]
		self.data = kwargs["data"][self.userid]
		self.enemy_data = kwargs["data"]

		# remove me from enemy_data
		self.enemy_data.pop(self.userid)
		#if self.userid in self.enemy_data.keys():
		#	print("IN")
		#print(self.enemy_data)

		# init maininfo labels
		self.ids["_maininfo"].userid = self.userid
		self.ids["_maininfo"].nickname = self.data["nickname"]
		self.ids["_maininfo"].resources = self.data["resources"]
		self.ids["_maininfo"].resources_increase = self.data["resources_increase"]
		self.ids["_maininfo"].residents = self.data["residents"]
		self.ids["_maininfo"].residents_increase = self.data["residents_increase"]
		self.ids["_maininfo"].crystal = self.data["crystal"]
		self.ids["_maininfo"].update()

		# init manage labels
		soldiers = 0
		for k in self.data["soldiers"]:
			soldiers += self.data["soldiers"][k]
		self.ids["_multipage"].ids["_managepage"].labors = self.data["residents"] - soldiers
		self.ids["_multipage"].ids["_managepage"].mines = self.data["mines"]
		self.ids["_multipage"].ids["_managepage"].update()

		# bind managepage: gather button
		self.ids["_multipage"].ids["_managepage"].ids["_gather"].bind(on_release=self.gather)

		# init building labels
		self.ids["_multipage"].ids["_buildingpage"].castle = self.data["buildings"]["castle"]
		self.ids["_multipage"].ids["_buildingpage"].house = self.data["buildings"]["house"]
		self.ids["_multipage"].ids["_buildingpage"].guard = self.data["buildings"]["guard"]
		self.ids["_multipage"].ids["_buildingpage"].camp = self.data["buildings"]["camp"]
		self.ids["_multipage"].ids["_buildingpage"].update()

		# bind buildingpage: upgrade buttons
		self.ids["_multipage"].ids["_buildingpage"].ids["_castle_upgrade"].bind(on_release=self.upgrade_castle)
		self.ids["_multipage"].ids["_buildingpage"].ids["_house_upgrade"].bind(on_release=self.upgrade_house)
		self.ids["_multipage"].ids["_buildingpage"].ids["_guard_upgrade"].bind(on_release=self.upgrade_guard)
		self.ids["_multipage"].ids["_buildingpage"].ids["_camp_upgrade"].bind(on_release=self.upgrade_camp)

		# init military labels
		self.ids["_multipage"].ids["_militarypage"].lancer = self.data["soldiers"]["lancer"]
		self.ids["_multipage"].ids["_militarypage"].shieldman = self.data["soldiers"]["shieldman"]
		self.ids["_multipage"].ids["_militarypage"].archer = self.data["soldiers"]["archer"]
		self.ids["_multipage"].ids["_militarypage"].cavalryman = self.data["soldiers"]["cavalryman"]
		self.ids["_multipage"].ids["_militarypage"].update()

		# bind militarypage training buttons
		self.ids["_multipage"].ids["_militarypage"].ids["_train_lancer"].bind(on_release=self.train_lancer)
		self.ids["_multipage"].ids["_militarypage"].ids["_train_shieldman"].bind(on_release=self.train_shieldman)
		self.ids["_multipage"].ids["_militarypage"].ids["_train_archer"].bind(on_release=self.train_archer)
		self.ids["_multipage"].ids["_militarypage"].ids["_train_cavalryman"].bind(on_release=self.train_cavalryman)


		# bind warpage buttons
		self.ids["_multipage"].ids["_warpage"].ids["_target_assign"].bind(on_release=self.target_enemy)
		self.ids._multipage.ids._warpage.ids._campaign.bind(on_release=self.campaign)
		self.ids._multipage.ids._warpage.ids._rob_all.bind(on_release=self.roball)
		self.ids._multipage.ids._warpage.ids._random_search.bind(\
			on_release=self.search_enemy)

		# bind storepage buttons
		self.ids._multipage.ids._storepage.ids._rapid_gathering.bind(\
			on_release=self.rapid_gathering)
		self.ids._multipage.ids._storepage.ids._resources_increase.bind(\
			on_release=self.resources_produce)
		self.ids._multipage.ids._storepage.ids._dismiss_military.bind(\
			on_release=self.dismiss_military)
		self.ids["_multipage"].ids["_storepage"].ids["_get_crystal_15"].bind(on_release=self.get_crystal_15)

	def rapid_gathering(self, instance):
		print("rapid gathering")

	def resources_produce(self, instance):
		print("resources produce")

	def dismiss_military(self, instance):
		print("dismiss military")

		if self.ids._maininfo.crystal < 25:
			return
		self.ids._maininfo.crystal -= 25

		self.ids._multipage.ids._militarypage.lancer = 0
		self.ids._multipage.ids._militarypage.shieldman = 0
		self.ids._multipage.ids._militarypage.archer = 0
		self.ids._multipage.ids._militarypage.cavalryman = 0
		self.ids._multipage.ids._militarypage.update()

	def target_enemy(self, instance):
        # get enemy id
		enemy_id = self.ids._multipage.ids._warpage.ids._get_enemyid.text
		if enemy_id == "":
			return
		print(enemy_id)
		if enemy_id not in self.enemy_data.keys():
			return

		self.show_enemy(enemy_id=enemy_id, crystal=45)

	def search_enemy(self, instance):
		print("random search")
		enemies = [k for k in self.enemy_data.keys()]
		n = random.randint(0, len(enemies)-1)
		enemy_id = enemies[n]
		self.show_enemy(enemy_id=enemy_id, crystal=3)

		# clear textinput in war page
		self.ids._multipage.ids._warpage.ids._get_enemyid.text = ""

	def do_attack(self, mode, resources_cost, crystal):
		print(mode, resources_cost, crystal)
		if self.ids._maininfo.resources < resources_cost or resources_cost == 0:
			return

		# crystal cost
		if self.ids._maininfo.crystal < crystal:
			return
		self.ids._maininfo.crystal -= crystal

		campaign_soldiers = self.ids._multipage.ids._warpage.me_soldiers
		# soldiers consuming
		self.ids._multipage.ids._militarypage.lancer -= campaign_soldiers["lancer"]
		self.ids._multipage.ids._militarypage.shieldman -= campaign_soldiers["shieldman"]
		self.ids._multipage.ids._militarypage.archer -= campaign_soldiers["archer"]
		self.ids._multipage.ids._militarypage.cavalryman -= campaign_soldiers["cavalryman"]
		print("Before resources: ", self.ids._maininfo.resources)
		# resources consuming
		self.ids._maininfo.resources -= int(resources_cost)
		print("After resources: ", self.ids._maininfo.resources)

		result = self.ids._multipage.ids._warpage.campaign()
		print(result)
		enemy = self.ids._multipage.ids._warpage.enemy
		#print(enemy["resources"])

		resources_rob = 0
		# set resources for rob
		if mode == 'roball':
			if result["resources"] > 0:
				resources_rob = int(enemy["resources"])
		# mode == 'normal'
		else:
			if result["resources"] >= enemy["resources"]:
				resources_rob = int(enemy["resources"])
			else:
				resources_rob = int(result["resources"])

		self.ids._multipage.ids._warpage.resources_rob = resources_rob
		print("rob: ", resources_rob)
		self.ids._maininfo.resources = int(self.ids._maininfo.resources + resources_rob)
		print("After rob resources: ", self.ids._maininfo.resources)
		self.ids._maininfo.update()

		# set soldiers after campaign
		soldiers = {"lancer": self.ids._multipage.ids._militarypage.lancer,
					"shieldman": self.ids._multipage.ids._militarypage.shieldman,
					"archer": self.ids._multipage.ids._militarypage.archer,
					"cavalryman": self.ids._multipage.ids._militarypage.cavalryman}
		soldiers["lancer"] += result["soldiers"]["lancer"]
		soldiers["shieldman"] += result["soldiers"]["shieldman"]
		soldiers["archer"] += result["soldiers"]["archer"]
		soldiers["cavalryman"] += result["soldiers"]["cavalryman"]
		self.ids._multipage.ids._militarypage.set_soldiers(soldiers)
		self.ids._multipage.ids._militarypage.update()
		# set max of sliders in war page
		self.ids._multipage.ids._warpage.lancer_max =\
			self.ids._multipage.ids._militarypage.lancer
		self.ids._multipage.ids._warpage.shieldman_max =\
			self.ids._multipage.ids._militarypage.shieldman
		self.ids._multipage.ids._warpage.archer_max = \
			self.ids._multipage.ids._militarypage.archer
		self.ids._multipage.ids._warpage.cavalryman_max =\
			self.ids._multipage.ids._militarypage.cavalryman
		self.ids._multipage.ids._warpage.update()

	def roball(self, instance):
		print("rob all")
		cost = self.ids._multipage.ids._warpage.campaign_cost
		self.do_attack(mode='roball', resources_cost=int(cost), crystal=300)

	def campaign(self, instance):
		cost = self.ids._multipage.ids._warpage.campaign_cost
		print(cost)
		#print("me_soldiers: ", self.ids._multipage.ids._warpage.me_soldiers)

		self.do_attack(mode='normal', resources_cost=int(cost), crystal=2)

	def show_enemy(self, enemy_id, crystal):
		# clear the flag of show war result in warpage
		self.ids._multipage.ids._warpage.ids._resources_rob.text = ""
		self.ids._multipage.ids._warpage.ids._damaged_1.text = ""
		self.ids._multipage.ids._warpage.ids._damaged_2.text = ""

		# show campaign military
		self.ids._multipage.ids._warpage.lancer_max =\
			self.ids._multipage.ids._militarypage.lancer
		self.ids._multipage.ids._warpage.shieldman_max =\
			self.ids._multipage.ids._militarypage.shieldman
		self.ids._multipage.ids._warpage.archer_max = \
			self.ids._multipage.ids._militarypage.archer
		self.ids._multipage.ids._warpage.cavalryman_max =\
			self.ids._multipage.ids._militarypage.cavalryman

		# crystal cost
		if self.ids._maininfo.crystal < crystal:
			return
		self.ids._maininfo.crystal -= crystal

		war_enemy = self.enemy_data[enemy_id]

		enemy = {
            "id": enemy_id, 
            "name": war_enemy["nickname"], 
            "resources": war_enemy["resources"], 
            "guard": war_enemy["buildings"]["guard"], 
            "lancer": war_enemy["soldiers"]["lancer"], 
            "shieldman": war_enemy["soldiers"]["shieldman"],
            "archer": war_enemy["soldiers"]["archer"], 
            "cavalryman": war_enemy["soldiers"]["cavalryman"]
        }
		self.ids["_multipage"].ids["_warpage"].set_enemy(enemy)
		self.ids["_multipage"].ids["_warpage"].update()

	def get_crystal_15(self, instance):
		self.ids["_maininfo"].crystal += 15
		self.ids["_maininfo"].update()

	def train_lancer(self, instance):
		print("train lancer")
		unit = self.ids["_multipage"].ids["_militarypage"].unit
		if unit != 0:
			cost = self.ids["_multipage"].ids["_militarypage"].get_train_cost('lancer') * unit
			if self.ids["_maininfo"].resources >= cost:
				lancer = self.ids["_multipage"].ids["_militarypage"].lancer + unit
				if self.ids["_maininfo"].residents >=  lancer:
					self.ids["_multipage"].ids["_militarypage"].lancer = lancer
					self.ids["_maininfo"].resources -= cost
					self.ids["_multipage"].ids["_militarypage"].update()

					# sync to war page
					self.ids._multipage.ids._warpage.lancer_max = lancer
					self.ids._multipage.ids._warpage.update()
        # set unit = 0 after done
        #self.ids["_multipage"].ids["_militarypage"].unit = 0

	def train_shieldman(self, instance):
		print("train shieldman")
		unit = self.ids["_multipage"].ids["_militarypage"].unit
		if unit != 0:
			cost = self.ids["_multipage"].ids["_militarypage"].get_train_cost('shieldman') * unit
			if self.ids["_maininfo"].resources >= cost:
				shieldman = self.ids["_multipage"].ids["_militarypage"].shieldman + unit
				if self.ids["_maininfo"].residents >=  shieldman:
					self.ids["_multipage"].ids["_militarypage"].shieldman = shieldman
					self.ids["_maininfo"].resources -= cost
					self.ids["_multipage"].ids["_militarypage"].update() 
					# sync to war page
					self.ids._multipage.ids._warpage.shieldman_max = shieldman
					self.ids._multipage.ids._warpage.update()
        # set unit = 0 after done
        #self.ids["_multipage"].ids["_militarypage"].unit = 0
        #self.ids["_multipage"].ids["_militarypage"].update()

	def train_archer(self, instance):
		print("train archer")
		unit = self.ids["_multipage"].ids["_militarypage"].unit
		if unit != 0:
			cost = self.ids["_multipage"].ids["_militarypage"].get_train_cost('archer') * unit
			if self.ids["_maininfo"].resources >= cost:
				archer = self.ids["_multipage"].ids["_militarypage"].archer + unit
				if self.ids["_maininfo"].residents >=  archer:
					self.ids["_multipage"].ids["_militarypage"].archer = archer
					self.ids["_maininfo"].resources -= cost
					self.ids["_multipage"].ids["_militarypage"].update()
					# sync to war page
					self.ids._multipage.ids._warpage.archer_max = archer
					self.ids._multipage.ids._warpage.update()

	def train_cavalryman(self, instance):
		print("train cavalryman")
		unit = self.ids["_multipage"].ids["_militarypage"].unit
		if unit != 0:
			cost = self.ids["_multipage"].ids["_militarypage"].get_train_cost('cavalryman') * unit
			if self.ids["_maininfo"].resources >= cost:
				cavalryman = self.ids["_multipage"].ids["_militarypage"].cavalryman + unit
				if self.ids["_maininfo"].residents >=  cavalryman:
					self.ids["_multipage"].ids["_militarypage"].cavalryman = cavalryman
					self.ids["_maininfo"].resources -= cost
					self.ids["_multipage"].ids["_militarypage"].update()
					# sync to war page
					self.ids._multipage.ids._warpage.cavalryman_max = cavalryman
					self.ids._multipage.ids._warpage.update()

	def upgrade_castle(self, instance):
        #print("upgrade castle")
        #print(instance)
		cost = self.ids["_multipage"].ids["_buildingpage"].castle_cost
		if self.ids["_maininfo"].resources >= cost:
			self.ids["_maininfo"]. resources -= cost
			self.ids["_multipage"].ids["_buildingpage"].castle += 1
			lv = self.ids["_multipage"].ids["_buildingpage"].castle
			cost_upgrade = self.ids["_multipage"].ids["_buildingpage"].calc_cost('castle', lv) 
			self.ids["_multipage"].ids["_buildingpage"].castle_cost = cost_upgrade
			self.ids["_multipage"].ids["_buildingpage"].update()

            # set residents increase per minute
			self.ids["_maininfo"].residents_increase += 1
			self.ids["_maininfo"].update()

	def upgrade_house(self, instance):
		cost = self.ids["_multipage"].ids["_buildingpage"].house_cost
		if self.ids["_maininfo"].resources >= cost:
			self.ids["_maininfo"]. resources -= cost
			self.ids["_multipage"].ids["_buildingpage"].house += 1
			lv = self.ids["_multipage"].ids["_buildingpage"].house
			cost_upgrade = self.ids["_multipage"].ids["_buildingpage"].calc_cost('house', lv) 
			self.ids["_multipage"].ids["_buildingpage"].house_cost = cost_upgrade
			self.ids["_multipage"].ids["_buildingpage"].update()
        #print("upgrade castle")

	def upgrade_guard(self, instance):
		cost = self.ids["_multipage"].ids["_buildingpage"].guard_cost
		if self.ids["_maininfo"].resources >= cost:
			self.ids["_maininfo"]. resources -= cost
			self.ids["_multipage"].ids["_buildingpage"].guard += 1
			lv = self.ids["_multipage"].ids["_buildingpage"].guard
			cost_upgrade = self.ids["_multipage"].ids["_buildingpage"].calc_cost('guard', lv) 
			self.ids["_multipage"].ids["_buildingpage"].guard_cost = cost_upgrade
			self.ids["_multipage"].ids["_buildingpage"].update()
		#print("upgrade castle")

	def upgrade_camp(self, instance):
		cost = self.ids["_multipage"].ids["_buildingpage"].camp_cost
		if self.ids["_maininfo"].resources >= cost:
			self.ids["_maininfo"]. resources -= cost
			self.ids["_multipage"].ids["_buildingpage"].camp += 1
			lv = self.ids["_multipage"].ids["_buildingpage"].camp
			cost_upgrade = self.ids["_multipage"].ids["_buildingpage"].calc_cost('camp', lv) 
			self.ids["_multipage"].ids["_buildingpage"].camp_cost = cost_upgrade
			self.ids["_multipage"].ids["_buildingpage"].update()
        #print("upgrade castle")

	def update(self):
        # mines auto increase
		self.counter += 1
		if (self.counter % 10) == 0:
			castle_lv = self.ids["_multipage"].ids["_buildingpage"].castle
			increase = 50 if castle_lv == 0 else castle_lv * 100
			self.ids["_multipage"].ids["_managepage"].mines += increase

			# residents increase
			house_lv = self.ids["_multipage"].ids["_buildingpage"].house
			residents_limit = house_lv * 5
			self.ids["_maininfo"].residents += castle_lv * 1
			if self.ids["_maininfo"].residents > residents_limit:
				self.ids["_maininfo"].residents = residents_limit

		# resources auto increase
		soldiers = self.ids["_multipage"].ids["_militarypage"].lancer + \
			self.ids["_multipage"].ids["_militarypage"].shieldman + \
			self.ids["_multipage"].ids["_militarypage"].archer + \
			self.ids["_multipage"].ids["_militarypage"].cavalryman

		labors = self.ids["_maininfo"].residents - soldiers
		self.ids["_multipage"].ids["_managepage"].labors = labors
		self.ids["_maininfo"].resources_increase = labors
		self.ids["_maininfo"].resources += self.ids["_multipage"].ids["_managepage"].labors

		# update labels
		self.ids["_maininfo"].update()
		self.ids["_multipage"].ids["_managepage"].update()
		self.ids["_multipage"].ids["_buildingpage"].update()

		#print("update data in jason")
		self.data["buildings"]["castle"] = self.ids["_multipage"].ids["_buildingpage"].castle
		self.data["buildings"]["house"] = self.ids["_multipage"].ids["_buildingpage"].house
		self.data["buildings"]["guard"] = self.ids["_multipage"].ids["_buildingpage"].guard
		self.data["buildings"]["camp"] = self.ids["_multipage"].ids["_buildingpage"].camp

		self.data["resources"] = self.ids["_maininfo"].resources
		self.data["resources_increase"] = self.ids["_maininfo"].resources_increase
		self.data["residents"] = self.ids["_maininfo"].residents
		self.data["residents_increase"] = self.ids["_maininfo"].residents_increase
		self.data["crystal"] = self.ids["_maininfo"].crystal

		self.data["mines"] = self.ids["_multipage"].ids["_managepage"].mines

        # save soldier data in json
		self.data["soldiers"]["lancer"] = self.ids["_multipage"].ids["_militarypage"].lancer
		self.data["soldiers"]["shieldman"] = self.ids["_multipage"].ids["_militarypage"].shieldman
		self.data["soldiers"]["archer"] = self.ids["_multipage"].ids["_militarypage"].archer
		self.data["soldiers"]["cavalryman"] = self.ids["_multipage"].ids["_militarypage"].cavalryman

		self.data["double_gathering_time"] = 0
		self.data["double_payload_time"] = 0

	def gather(self, instance):
		castle_lv = self.ids["_multipage"].ids["_buildingpage"].castle
		increase = 3 if castle_lv == 0 else castle_lv * 5
		if self.ids["_multipage"].ids["_managepage"].mines >= increase:
			self.ids["_maininfo"].resources += increase
			self.ids["_multipage"].ids["_managepage"].mines -= increase
        #self.update()

class GameApp(App):
    
    userid = "999999"
    data_path = "./user_data.json"
    data = {}

    def build(self):
        Window.bind(on_request_close=self.on_quit)
        self.check_user(self.userid)
        root = RootWidget(userid=self.userid, data=self.data)
        Clock.schedule_interval(self._update, 1.0)
        return root

    def _update(self, dt):
        self.root.update()
        self.save_data()

    def create_user(self):
        user_data = {\
                "nickname": "Admin",\
                "buildings": {"castle": 0, "house": 0, "guard": 0, "camp": 0}, \
                "resources": 0, "resources_increase": 0, \
                "residents": 0, "residents_increase": 0, \
                "soldiers": {"lancer": 0, "shieldman": 0, "archer": 0, "cavalryman": 0}, \
                "mines": 0, "crystal": 0, "double_gathering_time": 0, \
				"double_payload_time": 0}
        self.data[self.userid] = user_data

    def check_user(self, userid="999999"):
        if not exists(self.data_path):
            self.create_user()
        else:
            with open(self.data_path, "r") as f:
                self.data = json.load(f)
            if not userid in self.data.keys():
                self.create_user()

    def save_data(self):
        """
        data = {"admin": {"resources": 0}}
        """
        self.data[self.userid] = self.root.data
        
        # save chinese in json with indent=4
        with open(self.data_path, "w", encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
        #print("saved!")

    def on_quit(self, *args):
        self.save_data()    
    
if __name__ == '__main__':
    GameApp().run()
