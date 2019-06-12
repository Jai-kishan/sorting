# Class and Instance Variables (Or attributes)
'''
class CSStudent():

	# class variable 
	stream ='CS'

	# init method or constructor
	def __init__(self,roll):

		#instance variable
		self.roll = roll

# objects of class CSStudent
a =CSStudent(101)
b = CSStudent(102)

print(a.roll)
print(a.stream)
# or
print(CSStudent.stream)


'''

#class name
class CSStudent:

	# class Variable
	sub = "Science"

	# init method or constructor
	def __init__(self,name):
		#instance varibale
		self.name = name

	# adds instance varibale
	def setAddress(self,address):
		self.address= address

	def getAddress(self):
		return self.address

user = input('Enter your name : ')

#drive codes 
a= CSStudent(user)
print(a.name)
address = input('Enter your Address : ')
a.setAddress(address)
print(a.getAddress())