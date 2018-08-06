#anagram.py 
import collections
class Solution:
	def isAnagram(self, s, t):
		#print(s)\
		return len(collections.Counter(s) - collections.Counter(t)) == 0
		if len(s) == len(t):
			a=[i for i in s]
			for i in t:
				if i in a:
					a.remove(i)
			if len(a)==0:
				return True
				
		else:
			return False
		
		return False
		
		
sol = Solution()
s = "rt!4"
t = "r!3t"
result =sol.isAnagram(s,t) 
print(result)

print("s - ",len(collections.Counter(s)))
print("t - ", len(collections.Counter(t)))

print( (collections.Counter(s) - collections.Counter(t)))
	