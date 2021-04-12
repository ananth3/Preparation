class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            key = target - nums[i]
            
            if key in dic:
                return [dic[key],i]
                
            dic[nums[i]] = i
             
