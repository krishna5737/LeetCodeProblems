#Algo
# 1. Scan the infix expression from left to right.
# 2. If the scanned character is an operand, output it.
# 3. Else,
# …..3.1 If the precedence of the scanned operator is greater than the precedence of the operator 
#....    in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it.
# …..3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence 
#....    than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
# 4. If the scanned character is an ‘(‘, push it to the stack.
# 5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
# 6. Repeat steps 2-6 until infix expression is scanned.
# 7. Print the output
# 8. Pop and output from the stack until it is not empty.

def isPrecedence(a,b):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    try:
        if(precedence[a]<=precedence[b]):
            return True
        else:
            return False
    except:
        return False

def InfixToPostFix(str):
    stack = []
    outputPostfixString = ''
    for i in str:
        if(i.isalpha()==True):
            outputPostfixString+= i
        elif(i =='('):
            stack.append(i)
        elif(i==')'):
            while(stack and stack[-1]!='('):
                a = stack.pop()
                outputPostfixString+= a
            if(stack and stack[-1]!='('):
                return -1
            else:
                stack.pop()
        else:
            # print(i,stack,outputPostfixString)
            while(stack and isPrecedence(i,stack[-1])):
                outputPostfixString+= stack.pop()
            stack.append(i)
    print(outputPostfixString)

InfixToPostFix("a+b*(c^d-e)^(f+g*h)-i")
			
