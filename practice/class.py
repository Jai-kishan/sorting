class Jai:

	x=0.0
	y=0.0

	def set(self,x,y):
		self.x = x
		self.y =y


def Main():
	vec = Jai()

	vec.set(5,6)
	print("x: "+str(vec.x)+" y: "+str(vec.y) )


if __name__=='__main__':
	Main()
