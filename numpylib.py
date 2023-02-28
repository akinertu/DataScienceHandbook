# NUMPY MODULE (ndarray object)
import numpy as np
#numpy array
    np.array([1, 4, 2, 5, 3])
    np.zeros(10, dtype=int) # Create a length-10 integer array filled with zeros
    np.zeros((3, 5), dtype=int) # Create a 3x5 floating-point array filled with zeros
    np.full((3, 5), 3.14) # Create a 3x5 array filled with 3.14
    np.zeros_like(arr) #Return an array of zeros with the same shape and type as a given array.
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
    np.arange(1, 10).reshape((3, 3)) #put the numbers 1 through 9 in a 3×3 grid
    x[np.newaxis, :] # row vector via newaxis
    x[:, np.newaxis] # column vector via newaxis
    np.concatenate([arr1, arr2]) # joining of two arrays in NumPy
    np.vstack([arr1, arr2y]) # vertically stack the arrays
    np.hstack([arr1, arr2]) # horizontally stack the arrays
    np.split(x, [3, 5]) #Splitting of arrays
    np.vsplit(grid, [2]) 
    np.hsplit(grid, [2])
#numpy computation (ufuncs): Vectorized operations in NumPy are implemented via ufuncs
    np.abs(x)
    np.sin(theta) 
    np.exp(x) #e^x
    np.power(3, x) #3^x
    np.log(x) #ln(x)
    from scipy import special
        special.erf(x)# Error function (integral of Gaussian)
        special.gamma(x) ## Gamma functions (generalized factorials) and related functions
    np.add.reduce(arr) #sum of all elements in thearray
    np.multiply.reduce(arr) # product of all arrayelements
    np.add.accumulate(arr) #intermediate results of the computation
    np.multiply.outer(arr, arr) #output of all pairs of two different inputs
    np.sum() np.prod() #np.sum(arr, axis=1)
    np.prod()
    np.min() np.max #np.min(arr, axis=1)
    np.argmin np.argmax #index of maximum value
    np.mean np.median np.std np.var
    np.any np.all #Evaluate whether all elements are true
    np.array([1, 2, 3, 4, 5]) < 3 #array with a Boolean data type np.less(x, 3)
    np.count_nonzero(x < 6) #number of True entries in a Boolean array
    np.sum(x < 6, axis=1) #how many values less than 6 in each row?
    np.any(x > 8) # are there any values greater than 8?
    np.all(x < 10) # are all values less than 10?
    np.sum((inches > 0.5) & (inches < 1)) #all days with rain less than four inches and greater than one inch?
        & np.bitwise_and
        | np.bitwise_or
        ^ np.bitwise_xor
        ~ np.bitwise_not
    arr[arr < 5] #array filled with all the values that meet thiscondition
    np.sort(arr) 
    np.argsort(arr) #indices of the sortedelements
    arr.sort() #sort the array in-place
    np.sort(arr, axis=0) # sort each column of arr
    np.partition(x, 3) #new array with the smallest K values to the left of the partition