Adjust vector slicing
=============================

.. note::
   
    The Macro to Python converter is available from Metview version 5.21.0

Vectors in Macro are automatically converted to numpy arrays in Python and slicing is correctly resolved, like this:

.. list-table:: Vector literals and slicing converted to Python
   :header-rows: 1
 
   * - Macro
     - Generated Python code
   * -
       .. code-block:: python
            
        v = |1, 2, 3, 4, 5|
        # first 2 elements
        v1 = v[1, 2]     
        # every second element
        v1 = v[1, 5, 2] 
     -
       .. code-block:: python

        v = np.array([1, 2, 3, 4, 5])
        # first 2 elements
        v1 = v[0:2]     
        # every second element
        v1 = v[0:5:2] 
        
However, Macro supports vector slicing using 4 arguments with *start,end,step,num*, which is not supported in numpy. To overcome this problem whenever this happens Metview's built-in :func:`mv.compat.index4` method is used to generate the right indices for the slicing.

.. note::
   
   :func:`mv.compat.index4` is available from Metview Python version 1.16.0

The following examples shows how :func:`mv.compat.index4` is actually used.

.. list-table:: Resolving slicing based on 4 arguments
   :header-rows: 1
 
   * - Macro
     - Generated Python code
   * -
       .. code-block:: python
            
        v = |1, 2, 3, 4, 5, 6, 7|
        # two values from every 3rd element
        # resulting in: 1, 2, 4, 5
        v1 = v[1, 6, 3, 2]     
     -
       .. code-block:: python

        v = np.array([1, 2, 3, 4, 5, 6, 7])
        # two values from every 3rd element
        # resulting in: 1, 2, 4, 5
        v1 = v[mv.compat.index4(v, 0, 6, 3, 2)]   
      
