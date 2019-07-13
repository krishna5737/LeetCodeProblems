
# Read the Postfix expression from left to right
# If the symbol is an operand, then push it onto the Stack
# If the symbol is an operator, then pop two operands from the Stack
# Create a string by concatenating the two operands and the operator before them.
# string = "("+ operand2 + operator + operand1 + ")"
# And push the resultant string back to Stack
# Repeat the above steps until end of Prefix expression.


def PostFixToInfix(str):
    stack = []
    for i in str:
        if(i.isalpha()):
            stack.append(i)
        else:
            firstcharacter = stack.pop()
            secondcharacter = stack.pop()
            stack.append("("+secondcharacter+i+firstcharacter+")")
    return(stack[0])
print(PostFixToInfix("ab*c+"))
