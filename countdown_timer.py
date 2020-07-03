from datetime import timedelta

class CountdownTimer:
	def __init__(self):
		self.currentTime = 0
		self.steppedBeyondZero = False
		self.outputStringFormat = "{0}"

	def countdown_from(self, currentTime):
		self.currentTime = currentTime
		if currentTime < 0:
			self.steppedBeyondZero = True
			self.outputStringFormat = "-{0}"
		else:
			self.steppedBeyondZero = False
			self.outputStringFormat = "{0}"

	def step(self, amount=1):
		self.currentTime -= amount
		if self.currentTime < 0:
			self.steppedBeyondZero = True
			self.outputStringFormat = "-{0}"
		else:
			self.steppedBeyondZero = False
			self.outputStringFormat = "{0}"
	
	#returns string value of how much time passed H:M:S
	def get_time_stepped(self):
		return self.outputStringFormat.format(str(timedelta(seconds=abs(self.currentTime))))