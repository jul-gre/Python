class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix1 = [[3, 5, 32],
                [2, 4, 6],
                [-1, 64, -8]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matrix1[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix1]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix1]))

my_matrix = Matrix([[31, 22, 37],
                    [43, 51, 66],
                    [-10, -100, 9]],
                   [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]])
print(my_matrix.__add__())