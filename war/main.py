
__version__ = '0.6'

from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from os.path import exists
import json

from kivy.uix.label import Label

#import war_page

#from kivy.utils import utils

Builder.load_file("layout.kv")
Builder.load_file("manage_page.kv")
Builder.load_file("building_page.kv")
Builder.load_file("military_page.kv")
Builder.load_file("war_page.kv")
Builder.load_file("store_page.kv")
Builder.load_file("news_page.kv")

class WarMainLabel(Label):
    color = [0, 0, 0, 1]
    font_size = 20
    font_name = "font/DroidSansFallback.ttf"
    #color: 0, 0, 0, 1
    text_size = [200, 100]
    halign = 'left'
    valign ='middle'  

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
		self.ids["_multipage"].ids["_warpage"].ids["_target_assign"].bind(on_release=self.show_enemy)
		self.ids._multipage.ids._warpage.ids._campaign.bind(on_release=self.campaign)

		# bind storepage buttons
		self.ids["_multipage"].ids["_storepage"].ids["_get_crystal_15"].bind(on_release=self.get_crystal_15)

	def campaign(self, instance):
		# me
		#me = self.data["soldiers"]
		# enemy
		#enemy = self.ids._multipage.ids._warpage.enemy
		
		#print(me, enemy)
		result = self.ids._multipage.ids._warpage.campaign(self.data["soldiers"])
		print(result)

	def show_enemy(self, instance):
        	# get enemy id
		enemy_id = self.ids._multipage.ids._warpage.ids._get_enemyid.text
		if enemy_id == "":
			return
		print(enemy_id)
		if enemy_id not in self.enemy_data.keys():
			return

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
		self.ids["_multipage"].ids["_warpage"].update_enemy()

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

		print("update data in jason")
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
                "mines": 0, "crystal": 0}
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
        with open(self.data_path, "w") as f:
            json.dump(self.data, f)
        print("saved!")

    def on_quit(self, *args):
        self.save_data()    
    
if __name__ == '__main__':
    GameApp().run()
