def binary_search(lis_item,search_item,first,last):
	if(first <= last):
		mid = (first+last)//2
		if lis_item[mid] == search_item:
			return mid
		elif lis_item[mid] < search_item:
			return binary_search(lis_item,search_item,mid+1,last)
		else:
			return binary_search(lis_item,search_item,first,mid-1)
	return -1
sorted_list = [12,14,15,20,25,28,30,32]
find = 32
first=0
last=len(sorted_list)-1
index = binary_search(sorted_list,find,first,last)
print(index)