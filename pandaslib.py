# PANDAS MODULE (DataFrame object)
# Fundamental Pandas data structures: the Series, DataFrame, and Index.
import pandas as pd
    #SERIES OBJECT
    data = pd.Series([0.25, 0.5, 0.75, 1.0]) #Series Object pd.Series(data, index=index)
    data.values #numpy array object
    data.index #array-like object
    data[(data > 0.3) & (data < 0.8)] #masking
    pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd']) #the index need not be an integer
    series = pd.Series(dictionary) #convert dictionary to pandas series
    series['index1':'index2'] #slicing
    #DataFrame Object
    dataframe = pd.DataFrame({'label1': series1,'label2': series2})
    dataframe.index
    dataframe.columns
    pd.DataFrame(series, columns=['label']) #Constructing DataFrame objects From a single Series object
    pd.DataFrame(a list of dicts) # Constructing DataFrame objects From a list of dicts
    pd.DataFrame({'label': series1,'label2': series2}) # Constructing DataFrame objects From a dictionary of Series objects
    pd.DataFrame(np.random.rand(3, 2),columns=['foo', 'bar'],
                 index=['a', 'b', 'c']) # Constructing DataFrame objects From a two dimensional NumPy array
    pd.DataFrame(np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])) #From a NumPy structured array
    #Index Object (operates like an array but immutable)
    pd.Index([2, 3, 5, 7, 11])
    indA & indB # intersection 
        indA.intersection(indB)
    indA | indB # union
    indA ^ indB  # symmetric difference
    
    