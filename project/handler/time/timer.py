from handler.time.handler import AbstractEventTimeHandler
import schedule
import time

class Timer():
	def __init__(self, time_interval):
		self.time_interval = time_interval

class TimerHandler(AbstractEventTimeHandler):

	job = None

	def handle(self, event_time, method, *args):
		if event_time.type == 'timer':
			timer = Timer(**event_time.parameters)
			method(*args)
			#schedule.every(timer.time_interval).seconds.do(method, *args).tag('all', 'timer')
			self.job = schedule.every(timer.time_interval).seconds.do(method, *args)
			return cancel()
		else:
			return super().handle(event_time, method, *args)

	def cancel():
		def start():
			if job != None:
				schedule.cancel_job(job)
		return start