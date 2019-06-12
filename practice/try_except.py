
try:
	f = open("class.py")
	# ram =jai
except FileNotFoundError as e:
	print(e)
except NameError as e:
	print(e)
else:
	print(f.read())
	f.close()