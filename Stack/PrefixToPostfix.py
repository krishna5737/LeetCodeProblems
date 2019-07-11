# Read the Prefix expression in reverse order (from right to left)
# If the symbol is an operand, then push it onto the Stack
# If the symbol is an operator, then pop two operands from the Stack
# Create a string by concatenating the two operands and the operator after them.
# string = operand1 + operand2 + operator
# And push the resultant string back to Stack
# Repeat the above steps until end of Prefix expression.

def PrefixToPostfix(str):
    stack = []
    for j in range(len(str)-1,-1,-1):
        i = str[j]
        if(i.isalpha()):
            stack.append(i)
        else:
            firstcharacter = stack.pop()
            secondcharacter = stack.pop()
            stack.append(firstcharacter+secondcharacter+i)
    return(stack[0])
print(PrefixToPostfix("*-A/BC-/AKL"))
