import numpy as np
import random

array1 = np.array([[1, 2, 3], [4, 5, 6]])

array2 = np.array([[0.0, 0.1, 0.2, 0.3, 0.4]])
"""
for row in array1:
    print(row)
        for col in row:
        print(col, end=" ")
    print()

for i in array1.flat:
    print(i)
"""
array3 = np.zeros(5)

array4 = np.ones((2, 4), dtype=int)

array5 = np.full((3, 5), 13)

array6 = np.array(
    [
        [random.randint(1, 10) for i in range(5)],
        [random.randint(1, 10) for i in range(5)],
    ]
)

array7 = np.array(np.random.randint(1, 10, size=(2, 5)))

array8 = np.arange(5)

array9 = np.arange(5, 10)

array10 = np.arange(10, 1, -2)

print()
