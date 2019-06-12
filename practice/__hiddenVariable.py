class Myclass:
	__hiddenvariable= 0
	def add(self,increment):
		self.__hiddenvariable+=increment
		print(self.__hiddenvariable)

obj= Myclass()
obj.add(2)
obj.add(5)

print(obj._Myclass____hiddenvariable)