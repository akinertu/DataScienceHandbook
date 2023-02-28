# NUMPY MODULE
import numpy as np
    #numpy array
    np.array([1, 4, 2, 5, 3])
    np.zeros(10, dtype=int) # Create a length-10 integer array filled with zeros
    np.zeros((3, 5), dtype=int) # Create a 3x5 floating-point array filled with zeros
    np.full((3, 5), 3.14) # Create a 3x5 array filled with 3.14
    np.arange(0, 20, 2) # Create an array filled with a linear sequence
    np.linspace(0, 1, 5) # Create an array of five values evenly spaced between 0 and 1
    np.random.random((3, 3)) # Create a 3x3 array of uniformly distributed random values between 0 and 1
    np.random.randint(0, 10, (3, 3)) # Create a 3x3 array of random integers in the interval [0, 10)
    np.random.seed(0)  # same random arrays are generated each time
    np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
    .ndim .shape .size .dtype .itemsize .nbytes #Array Attributes
    np.eye(3) # Create a 3x3 identity matrix
        #Array Indexing
        x[start:stop:step]
        x1[5::-2]  # reversed every other from index 5
        x2[:2, :3]  # two rows, three columns
        x2[:, 0] # first column of x2
        if you modify this subarray, we’ll see that the original array is changed!
    .copy() #copy the data within an array or a subarray