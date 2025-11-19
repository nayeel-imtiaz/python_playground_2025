import numpy as np

# # 1) Core object: ndarray (WHAT DOES THIS MEAN?)
# a = np.array([1, 2, 3]) # 1-D
# b = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D
#
# print(f"a.dtype: {a.dtype}, a.shape: {a.shape}")
# print(f"b.dtype: {b.dtype}, b.shape: {b.shape}")
#
# # Create quickly:
# c = np.zeros((2,3))
# d = np.ones((4,1))
# e = np.full((3,3), 7)
# f = np.arange(0, 10, 2)        # 0,2,4,6,8
# g = np.linspace(0, 1, 5)       # 0.,0.25,0.5,0.75,1.
# h = np.random.randn(4, 3)      # N(0,1) samples

### Code below doesn't work as intended
# for char in [chr(ord('a') + index) for index in range(8)]:
#     print(
#         f"""
#         {{char}}: {char}
#         """
#           )

# print()
# print(f"h: {h}")
#
# # Reshape / add axes:
# x = np.arange(6)  # [0, 1, 2, 3, 4, 5], shape: (6, )
# x2 = x.reshape(2, 3)  # [ [0, 1, 2], [3, 4, 5] ], shape: (2, 3)
# y = x[:, np.newaxis]  # np.newaxis = None
# # y = [[0], [1], [2], [3], [4], [5]], shape: (6, 1)
# z = x[np.newaxis, :]
# # z = [[0, 1, 2, 3, 4, 5]], shape: (1, 6)
#
# print(f"x.shape: {x.shape}, x2.shape: {x2.shape}, y.shape: {y.shape}, z.shape: {z.shape}")
#
# print()
# print(f"y: {y}, y.shape: {y.shape}")
# print()
# print(f"z: {z}, z.shape: {z.shape}")


'''
X = [
    [4, 4, 4, 4],
    [10, 20, 30, 40],
    [5, 9, -15, 50]
]


'''
# # X = np.random.randn(3, 4)         # shape (3,4)
# X = np.array([[4, 4, 4, 4], [10, 20, 30, 40], [5, 9, -15, 50]])
# col_mean = X.mean(axis=0)         # shape (4,)
# '''
# col_mean = [6.33, 11, 6.33, 31.33], shape (4, )
# '''
# row_mean = X.mean(axis=1)
# '''
# row_mean = [4, 25, 49/4 = 12.25], shape (3, )
# '''
#
# print(f"col_mean: {col_mean}, col_mean.shape: {col_mean.shape}")
# print(f"row_mean: {row_mean}, row_mean.shape: {row_mean.shape}")

# col_mean = col_mean[None, :]      # reshape to (1,4)
# X_centered = X - col_mean         # now broadcast works

j = np.arange(8)


j1 = j.reshape(4, 2)
j2 = j.reshape(2, 4).T
j3 = j.reshape(2, 2, 2)

j4 = j[:, np.newaxis, np.newaxis]
j5 = j[np.newaxis, :, np.newaxis]

print(f"j: {j}")
print()

print(f"j1: {j1}")
print()

print(f"j2: {j2}")
print()

print(f"j3: {j3}")
print()

print(f"j4: {j4}")
print()

print(f"j5: {j5}")
print()

'''
j: [0, 1, 2, 3, 4, 5, 6, 7]

j1: [ 
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7]
]

j2: [
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

j3: 
[
    [
        [0, 1],
        [2, 3]
    ],
    [
        [4, 5],
        [6, 7]
    ]
]

j4:
[
    [
        [0]
    ],
    [
        [1]
    ],
    [
        [2]
    ],
    [
        [3]
    ],
    [
        [4]
    ],
    [
        [5]
    ],
    [
        [6]
    ],
    [
        [7]
    ]
]

j5:
[
    [[0], [1], [2], [3], [4], [5], [6], [7]]
]
'''

