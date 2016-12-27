# coding=utf-8
import numpy as np
# # ----
# print "---Attribute--"
# # ----
#
# a = np.arange(12).reshape((2, 3, 2,))
#
# print a  # what's `a` like.
# print a.shape  # shape of a
# print a.ndim  # how many a dimensions is
# print a.size
# print a.dtype  # (short of data_type)type of elements in a
# print a.itemsize  # size of elements in a
# print a.data
#
# # ----
# print "---Creation---"
# # ----
#
# a = np.array([2, 3, 4])
# print a.dtype, 'a>>'
#
# a = np.array([2., 3., 4]) # The 4 is not mark as a float, it's a int.
# print a.dtype, 'a2>>'
#
# b = np.array([(1.5,2,3), (4,5,6)])
# print b, 'b>>'
#
# c = np.array([[1, 2], [3, 4]], dtype=complex)
# print c, 'c>>'
#
# print np.zeros((2, 3)), 'zeros>>'
#
# print np.ones((2, 3, 4)), 'ones>>'
#
# print np.empty((2, 3))  # This value is random, depends on the status of memory default it is float64
#
# print np.arange(10, 30, 5, np.int64)  # start, end, step, dtype
# print np.arange(12)
#
# x = np.linspace(0, 2 * np.pi, 100) # split 0-2 to (9-1) pieces, it has 9 number.
# print x
# print np.sin(x)

# print(np.arange(10000).reshape(100,100))
# np.set_printoptions(threshold='nan')
# print(np.arange(10000).reshape(100,100))
#
#
# # ----
# print '----Basic Operations----'
# # ----
#
#
# a = np.array( [20,30,40,50] )
# b = np.arange( 4 )
# print b
# c = a - b
# print c, 'a-b>>'
# print b ** 2, 'b**2>>'
# print 10 * np.sin(a), '10sin(a)>>'
# print a < 35, 'a<35 >>'
#
# A = np.array([[1,1], [0,1]])
# B = np.array([[2,0], [3,4]])
# print A * B                       # elementwise product
# print A.dot(B)                    # matrix product
# print np.dot(A, B)                # another matrix product
#
# a = np.ones((2,3), dtype=int)
# b = np.random.random((2,3))
# a *= 3
# print a
# b += a
# print b
# a += b                  # b is not automatically converted to integer type
#
# a = np.random.random((2,3))
# print a
# print a.sum()
# print a.min()
# print a.max()
#
# b = np.arange(12).reshape(3,4)
# print b
# print b.sum(axis=0)                            # sum of each column
# print b.min(axis=1)                            # min of each row
# print b.cumsum(axis=1)                         # cumulative sum along each row
#
# # ----
# print '---Universal Functions---'
# # ----
#
# '''
# NumPy provides familiar mathematical functions such as
# sin, cos, and exp. In NumPy, these are called
# “universal functions”(ufunc). Within NumPy,
# these functions operate elementwise on an array,
# producing an array as output.
#
# Including:
# all, any, apply_along_axis, argmax, argmin, argsort, average,
# bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod,
# cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum,
# mean, median, min, minimum, nonzero, outer, prod, re, round,
# sort, std, sum, trace, transpose, var, vdot, vectorize, where
# '''
#
# print np.trace(np.eye(3))
#
# a = np.arange(8).reshape((2,2,2))
# print a
# print np.trace(a)
#
# print np.arange(3) * 3
# print [1] * 3
#
# # ------
# print '----Index, Slicing and Iterating------'
# # ------
#
# a = np.arange(10) ** 3
# print a[::-1]
# b = np.fromfunction(lambda x, y: 10 * x + y, (5, 4), dtype=int)
# print b, '>> b'
# print b[2, 3], '>> b[2, 3]'
# print b[:5, 1], '>> b[:5, 1]'
# print b[:2:-1, 0], '>> b[:2:-1, 0]'
#
# c = np.fromfunction(lambda x, y, z: 100*x + 10*y + z, (3, 3, 3))
# print c, '>> c'
# print c[1, ...], 'c[1, ...]'
# print c[...], 'c[...]'
# print [x for x in c.flat], '>> c.flat'
# print c.ravel()
#
# a = np.floor(10*np.random.random((2,2)))
# b = np.floor(10*np.random.random((2,2)))
# print a
# print b
# print np.vstack((a,b)), '>> np.vstack((a,b))'
# print np.hstack((a,b)), '>> np.hstack((a,b))'
# print np.column_stack((a,b))   # With 2D arrays
#
# from numpy import newaxis
# a = np.array([4.,2.])
# b = np.array([2.,8.])
# print a, '>>a'
# print b, '>>b'
# print a[:,newaxis], '>> a[:,newaxis]'  # This allows to have a 2D columns vector
# print np.column_stack((a[:,newaxis],b[:,newaxis])), '>>np.column_stack((a[:,newaxis],b[:,newaxis]))'
# print np.vstack((a[:,newaxis],b[:,newaxis])), '>>np.vstack((a[:,newaxis],b[:,newaxis]))' # The behavior of vstack is different
# #column_stack stacks 1D array like vstack and stacks 2D array like hstack.
#
# a = np.arange(4).reshape((2, 2))
# print a[:, :, newaxis], '>> a[:, :, newaxis]'
# print a[newaxis, :, :], '>> a[newaxis, :, :]'
# print a[:, newaxis, :], '>> a[:, newaxis, :]'
#
# # For arrays of with more than two dimensions,
# # hstack stacks along their second axes, vstack
# # stacks along their first axes, and concatenate allows
# # for an optional arguments giving the number of the axis
# # along which the concatenation should happen.
#
# a = np.floor(10*np.random.random((2,12)))
# print a
# print np.hsplit(a,3)   # Split a into 3
#
# print np.hsplit(a,(3,4))   # Split a after the third and the fourth column
# a = np.arange(12)
# b = a            # no new object is created
# print b is a           # a and b are two names for the same ndarray object
#
# b.shape = 3,4    # changes the shape of a
# print a.shape
#
# c = a.view()  # c is a shallow Copy from a
# print c
# print c is a
#
# print c.base is a                        # c is a view of the data owned by a
#
# print c.flags.owndata
#
#
# c.shape = 2,6                      # a's shape doesn't change
# print c.shape
# print c
# print a.shape
#
# c[0,4] = 1234                      # a's data changes
# print a
#
# a = np.arange(12).reshape(2, 6)
# s = a[ : , 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
# s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10
# print a
# print s
#
# a = np.arange(12).reshape(2, 6)
# def f(x):
#     return x * 2
#
# f = np.vectorize(f)
# print f(a)
#
# # ------
# print '----Index tricks----'
# # ------
#
# a = np.arange(12) ** 2
# i = np.array([1, 3, 5])  # get the element in the position of i element value.
# print a[i]
# j = np.array([[1, 3], [2, 4]])
# print a[j]  # this will return a j-shape-like array.
#
# a = np.fromfunction(lambda x, y: 10 * x + y, (3, 4))
# print a
# i = np.array( [ [0,1],                        # indices for the first dim of a
#                 [1,2] ] )
# j = np.array( [ [2,1],                        # indices for the second dim
#                 [3,3] ] )
#
# print a[i,j]                                     # i and j must have equal shape
# print a[i,2]
# print a[:,j]                                     # i.e., a[ : , j]

