from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, StringProperty
import json

Builder.load_string('''
<StatefulLabel>:
	#active: stored_state.active

	CheckBox:
		id: stored_state
		active: root.active
		on_release: root.store_checkbox_state()

	Label:
		text: root.camp_datetime
	Label:
		id: generated_state
		text: root.enemy_id

<RV>
	viewclass: 'StatefulLabel'
	RecycleBoxLayout:
		size_hint_y: None
		default_size: None, dp(40)
		default_size_hint: 1, None
		height: self.minimum_height
		orientation: 'vertical'

''')

class StatefulLabel(RecycleDataViewBehavior, BoxLayout):
	text = StringProperty()
	generated_state_text = StringProperty()
	active = BooleanProperty()
	index = 0
	camp_datetime = StringProperty()
	enemy_id = StringProperty()

	def refresh_view_attrs(self, rv, index, data):
		self.index = index
		print("refresh()", index, data)
		'''
		if data['text'] == '0':
			self.generated_state_text = "is zero"
		elif int(data['text']) % 2 == 1:
			self.generated_state_text = "is odd"
		else:
			self.generated_state_text = "is even"
		'''
		content = data["content"]
		self.enemy_id = content["enemy_id"]
		self.camp_datetime = content["camp_datetime"]
		super(StatefulLabel, self).refresh_view_attrs(rv, index, data)

	def store_checkbox_state(self):
		rv = App.get_running_app().rv
		rv.data[self.index]['active'] = self.active

class RV(RecycleView, App):
	def __init__(self, **kwargs):
		super(RV, self).__init__(**kwargs)
		self.data = [{'text': str(x), 'content': {'enemy_id': '000028', 'camp_datetime': '2022-05-11 16:43:40'}} for x in range(10)]
		'''
		with open("camp_history.json", "r") as f:
			dict = json.load(f)
			self.data = [{'index': x, 'content': dict[x]} for x in dict.keys()]
		'''
		App.get_running_app().rv = self

	def build(self):
		return self

if __name__ == '__main__':
	RV().run()
