
class Test:
	def __init__(self,limit):
		self.limit = limit

	def __iter__(self):
		self.x =10
		return self

	def __next__(self): # next(self) worked in python 2 and python3 for __next__
		x = self.x

		if x > self.limit:
			raise StopIteration
		self.x =x+1
		return x

for i in Test(15):
	print(i)

