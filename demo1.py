from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

ratio = 3

Window.size = 1440 // ratio, 2911 // ratio

mw, mh = map_size = 480, 480

Builder.load_string('''
#:import utils kivy.utils


<LVLabel@Label>:
	#font_name: 'fonts/JetBrainsMono-Regular.ttf' 
	font_name: 'fonts/DroidSansFallback.ttf'
	#font_name: 'fonts/sarasa-ui-cl-regular.ttf'
<LVBox>:
	orientation: 'vertical'
	canvas.before:
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos
	LVLabel:
		font_size: 18
		color: (244/255, 252/255, 3/255, 1)
		text: ' '* 5 + 'LV ' + '196' + ' ' * 5
	BoxLayout:
		LVLabel:
			font_size: 15
			text_size: self.size
			text: u' 轮回 1 次'
			halign: 'left'
			valign: 'bottom'
			color: (3/255, 252/255, 240/255, 1)
			#color: (3/255, 198/255, 252/255, 1)
		LVLabel:
			font_size: 15
			text_size: self.size
			text: u'转生 3 次 '
			halign: 'right'
			valign: 'bottom'
			color: (3/255, 252/255, 240/255, 1)

<LVLabel@Label>:
	font_size: 20
	background_color: utils.get_color_from_hex('#33322F7F')
	canvas.before:
		#Color:
		#	rgba: 0, 1, 0, .5
		#Line:
		#	width: 2
		#	rectangle: self.x, self.y, self.width, self.height
		Color:
			rgba: utils.get_color_from_hex('#33322F7F')
		Rectangle:
			size: self.size
			pos: self.pos

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

	#FloatLayout:
	LVBox:
		x: 0
		y: 0.935 * root.wh
		size_hint: 0.45, 0.05


''')

class LVBox(BoxLayout):
	pass


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
