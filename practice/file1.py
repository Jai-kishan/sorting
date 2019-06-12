
print("File1 __name__%s"%__name__)

if __name__=='__main__':
	print(True, "File1 is being run directly")
else:
	print(False,"File1 is being imported")