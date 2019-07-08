    
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if i == ')' :
                    if(stack and stack[-1] == '('):
                        stack.pop()
                    else:
                        return False
                elif i == '}' :
                    if(stack and stack[-1] == '{'):
                        stack.pop()
                    else:
                        return False
                elif i == ']' :
                    if(stack and stack[-1] == '['):
                        stack.pop()
                    else:
                        return False
        if(stack):
            return False
        return True
