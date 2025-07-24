import numpy as np

# a = np.array([0, 1, 2, 3, 4])
# print(a)
#
# print('a[0]: ', a[0])
# print(type(a))
# print(a.dtype)

# b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
# # type of array
# print(type(b))
# # value type of array
# print(b.dtype)

# c = np.array([20, 1, 2, 3, 4])
# print(c)
# # We can change the first element of the array to 100 as follows:
# c[0] = 100
# # We can change the 5th element of the array to 0 as follows:
# c[4] = 0
# print(c)
# #
# # # Slicing
# # d = c[1:4]
# # print(d)
#
# # arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# # # Print the even elements in the given array.
# # print(arr[1:8:2])
#
# select = [0, 2, 3, 4]
#
# d = c[select]
# print(d)
# c[select] = 1000
# print(c)

# a = np.array([0, 1, 2, 3, 4])
# print(a)
#
# print(a.size)
# print(a.ndim)
# print(a.shape)
# mean = a.mean()
# print(mean)

u = np.array([1, 0])
y = np.array([0, 1])
z = np.add(u, y)
print(z)

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
sum = np.add(arr1, arr2)
print(sum)
subtraction = np.subtract(arr2, arr1)
print(subtraction)

arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
dot = np.dot(arr1, arr2)
print(dot)

print(np.linspace(0,100, 12))