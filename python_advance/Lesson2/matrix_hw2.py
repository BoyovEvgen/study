"""
3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для объектов
класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly вывода
матрицы на экран.
"""


class My_two_level_matrix:

    def __new__(cls, matrix_data):
        matrix_data = cls.check_update_digit(matrix_data)
        obj = super().__new__(cls)
        obj.matrix = matrix_data
        return obj

    # def __init__(self, matrix_data: list):
    #     self.matrix = matrix_data

    @staticmethod
    def __check_full_len(matrix_data):
        return len(matrix_data) == 3 and len(matrix_data[0]) ==3 and len(matrix_data[1]) == 3 and len(matrix_data[2]) == 3

    @staticmethod
    def check_update_digit(matrix_data):
        if My_two_level_matrix.__check_full_len(matrix_data):
            return list(map(lambda a: [int(n) for n in a], matrix_data))
        else:
            raise ValueError

    def __repr__(self):
        str_mx = ''
        for row in self.matrix:
            str_mx += f'{row}\n'
        return str_mx

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, *args):
        if len(args) > 1:
            return self.matrix[args[0]][args[1]]
        else:
            return self.matrix[args[0]]

    def __add__(self, other_matrix):
        if len(other_matrix) == len(self):
            total_res = []
            for x in range(len(self)):
                str_res = []
                for y in range(len(self[x])):
                    str_res.append(self[x][y] + other_matrix[x][y])
                total_res.append(str_res)
            return My_two_level_matrix(total_res)
        else:
            raise TypeError('it is not possible to perform an operation with matrices of different sizes')

    def __sub__(self, other_matrix):
        # if len(other_matrix) == len(self):
        total_res = []
        for x in range(len(self)):
            str_res = []
            for y in range(len(self[x])):
                str_res.append(self[x][y] - other_matrix[x][y])
            total_res.append(str_res)
        return My_two_level_matrix(total_res)
        # else:
        #     raise TypeError('it is not possible to perform an operation with matrices of different sizes')

    def __mul__(self, num):
        total_res = []
        for x in range(len(self)):
            str_res = []
            for y in range(len(self[x])):
                str_res.append(self[x][y] * num)
            total_res.append(str_res)
        return My_two_level_matrix(total_res)

    def __truediv__(self, num):
        total_res = []
        for x in range(len(self)):
            str_res = []
            for y in range(len(self[x])):
                str_res.append(round(self[x][y] / num, 2))
            total_res.append(str_res)
        return My_two_level_matrix(total_res)

    def __eq__(self, other):
        return self.matrix == other.matrix


if __name__ == "__main__":
    data1 = [['1', 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    mx1 = My_two_level_matrix(data1)
    mx2 = My_two_level_matrix(data2)
    print(type(mx1))
    print(mx1)
    print(mx2)
    mx3 = mx1 + mx2
    print(mx3)
    mx4 = mx2 - mx1
    print(mx4)
    print(mx4 * 2)
    print(mx1 / 3)
    print(mx1 == mx2)
