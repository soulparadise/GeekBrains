class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, el)) for el in self.my_matrix)

    def __add__(self, other):
        if len(self.my_matrix) != len(other.my_matrix):
            return 'Сложение невозможно. Матрицы не равны'
        else:
            for a, b in self.my_matrix, other.my_matrix:
                if len(a) != len(b):
                    return 'Сложение невозможно. Матрицы не равны'
                else:
                    return Matrix(
                        list(map(lambda list_1, list_2: list(map(lambda el_1, el_2: el_1 + el_2, list_1, list_2)),
                                 self.my_matrix, other.my_matrix)))


my_matrix = [[1, 2, 3, 4], [9, 10, 11, 12]]
my_matrix_2 = [[5, 6, 7, 8], [13, 14, 15, 16]]

new_matrix_1 = Matrix(my_matrix)
new_matrix_2 = Matrix(my_matrix_2)
print(new_matrix_1 + new_matrix_2)
