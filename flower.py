#flower.py

class Solution:
	def canPlaceFlowers(self, flowerbed, n):
		if n == 0 or len(flowerbed)==0:
			return True 		
		if len(flowerbed)== 1:
			if(flowerbed[0]==0 and n==1):
				return True
			else:
				return False
		
		for i in range(len(flowerbed)):
			if(flowerbed[i]==0):
				if(i==0):
					if(flowerbed[i+1]==0):
						flowerbed[i] = 1
						n -= 1
				elif(i==len(flowerbed)-1):
					if(flowerbed[i-1]==0):
						flowerbed[i] = 1
						n -= 1
				elif(flowerbed[i-1]==0 and flowerbed[i+1]==0):
					flowerbed[i] = 1
					n -= 1
			if(n==0):
				return True
		if(n>0):
			return False
				
			
sol = Solution()
flowerbed=[0,1]

n=0
print(len(flowerbed))
result= sol.canPlaceFlowers(flowerbed,n)
print(result)