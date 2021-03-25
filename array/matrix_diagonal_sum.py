class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    sum+=mat[i][j]
                elif i+j==len(mat)-1 and i!=j:
                    sum+=mat[i][j]
        return sum
