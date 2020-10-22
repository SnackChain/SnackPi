from handler.time.handler import AbstractEventTimeHandler
import schedule
import time

class Timer():
	def __init__(self, time_interval):
		self.time_interval = time_interval

class TimerHandler(AbstractEventTimeHandler):

	def handle(self, event_time, method, *args):
		if event_time.type == 'timer':
			timer = Timer(**event_time.parameters)
			schedule.every(timer.time_interval).seconds.do(method, *args).tag('all', 'timer')
		else:
			super().handle(snack_device_id, snack, parameter_provider)