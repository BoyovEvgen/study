# import os
# import sys
#
# sys.path.insert(1, os.path.join(sys.path[0], '../Lesson2/matrix_hw2'))
# from matrix_hw2 import My_two_level_matrix

import pytest
import Lesson2.matrix_hw2 as matrix_f


data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data2 = [['1', 1, 1], [1, 1, 1], [1, 1, 1]]
matrix = matrix_f.My_two_level_matrix(data1)
matrix1 = matrix_f.My_two_level_matrix(data2)


def test_my_matrix():
    assert isinstance(matrix, matrix_f.My_two_level_matrix)


def test_add_my_matrix():
    matrix2 = matrix1 + matrix
    assert matrix2.matrix == [[2, 3, 4], [5, 6, 7], [8, 9, 10]]


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        matrix/0


def test_check_update_digit():
    res = matrix_f.My_two_level_matrix.check_update_digit([['1', 2, '3'], [4, '5', 6], [7, 8, '9']])
    assert res == data1


def test1_check_update_digit():
    with pytest.raises(ValueError):
        matrix_f.My_two_level_matrix([['f', 2, 'l'], [4, '5', 6], [7, 8, '9']])


def test2_check_update_digit():
    with pytest.raises(ValueError):
        matrix_f.My_two_level_matrix([[1, 2, 3], [4, 6], [7, 8, '9']])



