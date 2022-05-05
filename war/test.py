from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

kv = Builder.load_string("""


""")

Builder.load_string('''

<MyLabel@Label>
    color: 1, 1, 1, 1

<RootWidget>:
	max_v: 10000
    PopWidget:
		orientation: 'vertical'
        id: popw
		Label:
			color: 1, 1, 1, 1
			text : str(int(slider_1.value))
		Slider:
			id: slider_1
			min: 0
			max: root.max_v
			step: 1
			value: 0
    Button:
        text: "Pop"
        on_release: root.abc()
    
    


''')

class PopWidget(BoxLayout):
    pass

#class MyLabel(Label):
#    pass


def testfunc():
    a = 3
    b = 5
    c = 6

class RootWidget(BoxLayout):
    def abc(self):
        layout = self.ids["popw"]
        layout.add_widget(MyLabel(text="pop!"))

class TestApp(App):
    def build(self):
        root = RootWidget()
        return root
    
TestApp().run()

