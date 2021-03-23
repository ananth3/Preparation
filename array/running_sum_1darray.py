#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i])
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [None]*len(nums)
        res[0] = nums[0]
        for i in range(1,len(nums)):
            res[i] = nums[i]+res[i-1]
        return res
