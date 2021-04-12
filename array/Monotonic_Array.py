class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        sort_a = sorted(A)
        rev_sort = sorted(A, reverse=True)
        
        if A == sort_a or A == rev_sort:
            return True
        
        return False
