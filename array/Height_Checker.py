class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_arr = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sort_arr[i] != heights[i]:
                count+=1
        return count
        
