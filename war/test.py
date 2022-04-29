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
    PopWidget:
        id: popw
    Button:
        text: "Pop"
        on_release: root.abc()
    
    


''')

class PopWidget(BoxLayout):
    pass

#class MyLabel(Label):
#    pass

class RootWidget(BoxLayout):
    def abc(self):
        layout = self.ids["popw"]
        layout.add_widget(MyLabel(text="pop!"))

class TestApp(App):
    def build(self):
        root = RootWidget()
        return root
    
TestApp().run()