class Adition:
	first =0
	second =0
	answer =0 
	def add(self,f,s):
		self.first = f
		self.second = s

	def display(self):
		print("first Number : ",self.first)
		print("second Number : ",self.second)
		print("Aditon of two Number : ",self.answer)

	def calculation(self):
		self.answer = self.first+self.second


obj = Adition()
obj.add(5,6)
obj.calculation()
obj.display()