# polymorphism with the class mthods.

class India:
	def capital(self):
		print("New Delhi is the Capital of Indai. ")

	def language(self):
		print("Hindi the primary language of India. ")

	def type(self):
		print("India is a devloping Country. ")

class USA:

	def capital(self):
		print("Washington D.C. is the capital of USA. ")

	def language(self):
		print("English is the primary language of the USA. ")

	def type(self):
		print("USA is the devloped Country. ")

# obj_ind = India()
# obj_usa = USA()

# for country in (obj_usa,obj_ind):
# 	print(country.capital())
# 	print(country.language())
# 	print(country.type())

def func(obj):
	obj.Capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)


# a=("3,4,5")
# print(len(a))

# print(len([1,2,3]))


# class Bird:
# 	def intro(self):
# 		print('There are many types of birds. ')

# 	def flight(self):
# 		print("Most of the Birds can fly but some cannot. ")

# class Sparrow(Bird):
# 	def flight(self):
# 		print("sparrow can fly. ")

# class Ostrich(Bird):
# 	def flight(self):
# 		print("Ostrich cannot fly. ")


# obj_bird = Bird()
# obj_spr= Sparrow()
# obj_ost= Ostrich()

# print(obj_bird.intro())
# print(obj_bird.flight())

# print(obj_spr.intro())
# print(obj_spr.flight())

# print(obj_ost.intro())
# print(obj_ost.flight())

# or

