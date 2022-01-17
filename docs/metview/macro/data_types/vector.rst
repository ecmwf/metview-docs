.. _macro_vector:

Vectors in Macro
==================

.. note::

    A vector is an array of numbers designed for high-performance computations. For a full list and details of functions and operators on vectors, see :ref:`Vector functions <macro_vector_fn>`..

Vector basics
++++++++++++++++++++++

Vectors serve as a way to perform computations with diverse data types. For instance, arrays of values can be extracted as vectors from data types such as fieldset , geopoints , netcdf , odb and table . Some of these types also allow their arrays to be set using vectors.

Much of the vector functionality can also be achieved using lists of numbers, but vectors are significantly more efficient for larger sets of numbers (say 1000 or more elements), as lists are not designed to process those quantities of data.

Vectors can also be passed to inline Fortran or C/C++ code for further processing.

Vectors are created using the vector() function and matrices with the matrix() function. Their elements are read or set using the [] operator :

.. code-block:: python

    # Allocate a vector of 5 elements
    v = vector(5)

    # Initialise their value
    for i = 1 to 5 do
        v[i] = i
    end for


Vector literals can be written using the "|" character:

.. code-block:: python

    v = |3,6,7,9,10|
    
    
Vector data types
+++++++++++++++++++++++

By default, the elements of a vector are 64-bit double precision floating point values. By calling the function vector_set_default_type(type), where type can be one of 'float32' and 'float64', you can force all subsequently created vectors to contain elements of that type. A vector of float32 elements consumes half the memory of a float64 vector, but at the expense of some accuracy. The type of a vector can be queried with the dtype() function.

How operators and functions work on vectors
++++++++++++++++++++++++++++++++++++++++++++++

Operations between vectors and vectors are carried out between each pair of corresponding vector values. The result is another vector. Thus :

.. code-block:: python

    Z = X+Y

is equivalent to :

.. code-block:: python

    for each value i
        Zi = Xi + Yi

If one operand is a scalar and the other a vector, the operation is carried out between each vector value and the scalar. The result is another vector. Thus:

.. code-block:: python

    Z = X+n

is equivalent to:

.. code-block:: python
    
    for each value i
        Z i = X i + n

The same logic applies to functions. If the argument of a function is a vector, the result is a vector where each element is the result of the function at the corresponding element in the input vector. Thus :

.. code-block:: python
    Z = f(X)

is equivalent to :

.. code-block:: python

    for each value i
        Z i = f(X i )

Boolean operators such as > or <= produce 0 when the comparison fails, or 1 if it succeeds. Thus :

.. code-block:: python

    Z = X > 0

gives a vector where all the values are either 1 or 0 depending on the corresponding values of the vector X being above 0 or not.

Indexing vectors
+++++++++++++++++++

Indexing a vector allows you to access particular elements inside it. Indexing uses the square bracket operator [] . At its simplest you can use it to extract or refer to a single value inside a vector.

.. code-block:: python

    X[i] = ith value of vector X :

    # copies element 2 of vector X into Y
    Y = X[2]

More sophisticated usage of [] allows you to extract or refer to a range of values.

.. code-block:: python

    x[i,j] = all values of vector X from the ith to the jth :

    # copies values 3, 4, 5, 6, 7 and 8 of X into Y
    Y = X[3,8]

    X[i,j,k] = every kth value of vector X , from the ith to the jth :

    # copies values 1, 5, 9, 13, 17 of X into Y
    Y = X[1,20,4]

An additional fourth parameter specifies how many elements to extract from the current step :

.. code-block:: python

    # copies values 1,2, 5,6, 9,10, 13,14, 17,18 of X into Y
    Y = X[1,20,4,2]

If a vector is holding data representing a rectangular structure, this form could be used to extract a 'sub-area'.

A vector can also be used to provide a set of indexes to another vector:

.. code-block:: python

    # copies values 20, 10, 30 into r
    v = |10, 20, 30, 40|
    i = |2, 1, 3|
    r = v[i] 

Additionally, it is possible to assign a vector to an indexed position in another vector, for example: 

.. code-block:: python

    v[4] = |99,99,99| 
    
In this example, elements 4, 5 and 6 of v will be replaced.

Missing values in vectors
+++++++++++++++++++++++++++++

Vectors can contain missing values. These can be assigned or tested for using the global variable vector_missing_value . Operations between vectors will bypass missing values. For example, if we represent a missing value with an 'x', then the result of

.. code-block:: python

    |1,2,3,x,5| + |2,2,2,2,x|

will be::

    |3,4,5,x,x|

See the descriptions for particular functions and operators for specific details. The bitmap() function can be used to translate between missing values and 'real' values. When a vector is printed with the print() function, missing values are represented by an ' x '.

When a vector is generated from a fieldset, e.g.

.. code-block:: python

    a = values(fieldset)

missing values from the field are automatically translated into missing values in the vector. The same is true when obtaining a vector of values from a geopoints variable. Missing values in vectors are also translated correctly when inserted into fieldsets and geopoints.

Exporting vector data to an ASCII file
+++++++++++++++++++++++++++++++++++++++++

The following piece of code illustrates one way to write the contents of a vector variable to text file:

.. code-block:: python

    # Metview Macro
    
    v = |1,2,5,6,7|
    
    f = file('result.txt') # open a handle to the output file
    
    for i = 1 to count(v) do
        write(f, v[i], ',') # write each element of the vector
    end for
    
    write(f, newline) # write a newline at the end
    
    f = 0 # close the file handle

Making computations more efficient by using vectors
++++++++++++++++++++++++++++++++++++++++++++++++++++++

When performing computations with other data types (fieldsets, geopoints, netcdf), Metview Macro will store intermediate results on disk. This slight overhead can be averted by using vectors instead. The following simple example illustrates what happens.

.. code-block:: python

    a   = read('a.grib')   # a is a fieldset
    b   = read('b.grib')   # b is a fieldset
    spd = sqrt(a*a + b*b)  # some temporary GRIB files generated

Here, three temporary GRIB files will be generated: for the expressions a*a, b*b and their addition (the sqrt function will also generate a file, but as it is the intended result we won't consider it to be temporary). This has the advantage that memory is released between parts of the computation (and only one field from each fieldset is expanded into memory at a time), but there is an overhead of file I/O and GRIB packing/unpacking. Also note that these intermediate results will not be in 64-bit precision, but instead at the precision of their GRIB files.

An alternative is to extract the arrays of values from the fieldsets, do the computation with these, then write the final result back into a fieldset variable. The following code illustrates this, with some renaming of variables in order to keep the names of the variables used in the computation the same as before.

.. code-block:: python

    afs   = read('a.grib')        # afs is a fieldset
    bfs   = read('b.grib')        # bfs is a fieldset
    a     = values(afs)           # a is a vector or a list of vectors
    b     = values(bfs)           # b is a vector or a list of vectors
    spd   = sqrt(a*a + b*b)       # spd is a vector or a list of vectors
    spdfs = set_values(afs, spd)  # write the result back into a fieldset

.. note::

    Notes on this example:

    * no temporary files are generated
    * computations are performed with the default of 64-bit double-precision floating point numbers
    * the vector variables are held in memory
    * the values() function on a fieldset with many fields will yield a list of many vectors, which may require much memory
    * if this is the end of the computation, the vector variables should be freed, e.g.

        .. code-block:: python

            a   = 0
            b   = 0
            spd = 0