#Problem Statement:
#Find maximu#m value of Sum( i*arr[i]) with only rotations on given array allowed
# R0 = 0*a[0] + 1*a[1] + 2*a[2] + 3*a[3] + .......................... + (n-2)*a[n-2] + (n-1)*a[n-1]
# R1 = 1*a[0] + 2*a[1] + 3*a[2] + 4*a[3] + .......................... + (n-1)*a[n-2] + 0*a[n-1]
# R2 = 2*a[0] + 3*a[1] + 4*a[2] + 5*a[3] + .......................... + (0)*a[n-2] + 1*a[n-1]

# R1-R0 = a[0] + a[1] + a[2] + ....................................... + 1*a[n-2] - (n-1) * a[n-1]
# R1-R0 = a[0] + a[1] + a[2] + ....................................... + 1*a[n-2] + 1 * a[n-1] - n * a[n-1]

# R2-R0 = sum - n * a[n-2]

#General Formula: Rj - Rj-1 = sum_of_array - len(arr) * a[n-j]

arr = [int(x) for x in input()]
sum_array = sum(arr)
result = 0

currentSumOfProductOfIndexAndValue = sum(i*arr[i] for i in range(len(arr)))
for i in range(len(arr)):
	currentSumOfProductOfIndexAndValue = currentSumOfProductOfIndexAndValue + sum_array - len(arr)* arr[(len(arr)-i-1)]
	if(currentSumOfProductOfIndexAndValue > result ):
		result = currentSumOfProductOfIndexAndValue
print(result)
