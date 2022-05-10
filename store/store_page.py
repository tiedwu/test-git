from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock
import glob
import random

class StorePage(Screen):
	double_gathering_time = 0
	double_payload_time = 0
	benefits_remain = 0
	crystal_counter = 50
	crystal_countdown = 60
	crystal_remain_countdown = 0

	def update(self):
		self.ids._double_gathering_remain.text = \
			str(format(self.double_gathering_time, ","))

		self.ids._double_payload_remain.text = \
			str(format(self.double_payload_time, ","))

		self.ids._crystal_countdown.text = \
			str(self.crystal_countdown)

		self.ids._crystal_counter.text = \
			str(self.crystal_counter) 

class AdvWidget(Popup):

	adv_countdown = 30
	#clock = Clock()

	def countdown(self):
		Clock.schedule_interval(self.update, 1)
		files = glob.glob('adverts/*.jpg')
		#print(files) 
		file = random.choice(files)
		#print(file)
		self.ids._image_path.source = file

	def update(self, dt):
		if self.adv_countdown > 0:
			self.adv_countdown -= 1
		self.ids._adv_countdown.text = str(self.adv_countdown)

	def confirm_dismiss(self):
		if self.adv_countdown > 0:
			return
		self.dismiss()
