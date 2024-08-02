## Timer class from the BUG mod by EmperorFool

from CvPythonExtensions import *
import CvEventInterface
import time
from RFCUtils import utils

gc = CyGlobalContext()

## Timing Code Execution

class Timer:
	"""
	Stopwatch for timing code execution and logging the results.
	
	timer = BugUtil.Timer('function')
	... code to time ...
	timer.log()
	
	In a loop, log() will display each iteration's time. Since Timers are started
	when created, call reset() before entering the loop or pass in False.
	Use logTotal() at the end if you want to see the sum of all iterations.
	
	timer = BugUtil.Timer('draw loop', False)
	for/while ...
		timer.start()
		... code to time ...
		timer.log()
	timer.logTotal()
	
	A single Timer can be reused for timing loops without creating a new Timer
	for each iteration by calling restart().
	"""
	def __init__(self, item, start=True):
		"""Starts the timer."""
		self._item = item
		self.reset()
		if start:
			self.start()
	
	def reset(self):
		"""Resets all times to zero and stops the timer."""
		self._initial = None
		self._start = None
		self._time = 0
		self._total = 0
		return self
	
	def start(self):
		"""Starts the timer or starts it again if it is already running."""
		self._start = time.clock()
		if self._initial is None:
			self._initial = self._start
		return self
	
	def restart(self):
		"""Resets all times to zero and starts the timer."""
		return self.reset().start()
	
	def stop(self):
		"""
		Stops the timer if it is running and returns the elapsed time since start,
		otherwise returns 0.
		"""
		if self.running():
			self._final = time.clock()
			self._time = self._final - self._start
			self._total += self._time
			self._start = None
			return self._time
		return 0
	
	def running(self):
		"""Returns True if the timer is running."""
		return self._start is not None
	
	def time(self):
		"""Returns the most recent timing or 0 if none has completed."""
		return self._time
	
	def total(self):
		"""Returns the sum of all the individual timings."""
		return self._total
	
	def span(self):
		"""Returns the span of time from the first start() to the last stop()."""
		if self._initial is None:
			warn("called span() on a Timer that has not been started")
			return 0
		elif self._final is None:
			return time.clock() - self._initial
		else:
			return self._final - self._initial
	
	def log(self, extra=None):
		"""
		Stops the timer and logs the time of the current timing.
		
		This is the same as calling logTotal() or logSpan() for the first time.
		"""
		self.stop()
		return self._log(self.time(), extra)
	
	def logTotal(self, extra="total"):
		"""
		Stops the timer and logs the sum of all timing steps.
		
		This is the same as calling log() or logSpan() for the first time.
		"""
		self.stop()
		return self._log(self.total(), extra)
	
	def logSpan(self, extra=None):
		"""
		Stops the timer and logs the span of time covering all timings.
		
		This is the same as calling log() or logTotal() for the first time.
		"""
		self.stop()
		return self._log(self.span(), extra)
	
	def _log(self, runtime, extra):
		"""Logs the passed in runtime value."""
		if extra is None:
			utils.echo("Timer - %s took %d ms" % (self._item, 1000 * runtime))
		else:
			utils.echo("Timer - %s [%s] took %d ms" % (self._item, str(extra), 1000 * runtime))
		return self
