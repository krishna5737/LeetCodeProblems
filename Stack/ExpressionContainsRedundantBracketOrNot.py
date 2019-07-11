#Given a string of balanced expression, find if it contains a redundant parenthesis or not. 
#A set of parenthesis are redundant if same sub-expression is surrounded by unnecessary or multiple brackets. 
#Print ‘Yes’ if redundant else ‘No’.
# Input: 
# ((a+b))
# (a+(b)/c)
# (a+b*(c-d))
# Output: 
# Yes
# Yes
# No

def checkRedundancy(str):
	stack = []
	for i in str:
		if(i==')'):
			top = stack.pop()
			flag = True
			while(top!='('):
				if(top == '+' or top == '-' or top == '*' or top == '/' ):
					flag = False
				top = stack.pop()
			if(flag == True):
				return True
		else:
			stack.append(i)
	
array = ["((a+b))", "(a+(b)/c)"]
for j in array:
	
	if(not(checkRedundancy(j))):
		print("No Redundancy")
	else:
		print("Redundancy")
	


		
