#Given an array, print the Next Greater Element (NGE) for every element. 
#The Next greater Element for an element x is the first greater element on the right side of x in array. 
#Elements for which no greater element exist, consider next greater element as -1.

# Examples:
# For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.
# Element       NGE
#   4      -->   5
#   5      -->   25
#   2      -->   25
#   25     -->   -1

#Solution
arr = [11,5,2,4,21,3]

stack = []
stack.append(arr[0])

for i in range(1,len(arr),1):
	next = arr[i]
	if(stack):
		element = stack.pop()
		while(element<next):
			print(str(element)  + ' --- ' +str(next))
			if(not stack):
				break
			element = stack.pop()
		if(element>next):
			stack.append(element)
			
		if(element>next):
		  stack.push(next)
	stack.append(next)
while(stack):
	element = stack.pop()
	print(str(element)  + ' --- ' + str(-1))
