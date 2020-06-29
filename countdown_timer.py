from datetime import timedelta

class CountdownTimer:
	def __init__(self):
		self.currentTime = 0
		self.steppedBeyondZero = False
		self.outputStringFormat = "{0}"


	def startAt(self, currentTime):
		self.currentTime = currentTime

	def step(self, amount=1):
		self.currentTime -= amount
		if self.currentTime < 0 and self.steppedBeyondZero == False:
			self.steppedBeyondZero = True
			self.outputStringFormat = "-{0}"
		else:
			self.steppedBeyondZero = False
			self.outputStringFormat = "{0}"
	
	def getTimeStepped(self):
		return self.outputStringFormat.format(str(timedelta(seconds=abs(self.currentTime))))