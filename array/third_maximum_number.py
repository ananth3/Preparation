class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sort_array = sorted(set(nums))
        
        if len(sort_array) < 3:
            return sort_array[-1]
        
        if len(sort_array) == 3:
            return sort_array[0]
        
        else:
            return sort_array[-3]
