###arr_digit.py

digits=[9,9,2,9]

length = len(digits)



if(digits[length-1] != 9):
	digits[length-1] += 1
else:
	while(digits[length-1] == 9 and (length-1) != 0):
			
		digits[length-1] = 0
		length -=1
		
	else:
		if digits[length-1] == 9:
			digits[length-1] = 0
			digits.insert(0,1)
		else:
			digits[length-1] += 1

print(digits)