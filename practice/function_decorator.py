
def messageWithWelcome(str):

	def addWelcome():
		return ("Welcome to ")

	return addWelcome()+str

def site(site_name):
	return site_name


print(messageWithWelcome(site("NavGurukul")))



# def messageWithWelcome(fun):

# 	def addWelcome(site_name):
# 		return "Welcome to " + fun(site_name)

# 	return addWelcome

# @messageWithWelcome
# def site(site_name):
# 	return site_name


# print(site("NavGurukul"))

