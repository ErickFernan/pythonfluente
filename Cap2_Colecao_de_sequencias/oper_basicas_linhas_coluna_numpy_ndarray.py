import numpy

a = numpy.arange(12)

print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(type(a))
# <class 'numpy.ndarray'>

print(a.shape) # Inspeciona as dimensões do array
# (12,)

a.shape = 3, 4

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]


print(a[2])
# [ 8  9 10 11]

print(a[2, 1])
# 9

print(a[:, 1])
# [1 5 9]

print(a.transpose())
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]
