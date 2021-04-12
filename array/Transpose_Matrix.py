class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        trans = [[0]*rows for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                trans[j][i] = matrix[i][j]
        return trans
