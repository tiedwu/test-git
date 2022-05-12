from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
import json
from os.path import exists
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty

class NewsPage(Screen):
	data_items = []
	file = "camp_history.json"
	#rv_layout = ObjectProperty(None)

	def update(self):
		#print("update()", self)
		if exists(self.file):
			with open(self.file, "r") as f:
				hist_dict = json.load(f)
				hist_data = [{'index': x, 'content': hist_dict[x]} for x in hist_dict.keys()]
				#print(hist_data)
				self.data_items = hist_data[::-1]
		self.ids._rv_news.data = self.data_items
		self.ids._rv_news.refresh_from_data()

class StatefulLabel(RecycleDataViewBehavior, BoxLayout):
	index = 0
	camp_datetime = StringProperty()
	enemy_id = StringProperty()
	enemy_nickname = StringProperty()
	enemy_guard = StringProperty()
	enemy_resources = StringProperty()
	enemy_lancer = StringProperty()
	enemy_shieldman = StringProperty()
	enemy_archer = StringProperty()
	enemy_cavalryman = StringProperty()
	resources_robbed = StringProperty()
	lancer_damaged = StringProperty()
	shieldman_damaged = StringProperty()
	archer_damaged = StringProperty()
	cavalryman_damaged = StringProperty()
	def refresh_view_attrs(self, rv, index, data):
		#print("refresh()", data)
		self.index = index
		content = data["content"]
		self.camp_datetime = "时间: %s" % content["camp_datetime"]
		self.enemy_id = "ID: %s" % content["enemy_id"]
		self.enemy_nickname = "昵称: %s" % content["enemy_nickname"]
		self.enemy_guard = "城卫: %s" % str(format(content["enemy_guard"], ","))
		self.enemy_resources = "资源: %s" % str(format(content["enemy_resources"], ","))
		self.enemy_lancer = "枪兵: %s" % str(format(content["enemy_lancer"], ","))
		self.enemy_shieldman = "盾兵: %s" % str(format(content["enemy_shieldman"], ","))
		self.enemy_archer = "弓兵: %s" % str(format(content["enemy_archer"], ","))
		self.enemy_cavalryman = "骑兵: %s" % str(format(content["enemy_cavalryman"], ","))
		self.resources_robbed = "掠夺资源: %s" % str(format(content["resources_robbed"], ","))
		self.lancer_damaged = "枪兵损失: %s" % str(format(content["lancer_damaged"], ","))
		self.shieldman_damaged = "盾兵损失: %s" % str(format(content["shieldman_damaged"], ","))
		self.archer_damaged = "弓兵损失: %s" % str(format(content["archer_damaged"], ","))
		self.cavalryman_damaged = "骑兵损失: %s" % str(format(content["cavalryman_damaged"], ","))

		super(StatefulLabel, self).refresh_view_attrs(rv, index, data)

