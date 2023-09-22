Adjust read() calls with a single argument
===========================================

.. note::
   
    The Macro to Python converter is available from Metview version 5.21.0

When we call :func:`read` with a single argument the converter always assumes it is a path. However, the argument can also be a variable storing a definition and in this case the converted code will be incorrect since it would require run-time information to detect the correct type and apply the proper conversion. Therefore, when the only argument of :func:`read` is a variable a warning is placed at the top of the generated Python script and we might need to adjust the code manually. 

The following table contains a use-case showing both the generated and the correct Python code side by side. We can see that the required fix is very simple, we just need to prefix the variable with ``**`` when passing it to :func:`read`.

.. list-table:: 
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
     - Correct Python code
   * -
       .. code-block:: python
        
          d = (grid: [2, 2], 
              param: "t",
              data: fs)
          r = read(d)

     -
       .. code-block:: python
        
          d = {"grid": [2, 2],
               "param": "t",
               "data": fs}
          r = mv.read(d) # wrong

     -
       .. code-block:: python
        
          d = {"grid": [2, 2], 
               "param": "t",
               "data": fs}
          r = mv.read(**d) # correct

