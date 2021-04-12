class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count = 0
        
        if len(candyType)/2 == len(set(candyType)):
            return len(candyType)//2
        else:
            if len(candyType)/2 > len(set(candyType)):
                return len(set(candyType))
            return len(candyType)//2
