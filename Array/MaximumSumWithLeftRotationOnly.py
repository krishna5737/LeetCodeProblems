#Problem Statement:
#Find maximu#m value of Sum( i*arr[i]) with only left rotations on given array allowed
# R0 =     0*a[0] + 1*a[1]     + 2*a[2] + 3*a[3] + .......................... + (n-2)*a[n-2] + (n-1)*a[n-1]
# R1 = (n-1)*a[0] + 0*a[1]     + 1*a[2] + 2*a[3] + .......................... + (n-3)*a[n-2] + (n-2)*a[n-1]
# R2 = (n-2)*a[0] + (n-1)*a[1] + 0*a[2] + 1*a[3] + .......................... + (n-4)*a[n-2] + (n-3)*a[n-1]

# R1-R0 = (n-1)a[0] - a[1] - a[2] + ....................................... - a[n-2] - a[n-1]
# R1-R0 = -sum + n * a[0]

# R2-R0 = - sum + n * a[1]

#General Formula: Rj - Rj-1 = sum_of_array - len(arr) * a[j-1]

arr = [int(x) for x in input()]
sum_array = sum(arr)
result = 0

sumOfProductOfIndexAndValue = sum(i*arr[i] for i in range(len(arr)))

for i in range(1,len(arr)):
	sumOfProductOfIndexAndValue = sumOfProductOfIndexAndValue - sum_array + len(arr)* arr[i-1]
	if(sumOfProductOfIndexAndValue > result ):
		result = sumOfProductOfIndexAndValue
print(result)
