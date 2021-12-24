from handler.time.timer import TimerHandler
import schedule

class EventTimeClient():

	handler = None

	def __init__(self):
		timer_handler = TimerHandler()
		self.handler = timer_handler

	def handle(self, event_time, method, *args):
		return self.handler.handle(event_time, method, *args)

	@staticmethod
	def cancel_all():
		return
		schedule.clear('all')