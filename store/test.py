from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

#Builder.load_file("testadv.kv")


Builder.load_string('''
<MainWidget>:
	orientation: 'vertical'
	Label:
		text: "KivyMob"

	Button:
		text: "Click"
		on_release: root.clicked()

<FirstWidget>:
	canvas.before:
		BorderImage:
			border: 10, 10, 10, 10
			texture: self.background_image.texture
			pos: self.pos
			size: self.size
	orientaion: 'vertical'
	FloatLayout:
		Label:
			text: "30"
			text_size: self.width-20, self.height-20
			valign: 'top'
		Button:
			text:"x"
			size_hint: .05, .05
			#texture_size: 10, 10
			text_size: self.texture_size
			valign: 'top'	

	#AsyncImage:
	#	source: 'adverts/pic-001.jpg'

''')


class FirstWidget(FloatLayout):
	background_image = ObjectProperty(Image(source='adverts/pic-001.jpg'))




class MainWidget(BoxLayout):

	def clicked(self):
		print("clicked")
		self.clear_widgets()
		cur_widget = Factory.FirstWidget()
		self.add_widget(cur_widget)
	pass

class TestApp(App):
	def build(self):
		return MainWidget()


TestApp().run()
