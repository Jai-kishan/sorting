import file1

print("File2 __name__%s"%__name__)

if __name__=='__main__':
	print(True, "File2 is being run directly")
else:
	print(False,"File2 is being imported")