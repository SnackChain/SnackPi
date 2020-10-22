from handler.time.handler import EventTimeHandler
from handler.time.timer import TimerHandler
import schedule

class EventTimeClient():

	handler: EventTimeHandler

	def __init__(self):
		timer_handler = TimerHandler()
		self.handler = timer_handler

	def handle(self, event_time, method, *args):
		self.handler.handle(event_time, method, *args)

	@staticmethod
	def cancel_all():
		schedule.clear('all')