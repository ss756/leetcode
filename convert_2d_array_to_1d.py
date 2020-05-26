class Solution:
    def convert(self):
        A= [[1, 2, 3, 4], [5, 6, 7, 8]]
        print(A)
        new_list = list(range(len(A)*len(A[0])))
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                new_pos = i*len(A[0]) + j
                new_list[new_pos]= A[i][j]
        print(new_list)

    def __init__(self):
        self.convert()
Solution()