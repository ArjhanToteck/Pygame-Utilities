class AnimationController:

	def __init__(self, frameCount, frameInterval, startFrame = 0):
		self.frameCount = frameCount
		self.interval = frameInterval

		self.restart(startFrame)

	def restart(self, startFrame = 0):
		self.currentFrame = startFrame

		self.timeSinceLastFrame = 0

	def getFrame(self, timeElapsed):
		# factor in time since last getFrame call
		self.timeSinceLastFrame += timeElapsed

		# check if time to change frame
		if self.timeSinceLastFrame >= self.interval:
			print(self.timeSinceLastFrame)
			# current frame should be the floor of time elapsed / frame interval
			self.currentFrame += self.timeSinceLastFrame // self.interval

			# set timeSinceLastFrame to the remained to keep things smooth
			self.timeSinceLastFrame = self.timeSinceLastFrame % self.interval

		# cap current frame at the max
		if self.currentFrame >= self.frameCount:
			self.currentFrame = self.currentFrame - self.frameCount


		return self.currentFrame
