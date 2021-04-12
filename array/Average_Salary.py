class Solution:
    def average(self, salary: List[int]) -> float:
        avg = 0.00000
        sort_num = sorted(salary)
        sort_num = sort_num[1:-1]
        avg = sum(sort_num)/len(sort_num)
        return avg
