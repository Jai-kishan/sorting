class Calculation1:
	def addition(self,a,b):
		return a+b;

class Calculation2(Calculation1):
	def subtraction(self,a,b):
		return a-b;

class Calculation3(Calculation2):
	def multiplication(self,a,b):
		return a*b;

class Calculation4(Calculation3):
	def division(self,a,b):
		return a/b;

obj = Calculation4()
print(issubclass(Calculation3,Calculation2))