#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.
#Note: A word is defined as a character sequence consists of non-space characters only.

#Example:
#Input: "Hello World"
#Output: 5

s = "Heloo World    "

x = s.split(" ")
print("Split : ", x)
x = list(filter(None, x))
print("filter : ", x)
if len(x) == 0:
	print("0")
else:
	print(len(x[len(x)-1]))
