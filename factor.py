from functools import reduce

#-------Finding factor for a number-------#
#----Retrun tyoe: set-------------#
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
		

inp = str(input("Enter input : "))
factor = factors(len(inp))
#---Removing the prime number----####
factor.remove(1)
factor.remove(len(inp))

if(len(factor) != 0):
	while(factor): 
		s = factor.pop()  #---pops out s
		sub_str = inp[:s]
		if(len(inp) == inp.count(sub_str) * len(sub_str)):
			print(sub_str)
			break
		elif(len(factor) != 0):  #---check for n/s value 
			if(len(inp) == inp.count(inp[:len(inp)//s]) * len(inp)//s):
				print(inp[:len(inp)//s])
				break
			factor.remove(len(inp)/s) 	
	else:
		print("None")
else:
	print("None")
		