class Solution:
    def maxPower(self, s: str) -> int:
        l = len(s)
        p = 0
        count = 1
        for i in range(1, l):
            if s[i]==s[i-1]:
                count+=1
            else:
                p = max(p, count)
                count = 1
        return max(p, count)
        
