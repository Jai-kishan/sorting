def merge(left,right):
	import ipdb ; ipdb.set_trace()  #### ipdb
	result = []
	i,j = 0, 0
	while i<len(left) and j< len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

	result += left[i:]
	result += right[j:]
	return result


def mergesort(lst): # pass the argument of lis [5,3,4,2]
	if(len(lst) <= 1): # []
		return lst
	mid = int(len(lst)/2)
	import ipdb ; ipdb.set_trace() # ipdb
	left = mergesort(lst[:mid])
	right = mergesort(lst[mid:])
	return merge(left,right)


arr = [5,3,4,2]
print(mergesort(arr))
