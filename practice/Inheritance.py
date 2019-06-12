#Inheritance

class Pet:

	def __init__(self,name,age):
		self.name =name
		self.age=age

class Cat(Pet):

	def __init__(self,name,age):
		super().__init__(name,age)

def Main():
	thePet = Pet('Pet',3)
	jess = Cat('jess',3)
	print("Is jess a cat? " +str(isinstance(jess, Cat))) 
	print("Is jess a pet? " +str(isinstance(jess, Pet))) 
	print("Is the pet a cat? "+str(isinstance(thePet, Cat))) 
	print("Is thePet a Pet? " +str(isinstance(thePet, Pet))) 
	print(jess.name) 




if __name__=='__main__':
	Main()