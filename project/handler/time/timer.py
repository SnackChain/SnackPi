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
			method(*args)
			#schedule.every(timer.time_interval).seconds.do(method, *args).tag('all', 'timer')
			schedule.every(timer.time_interval).seconds.do(method, *args)
		else:
			super().handle(event_time, method, *args)