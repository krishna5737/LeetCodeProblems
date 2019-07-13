#Ref: https://www.youtube.com/watch?v=1Q94XEp1yfk&t=7s
def StockSpan(a):
    resultantarray = [1]
    stack = [0]
    for i in range(1,len(a)):
        print(stack,a[i])
        while(stack and a[i]>=a[stack[-1]]):
            stack.pop()
        if(not stack):
            resultantarray.append(i+1)
        else:
            resultantarray.append(i-stack[-1])
        stack.append(i)
    return resultantarray
print(StockSpan([10, 4, 5, 90, 120, 80]))
