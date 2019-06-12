# Calculator

class Calculation1:
	def sum(self,a,b):
		return a+b

class Calculation2(Calculation1):
	def mul(self,a,b):
		return a*b

# class Calculation3(Calculation1,Calculation2):
# 	def divide(self,a,b):
# 		return a/b

d=Calculation2()
print(d.sum(5,10))
print(d.mul(5,10))
# print(d.divide(10,5))
