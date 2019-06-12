# O(n²). 
def bubble_sort(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp 

lis = [5,2,7,9,12,3]
bubble_sort(lis)
print(lis)