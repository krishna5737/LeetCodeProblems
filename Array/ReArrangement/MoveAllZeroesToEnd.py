#Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
#I/P: {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, 
#O/P: {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
#Expected time complexity is O(n) and extra space is O(1).

arr = [1,2,3,4,5,0,6,7,0]
n = len(arr)
count = 0

for i in range(n):
	if(arr[i] is not 0):
		arr[count] = arr[i]
		count += 1

while(count<n):
	arr[count] = 0
	count += 1

print(arr)
