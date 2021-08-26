.. _macro_vector_fn:

Vector functions
========================


For an overview, please see Vectors.

.. describe:: vector ( vector op vector )

    Operation between two vectors. op is one of the operators below :

    * \+ Addition
    * \- Subtraction
    * \* Multiplication
    * / Division
    * ^ Power
        
    The vectors returned by these boolean operators are boolean vectors (containing only 1 where result is true, 0 where it is false):

    * > Larger Than     
    * < Smaller Than
    * >= Larger or Equal
    * <= Smaller or Equal
    * = Equal       
    * <> Not Equal

    In all of the above operations, a missing value in one of the input vectors results in a corresponding missing value in the output vector.


.. describe:: vector ( vector op number )
.. describe:: vector ( number op vector )

    Operations between vectors and numbers. op is any of the operations defined above. A missing value in either input vector will result in a missing value in the corresponding place in the output vector.

.. describe:: vector ( vector and vector )
.. describe:: vector ( vector or vector )
.. describe:: vector ( not vector )

    Conjunction, Disjunction and Negation. Boolean operators consider all null values to be false and all non null values to be true. The vectors created by boolean operators are binary vectors (containing only 1 where result is true, 0 where it is false). For example :

    .. code-block:: python
    
        a = |1,2,3,0|
        b = |0,5,6,7|
        c = a and b

    creates a vector c with values of 1 where the corresponding values of vector a and vector b are both non zero, and 0 otherwise. A missing value in either input vector will result in a missing value in the corresponding place in the output vector.


.. describe:: vector ( vector and number )
.. describe:: vector ( number or vector )

    Boolean operations between vectors and numbers. See above. A missing value in either input vector will result in a missing value in the corresponding place in the output vector.


.. describe:: vector ( vector & vector & ... )
.. describe:: vector ( nil & vector & ... )
.. describe:: vector ( vector & nil )
.. describe:: vector merge( vector,vector,... )

    Merge several vectors. The output is a vector with as many elements as the total number of elements in all merged vectors. Merging with the value nil does nothing, and is used to initialise when building a vector from nothing.


.. describe:: vector vector[number]
.. describe:: vector vector[number,number]
.. describe:: vector vector[number,number,number]
.. describe:: vector vector[number,number,number,number]

    Extract a selection of elements from a vector. If one parameter is given, only one element is selected. If two parameters are given, the elements ranging from the first to the last index are returned. The optional third parameter represents an increment n - every nth element from the first to the last index are returned. The optional fourth parameter specifies how many elements to take each time.

    .. code-block:: python

        # copies fields 1, 5, 9, 13, 17 of x into y
        Y = X[1,20,4]

.. describe:: vector vector[vector]

    Extract a selection of elements from a vector. The vector supplied as the argument provides the set of indices to be used. For example:

    .. code-block:: python

        v = |10, 20, 30, 40|
        i = |2, 1, 3|
        r = v[i] # r is now |20, 10, 30|   

.. describe:: vector abs( vector )

    Returns the vector of the absolute value of the input vector at each element. Missing values are retained, unaltered by the calculation.


.. describe:: vector acos( vector )
.. describe:: vector asin( vector )
.. describe:: vector atan( vector )

    Return the vector of the arc trigonometric function of the input vector at each element. Result is in radians. Missing values are retained, unaltered by the calculation.


.. describe:: vector bitmap (vector,number)

    Returns a copy of the input vector (first argument) with zero or more of its values replaced with missing value indicators. The second argument is a number - any value equal to that number in the input vector is replaced with the missing value indicator. See also nobitmap.


.. describe:: vector cos( vector )

    Returns the vector of the cosine of the input vector at each element. Input values must be in radians. Missing values are retained, unaltered by the calculation.


.. describe:: number count( vector )

    Returns the number of elements in a vector.


.. describe:: vector div( vector,vector )

    Returns a vector with as many elements as the input vectors; the elements of the output vector are the integer part of the division of the first vector by the second vector. A missing value in either input vector will result in a missing value in the corresponding place in the output vector.


.. describe:: vector dtype( vector )

    Returns a string describing the data type of the elements of the given vector, either 'float32' or 'float64'.


.. describe:: vector exp( vector )

    Returns the vector of the exponential of the input vector at each element. Missing values are retained, unaltered by the calculation.


.. describe:: vector exp( vector )
.. describe:: vector filter( vector,vector )

    Takes two vectors, and returns a new vector containing only the values of the first vector where the second vector's values are non-zero and non-missing. Examples:

    .. code-block:: python
    
        v1 = filter(v, v>273.15) # returns only the values above 273.15
        v2 = filter(v, v <> vector_missing_value) # returns only the non-missing values


.. describe:: number or vector find( vector,number )
.. describe:: number or vector find( vector,number,string )

    Searches the given vector for a number and returns the index of the first occurrence of it. If an optional third argument is given as the string 'all', then a vector of the indexes of all occurrences of the number is returned. In both cases, if the number is not contained in the vector, nil is returned.

.. describe:: vector int( vector )

    Returns the vector of the integer part of the input vector at each element. Missing values are retained, unaltered by the calculation.


.. describe:: vector log( vector )

    Returns the vector of the natural log of the input vector at each element. Missing values are retained, unaltered by the calculation.


.. describe:: vector log10( vector )

    Returns the vector of the log base 10 of the input vector at each element. Missing values are retained, unaltered by the calculation.


.. describe:: vector max( vector,vector )   
.. describe:: vector min( vector,vector )

    Returns the vector of maximum (minimum) value of the two input vectors at each element. A missing value in either input vectors will result in a missing value in the corresponding place in the output vectors.


.. describe:: vector max( vector,number )
.. describe:: vector min( vector,number )

    Returns the vector of the maximum (minimum) of the number and the vector value at each element. Missing values in the input vector are transferred to the output vector.


.. describe:: number maxvalue( vector )
.. describe:: number minvalue( vector )

    Returns the vector (minimum) value of all the values of the vector. Only non-missing values are considered in the calculation. If there are no valid values, the function returns the missing value indicator.


.. describe:: number mean( vector )

    Returns the mean of all non-missing values in the input vector. If there are no valid input values, then nil is returned.


.. describe:: vector merge( vector,vector,... )

    Merge several vectors. The same as the operator &. The output is a vector with as many elements as the total number of elements in all merged vectors. Merging with the value nil does nothing, and is used to initialise when building a vector from nothing.


.. describe:: vector mod( vector,vector )

    Returns a vector where the elements are the remainder of the division of the first vector by the second vector. A missing value in either input vector will result in a missing value in the corresponding place in the output vector. Note that only the integer parts of the inputs are considered in the calculation, meaning that a second parameter of 0.5 would cause a division by zero.


.. describe:: vector neg( vector )

    Returns the vector of the negative of the input vector at each element. The same as (-vector). Missing values are retained, unaltered by the calculation.


.. describe:: vector nobitmap ( vector,number )

    Returns a copy of the input vector (first argument) with all of its missing values replaced with the number specified by the second argument. See also bitmap.


.. describe:: vector or list percentile( list,vector )
.. describe:: vector or list percentile( list,list )
.. describe:: vector or list percentile( list,number )

    From a given list of V vectors, each with the same number, N, of elements, and a set of P percentiles, computes a new list of P vectors, each containing N elements - one percentile for each of the N elements across all V input vectors. The function implements the nearest neighbour algorithm. The set of percentiles is supplied as the second argument and can be a vector, a list or a single number. If it is a single number then the result will be a single vector rather than a list of vectors; however, supplying a vector or list with just one percentile will result in a list of one vector result. The function complements the Percentile module, which acts directly on GRIB fields.

    One example use of this function is to simulate the Percentile module, but using data that is all in memory. The following code does exactly that, but starts and ends with GRIB data.

    .. code-block:: python

        data = read('my_data.grib')
        vals = values(data)
        percents = percentile(vals, [100, 90, 89, 80, 75, 55])
        new_grib = set_values(duplicate(data[1], 6), percents)
        vector percentile( vector,list )

    Computes, from a single array of data in the first argument, the percentiles listed in the second argument. For example:

    .. code-block:: python

        p = percentile(vdata, |2, 99, 60|) # vector of 3 percentiles


.. describe:: vector sgn( vector )

    Returns the vector of the sign of the values of the input vector at each element-1 for negative values, 1 for positive and 0 for null values. Missing values are retained, unaltered by the calculation.


.. describe:: vector sin( vector )

    Returns the vector of the sine of the input vector at each element. Input vector must have values in radians. Missing values are retained, unaltered by the calculation.


.. describe:: vector sort( vector )
.. describe:: vector sort( vector,string )

    Returns a sorted version of the given vector. If no second argument is given, the result will be sorted in ascending order; otherwise, a second argument consisting of a string can be given: '<' for ascending, '>' for descending order.


.. describe:: vector sort_indices( vector )
.. describe:: vector sort_indices( vector,string )

    Performs the same sorting as the sort() function, but instead of returning the sorted values, it returns the indices ofwhere the sorted values lie in the original vector. For example:

    .. code-block:: python

        v1 = |5, 3, 4, 9, 1, 4.2|
        sort(v1)                  # returns |1, 3, 4, 4.2, 5, 9|
        sort_indices(v1)          # returns |5, 2, 3, 6, 1, 4|, e.g. the 4th sorted number is the 6th element from the original


.. describe:: vector sqrt( vector )

    Returns the vector of the square root of the input vector at each element. Missing values are retained, unaltered by the calculation.


.. describe:: number sum( vector )

    Returns the sum of all non-missing values in the input vector. If there are no valid input values, then nil is returned.


.. describe:: vector tan( vector )

    Return the tangent of the input vector at each element. Input vector must have values in radians. Missing values are retained, unaltered by the calculation.


.. describe:: vector tolist( vector )

    Converts the input vector to a list. Missing values are converted to nil.


.. describe:: vector unique( vector )

    Returns a vector of the unique elements in the input vector.


.. describe:: vector vector_set_default_type( string )

    Sets the default type of new vectors to the type specified by the input string, either 'float32' or 'float64'. The initial default type is float64. After changing the default type, all subsequently created vectors, including the results of operations on existing vectors, will have the new default data type.