class Person:
	#init method or constructor
	def __init__(self,name,age):
		self.name = name
		self.age= age

	#simple Method
	def Sayhi(self):
		print("Hii I am ",self.name,self.age)

#creating a object 'P'
P =Person("Jai kishan",34)
P.Sayhi() #object Method