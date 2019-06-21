#You are given an array of n elements. You have to divide the given array into two group such that 
#one group consists exactly k elements and second group consists rest of elements. 
#Your result must be maximum possible difference of sum of elements of these two group.
Input : arr[n] = {1, 5, 2, 6, 3}  , k = 2
# Output : Maximum Difference = 11
# Explanation : group1 = 1+2 , group2 = 3+5+6
#               Maximum Difference = 14 - 3 = 11

# Input : arr[n] = {1, -1, 3, -2, -3} , k = 2
# Output : Maximum Difference = 10
# Explanation : group1 = -1-2-3 , group2 = 1+3
#               Maximum Difference = 4 - (-6) = 10

##1 liner print(max(abs(sum(a)-2*sum(sorted(a)[:k])) , abs(sum(a)-2*sum(sorted(a)[-k:]))))


a = [1,2,4,-5,6,7,11,-1]
k = 3
a.sort()
arraySum = sum(a)
smallestNumberSum = sum(a[:k])
diff1 =  abs(arraySum-2*smallestNumberSum)
largestNumberSum = sum(a[-k:])
diff2 = abs(arraySum-2*largestNumberSum)
print(max(diff1 ,diff2))
