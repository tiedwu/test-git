from kivy.uix.screenmanager import Screen

class BuildingPage(Screen):
    castle = 0
    house = 0
    guard = 0
    camp = 0
    castle_cost = 0
    house_cost = 0
    guard_cost = 0
    camp_cost = 0
    
    def calc_cost(self, k, lv):
        if k == 'castle':
            return (lv+1) * 10
        elif k == 'house':
            return (lv+1) * 10
        elif k == 'guard':
            return (lv+1) * 10
        elif k == 'camp':
            return (lv+1) * 10
    
    def update(self):
        self.ids["_castle"].text = str(format(self.castle, ","))
        self.ids["_house"].text = str(format(self.house, ","))
        self.ids["_guard"].text = str(format(self.guard, ","))
        self.ids["_camp"].text = str(format(self.camp, ","))
        self.castle_cost = self.calc_cost('castle', self.castle)
        self.ids["_castle_cost"].text = ' ' * 5 + str(format(self.castle_cost, ","))
        self.house_cost = self.calc_cost('house', self.house)
        self.ids["_house_cost"].text = ' ' * 5 + str(format(self.house_cost, ","))
        self.guard_cost = self.calc_cost('guard', self.guard)
        self.ids["_guard_cost"].text = ' ' * 5 + str(format(self.guard_cost, ","))
        self.camp_cost = self.calc_cost('camp', self.camp)
        self.ids["_camp_cost"].text = ' ' * 5 + str(format(self.camp_cost, ","))
        
        
