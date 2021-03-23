class Solution:
    def xorOperation(self, n: int, start: int):
        x = 0
        for i in range(n):
            x = x^(start + 2*i)
        return x
        
