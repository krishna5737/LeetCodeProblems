#Generate all rotations of a number

#Logic
#423-->234
#423*10 = 4230
#4230+4 = 4234
#4234-4000 = 234

number = int(input())
original_number = number
next_permutation = 0
while(next_permutation!=original_number):
  print(number)
	next_permutation = number * 10 + int(str(number)[0]) - pow(10,len(str(number)))*int(str(number)[0])
	number = next_permutation
	
