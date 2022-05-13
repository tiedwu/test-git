from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, StringProperty
import json


Builder.load_string('''
<StatefulLabel>:
	orientation: 'vertical'
	padding: 3, 3
	spacing: 5
	# Index
	# Enemy ID - row1
	# Enemy Nickname
	# Enemy Guard
	# Enemy Resources - row2
	# Enemy Lancer - row 3
	# Enemy Shieldman
	# Enemy Archer - row4
	# Enemy Cavalryman
	# Campaign Lancer - row5
	# Campaign Shieldman
	# Campaign Archer - row6
	# Campaign Cavalryman 
	# Resources Robbed - row7
	# Lancer Damaged - row 8
	# Shieldman Damaged
	# Archer Damaged - row9
	# Cavalryman Damaged
	# Datetime  - row0
	BoxLayout:
		Label:
			text: root.camp_datetime
			text_size: self.size
			#pos_hint: {'x': .2}
			valign: 'middle'
			haign: 'left'
		#Label:
		#	text: root.enemy_resources
	BoxLayout:
		Label:
			text: root.enemy_id
			text_size: self.size
			valign: 'middle'
			haign: 'left'
			#pos_hint: {'x': .2}
		Label:
			text: root.enemy_nickname
		Label:
			text: root.enemy_guard
		#Label:
			#text: root.enemy_resources
			#text_size: self.size
			#halign: 'left'
	BoxLayout:
		Label:
			text: root.enemy_lancer
			text_size: self.size
			valign: 'middle'
			halign: 'left'
		Label:
			text: root.enemy_shieldman
		Label:
			text: root.enemy_archer
		Label:
			text: root.enemy_cavalryman
	BoxLayout:
		Label:
			text: root.enemy_resources
			text_size: self.size
			valihn: 'middle'
			halign: 'left'
		Label:
			text: root.resources_robbed
		#	text: root.enemy_resourcesd
	BoxLayout:
		Label:
			text: root.lancer_damaged
			text_size: self.size
			valign: 'middle'
			halign: 'left'
		Label:
			text: root.shieldman_damaged
		Label:
			text: root.archer_damaged
		Label:
			text: root.cavalryman_damaged

<RecycleViewWidget>:
	viewclass: 'StatefulLabel'
	RecycleBoxLayout:
		#default_size: , dp(40)
		default_size_hint: 1, None
		size_hint_y: None
		height: self.minimum_height
		orientation: 'vertical'

''')

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

		#print("refresh()", index)
		#print(data)
		super(StatefulLabel, self).refresh_view_attrs(rv, index, data)

class RecycleViewWidget(RecycleView):
	data = []
	def __init__(self, **kwargs):
		super(RecycleViewWidget, self).__init__(**kwargs)
		#self.data = [{'text': str(x), 'active': False} for x in range(10)]
		with open("camp_history.json", "r") as f:
			data_dict = json.load(f)
			#print(dict)
			data_list = [{'index': x, 'content': data_dict[x]} for x in data_dict.keys()]
			#print(data_list)
			self.data = data_list
			#self.data = [{'index': x, 'content': dict[x]} for x in dict.keys()]
			#print(self.view_data)
		#print("__init__")
		App.get_running_app().rv = self
		print(self.data)

class RecycleViewApp(App):
	def build(self):
		return RecycleViewWidget()

if __name__ == '__main__':
	from kivy.core.window import Window
	Window.clearcolor = [.8, .8, .8, 1]
	RecycleViewApp().run()
