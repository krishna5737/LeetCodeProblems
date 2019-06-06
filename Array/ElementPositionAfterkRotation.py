#Find element at given index after a number of rotations
# Input : arr[] : {1, 2, 3, 4, 5}
#         ranges[] = { {0, 2}, {0, 3} }
#         index : 1
# Output : 3
# Explanation : After first given rotation {0, 2}
#                 arr[] = {3, 1, 2, 4, 5}
#               After second rotation {0, 3} 
#                 arr[] = {4, 3, 1, 2, 5}
# After all rotations we have element 3 at given
# index 1. 

def findElement(arr, ranges, rotations, index):
	for i in range(rotations-1,-1,-1):
		start = ranges[i][0]
		end = ranges[i][1]
		if(start<=index and end>=index):
			if (index == start):
				index = end
			else:
				index -= 1
	print(arr[index])
   
arr = [int(x) for x in input()]
rotations = int(input())
ranges = [ [ 0, 2 ], [ 0, 3 ] ] 
index = int(input())
findElement(arr, ranges, rotations, index)
