from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
#from kivy.properties import PropertyObject

#class WarLabel(Label):
#    color = [0, 0, 0, 1]
#    font_size = 20
#    font_name = "font/DroidSansFallback.ttf"
#    #color: 0, 0, 0, 1
#    text_size = [200, 100]
#    halign = 'left'
#    valign ='middle'  
    
class WarPage(Screen):
   #enemy_info = PropertyObject(None)
    #enemy_info_box = PropertyObject(None)
    enemy = {
        "id": "000000", 
        "name": "Enemy", 
        "resources": 0, 
        "guard": 0, 
        "lancer": 0, 
        "shieldman": 0,
        "archer": 0, 
        "cavalryman": 0
    }
    
    def set_enemy(self,  enemy):
        self.enemy = enemy

    def update_enemy(self):
        #layout = self.ids._enemy_info
        #for w in layout.children:
            #layout.remove_widget(w)
        
        #box = BoxLayout(orientation='vertical')
        
        # get enemy info
        #user = self.ids._get_enemyid.text
        #print(user)
        
        self.ids._enemy_id.text ="id: %s" % self.enemy["id"]
        self.ids._enemy_name.text = u"name: %s" % self.enemy["name"]
        self.ids._enemy_resources.text = "resources: %s" % str(format(self.enemy["resources"],  ","))
        self.ids._enemy_guard.text = "guard: %s" % str(format(self.enemy["guard"],  ","))
        self.ids._enemy_lancer.text = "lancer: %s" % str(format(self.enemy["lancer"],  ","))
        self.ids._enemy_shieldman.text = "shieldman: %s" % str(format(self.enemy["shieldman"],  ","))
        self.ids._enemy_archer.text = "archer: %s" % str(format(self.enemy["archer"],  ","))
        self.ids._enemy_cavalryman.text = "cavalryman: %s" % str(format(self.enemy["cavalryman"],  ","))
 
        #layout.add_widget(box)

#class WarLabel(Label):
#    pass

#class EnemeyInfo(BoxLayout):
#    pass

