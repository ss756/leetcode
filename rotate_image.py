class Solution:
    def rotate(self, matrix):
        if len(matrix) != len(matrix[0]):
            print("This operation can only be performed on square matrices")
            return
        N = len(matrix)
        for i in range(0, N):
            for j in range(i, N):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print("transposed matrix look like", matrix)
        for i in range(0, N):
            for j in range(0, N//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][N-j-1]
                matrix[i][N-j-1] = temp
        return matrix


    def __init__(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print("original matrix is ", matrix)
        result = self.rotate(matrix)
        print("Matrix after rotating 90 degrees looks like this", matrix)

Solution()
