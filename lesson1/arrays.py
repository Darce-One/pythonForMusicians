# Importing numpy
import numpy as np


"""
Why learn to use numpy arrays?

- Arrays give lists mathematical super-powers
- Numpy is a fundamental part of many other libraries,
    including SciPy and Librosa
- Your computer will thank you.

numpy for beginners: https://numpy.org/doc/1.26/user/absolute_beginners.html
"""

def main():
    # converting a list to an array
    to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr = np.array(to_ten)

    # element-wise math:
    arr = arr - 1
    arr = arr / 10
    print(arr)

    # numpy can also create arrays efficiently
    to_one = np.linspace(0, 1, 10, endpoint=False)
    print(to_one)
    zeros = np.zeros(10)
    print(zeros)

    # numpy has functions that do mathematical operations:
    result = np.sin(to_one) ** 2 + np.cos(to_one) ** 2
    print(result)

if __name__ =="__main__":
    main()
