from kivy.uix.screenmanager import Screen

class MilitaryPage(Screen):
    lancer = 0
    shieldman = 0
    archer = 0
    cavalryman = 0
    unit = 0
    
    buttons = {'_unit_one': 1, '_unit_ten': 10, '_unit_hundred': 100, '_unit_thousand': 1000, '_unit_ten_thousand': 10000}
    
    def update(self):
        self.ids["_lancer"].text = str(format(self.lancer, ","))
        self.ids["_shieldman"].text = str(format(self.shieldman, ","))
        self.ids["_archer"].text = str(format(self.archer, ","))
        self.ids["_cavalryman"].text = str(format(self.cavalryman, ","))
        
        # clear the status if unit buttons
        #for k in self.buttons:
            #self.ids[k].color = [0, 0, 0, 1]
        
    
    def get_train_cost(self, kind):
        cost = {'lancer': 100, 'shieldman': 150, 'archer': 200, 'cavalryman': 350}
        return cost[kind]
        
    def get_campaign_cost(self, kind):
        cost = {'lancer': 300, 'shieldman': 350, 'archer': 450, 'cavalryman': 400}
        return cost[kind]
    
    def set_unit(self, unit):
        
        # text color read while pressed
        self.unit = self.buttons[unit]
        for k in self.buttons:
            self.ids[k].color = [1, 0, 0, 1] if k == unit else [0, 0, 0, 1]
        
        
        
        
        
