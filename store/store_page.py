from kivy.uix.screenmanager import Screen

class StorePage(Screen):
	double_gathering_time = 0
	double_payload_time = 0
	benefits_remain = 0

	def update(self):
		self.ids._double_gathering_remain.text = \
			str(format(self.double_gathering_time, ","))

		self.ids._double_payload_remain.text = \
			str(format(self.double_payload_time, ","))
