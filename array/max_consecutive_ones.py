class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        n=0
        for i in nums:
            if i==1:
                c+=1
            else:
                n = c
                c = 0
        if n>c:
            return n
        return c
