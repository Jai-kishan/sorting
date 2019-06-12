def Reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]


def Main(inp):
	rev = Reverse(inp)
	for char in rev:
		print(char)

	print(list(inp[i] for i in range(len(inp)-1,-1,-1)))

if __name__=='__main__':
	print("This program for Reverse String")
	inp = input("Enter the name : ")
	Main(inp)