#backtester.py
#Charles J. Lai
#August 26, 2013

class Backtester(object):
	#Fields (Hidden)
	_field = 0		# Field Comment

	#Properties (Get and set fields)
	@property
	def field(self):
		return self._field

	@field.setter
	def field(self, value):
		#assert value >= 1, "Use assert statement to enforce preconditions"
		self._field = value

	#Immutable Properties

	#Built-in Functions
	def __init__(self, field):
		self.field = field

	def method(self, value):
		pass