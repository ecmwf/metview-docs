Adjust read() calls
=============================

.. note::
   
    The Macro to Python converter is available from Metview version 5.21.0

In Macro we can call the :func:`read` function with a definition to filter GRIB data. When this definition is passed as a variable to :func:`read` the converter is not able generate the correct Python code, since it would require run-time information. When there is a chance of having this situation, i.e. when the only argument of :func:`read` is a variable a warning is placed to the top of the generated Python script and we might need to adjust the code manually. 

The following table contains a use-case  showing both the generated and the correct Python code side by side. We can see the required fix is actually very simple, we just need to prefix the variable with ``**`` when passing it to :func:`read`.

.. list-table:: 
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
     - Correct Python code
   * -
       .. code-block:: python
        
          d = (grid: [2, 2], 
              param: "t")
          r = read(d)

     -
       .. code-block:: python
        
          d = {"grid": [2, 2],
               "param": "t"}
          r = mv.read(d) # wrong

     -
       .. code-block:: python
        
          d = {"grid": [2, 2], 
               "param": "t"}
          r = mv.read(**d) # correct

