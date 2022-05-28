#array = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
#snail(array)  # => [1,2,3,6,9,8,7,4,5]
#    res.append([x for x in arr[0]])


def snail(arr):

    res = []
    if len(arr[0]) > 0:
        while arr:
            res += arr.pop(0)

            for i in range(len(arr)-1):
                res.append(arr[i].pop())
            try:
                last_lin = arr.pop()
                last_lin = last_lin[::-1]
                for i in last_lin:
                    res.append(i)
            except IndexError: break
            left = []
            for i in arr:
                left.append(i.pop(0))
            left = left[::-1]
            res += left
        return res
    else:
        return []

array = [[1,2,3,4,44],
         [12,13,14,5,55],
         [11,16,15,6,66],
         [10,9,8,7,77],
         [1,2,3,4,5]]
array2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(snail(array))


'''
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret'''

'''
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
'''