:nosearch:

Adjust vector slicing
=============================

.. note::
   
    The Macro to Python converter is available from Metview version 5.20.0

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
        
However, Macro supports vector slicing using 4 arguments with *start,end,step,num*, which is not supported in numpy. To overcome this problem whenever this happens a local function called ``_slice4()`` will be added to the top of the generated Python script and the slicing will be resolved by calling this function.

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
        v1 = _slice4(0, 6, 3, 2)    
      
