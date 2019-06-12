	
# Rearrange array such that even positioned are greater than odd
# Given an array A of n elements, sort the array according to the following relations :
#  A[i] >= A[i-1]  , if i is even.
#  A[i] <= A[i-1]  , if i is odd.
# Print the resultant array.

# Input : A[] = {1, 2, 2, 1}
# Output :  1 2 1 2

# Input : A[] = {1, 3, 2}
# Output : 1 3 2

a = [5,6,7,8,9,11,12,13,10]
a.sort()
n = len(a)
b = [0]*n
q = n-1
p = 0
for i in range(n):
	if(i+1) %2 ==0:
		b[i] = a[q]
		q -= 1
	else:
		b[i] = a[p]
		p += 1
print(b)
