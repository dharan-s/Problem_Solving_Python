def factors(n):    
	for i in range(2, int(pow(n, 0.5) + 1)):
		if(n % i == 0):
			if(n == inp.count(inp[:i]) * i):
				print(inp[:i])
				return True
			elif(n == inp.count(inp[:n//i]) * n//i):
				print(inp[:n//i])
				return True
				
inp = str(input("Enter input : "))
if(factors(len(inp)) != True):
	print("None")
