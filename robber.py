#robber.py

def rob(nums):

	if len(nums) == 0: 
		return 0
	if len(nums) == 1:
		return nums[0]
	
	dp = [0 for i in range(len(nums))]
	dp[0] = nums[0]
	dp[1] = max(nums[0],nums[1])
	
	for i in range(2, len(nums)):
		dp[i] = max(dp[i-1], dp[i-2] + nums[i])
		#print(dp[i])
		
	print(len(dp))
	print(dp[6])	
	return dp[-1]

nums=[2,1,1,2,3,2,4]
value = rob(nums)
print(value)