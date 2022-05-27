from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window

ratio = 3

Window.size = 1440 // ratio, 2911 // ratio

mw, mh = map_size = 480, 480

Builder.load_string('''
#:import utils kivy.utils

<RootWidget>:
	canvas:
		Color:
			rgba: utils.get_color_from_hex('#6B6863')
			#rgba: 0, 0, 1, 1
		Rectangle:
			pos: 0, 0
			size: root.ww, root.wh/15

		Color:
			rgba: utils.get_color_from_hex('#73B5D3')
		Rectangle:
			pos: 0, root.wh // 15
			size: root.ww, root.mh
			#source: 'worldmap_480_480.png'
			source: 'worldmap-resized-1.png'

		Color:
			rgba: utils.get_color_from_hex('#73B5D3')
		Rectangle:
			pos: 0, (root.wh // 15 + root.mh)
			size: root.ww, root.wh - root.wh // 15 - root.mh

	FloatLayout:
		Label:
			text: 'Hello'
			pos:  


''')

class SubWidget(Widget):
	ww, wh = Window.size
	mw, mh = 480, 480
	pass

class RootWidget(Screen):
	ww, wh = Window.size
	mw, mh = 480, 480
	pass

class TestApp(App):
	ww, wh = Window.size
	def build(self):
		return RootWidget()

if __name__ == '__main__':
	TestApp().run()
