from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
#from kivy.factory import Factory

#Builder.load_file("testadv.kv")

Builder.load_string('''
#:import Factory kivy.factory.Factory
<MainWidget>:
	orientation: 'vertical'
	Label:
		text: "KivyMob"

	Button:
		text: "Click"
		on_release: Factory.FirstWidget().open()

<FirstWidget@Popup>:
	#size_hint: .8, .8
	title: ""
	separator_height: 0
	#size: 400, 200
	FloatLayout
		#canvas.before:
		#	BorderImage:
		#		border: 10, 10, 10, 10
				#texture: root.background_image.texture
		#		source: 'adverts/pic-001.jpg'
		#		pos: self.pos
		#		size: self.size
		#orientation: 'vertical'
		#FloatLayout:
		AsyncImage:
			source: 'adverts/pic-001.jpg'
			pos_hint: {'center_x': .5, 'center_y': .5} 
		Label:
			text: "30"
			#text_size: self.width-20, self.height-20
			text_size: self.size
			valign: 'top'
			pos_hint: {'x': 0, 'top': 1}
		Button:
			text:"x"
			size_hint: .05, .05
			#texture_size: 10, 10
			text_size: self.texture_size
			valign: 'top'
			on_release: root.dismiss()

	#AsyncImage:
	#	source: 'adverts/pic-001.jpg'

''')


class FirstWidget():
	#background_image = ObjectProperty(Image(source='adverts/pic-001.jpg'))
	pass




class MainWidget(BoxLayout):

	def clicked(self):
		print("clicked")
		#self.clear_widgets()
		#cur_widget = Factory.FirstWidget()
		#self.add_widget(cur_widget)
		
	pass

class TestApp(App):
	def build(self):
		return MainWidget()


TestApp().run()
