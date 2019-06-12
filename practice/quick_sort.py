def partition(arr,l,h):
	i = (l-1)
	x =(arr[h])
	for j in range(l,h):
		i = i+1
		arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[h] = arr[h],arr[i+1]
	return(i+1)

def quick_sort(arr,l,h):
	size = h-l+1
	stack = [0] * (size)
	top = -1

	top = top+1
	stack[top]=l
	top = top+1
	stack[top]=h
