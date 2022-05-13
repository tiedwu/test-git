from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder

Builder.load_string('''
<RecycleViewWidget>:
	viewclass: 'Label'
	RecycleBoxLayout:
		default_size: None, dp(56)
		default_size_hint: 1, None
		size_hint_y: None
		height: self.minimum_height
		orientation: 'vertical'


''')


class RecycleViewWidget(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.data = [{'text': str(x)} for x in range(100)]

class RecycleViewApp(App):
	def build(self):
		return RecycleViewWidget()

if __name__ == '__main__':
	from kivy.core.window import Window
	Window.clearcolor = [.8, .8, .8, 1]
	RecycleViewApp().run()

