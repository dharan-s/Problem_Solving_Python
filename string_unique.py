# Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

class Solution:
	def string_unique(self, input_string):
		for i,val in enumerate(input_string.lower()):
			if val in input_string[i+1:]:
				return False
		return True	
####################

s = Solution()
print(s.string_unique("s12f 6yu"))  ###Test your string here.