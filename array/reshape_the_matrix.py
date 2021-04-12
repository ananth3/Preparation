class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        matrix = []
        
        for num in nums:
            for n in num:
                flat.append(n)
        
        if len(flat) != r*c:
            return nums
        
        return [flat[i*c:(i+1)*c] for i in range(r)]
