
Adjust plot() calls
=============================

.. note::
   
    The Macro to Python converter is available from Metview version 5.21.0

In Macro we can call :func:`plot` multiple times for a given :ref:`graphical output <toc_plot_output>`. However, in Python it behaves differently and only the result of the last call is kept. The converter is not able to merge multiple :func:`plot` calls into a single one, instead a warning is placed to the top of the generated Python script and the adjustment has to be made manually. 

In Macro we use multiple :func:`plot` calls
for a :ref:`graphical output <toc_plot_output>` when we have a layout, i.e. we use :func:`plot_superpage` with multiple pages. The following examples show how to do the Macro to Python conversion in this case: 

.. list-table:: Calling plot in multiple lines in Macro
 
   * - **Macro code**
   * - 
       .. code-block:: python

        # create a 1x2 layout
        dw = plot_superpage(pages: mvl_regular_layout(geoview(), 2, 1, 1, 1))

        # invoke a plot command for each layout page separately
        plot(dw[1], fs_1, visdef_1)
        plot(dw[2], fs_2, visdef_2)
   * - **Adjusted Python code** 
   * -
       .. code-block:: python

        # create a 1x2 layout
        dw = mv.plot_superpage(pages=mvl_regular_layout(mv.geoview(), 2, 1, 1, 1))
                
        # collect all the plot arguments into a list
        plt_data = []
        plt_data.extend([dw[0], fs_1, visdef_1])
        plt_data.extend([dw[1], fs_2, visdef_2])   
        
        # call plot with all the arguments
        mv.plot(plt_data)


.. list-table:: Calling plot in a loop in Macro

   * - **Macro code**
   * - 
       .. code-block:: python

        # create a 1x2 layout
        dw = plot_superpage(pages: mvl_regular_layout(geoview(), 2, 1, 1, 1))
        
        for i=1 to count(dw) do
            plot(dw[i], fs[i])
        end for
   * - **Adjusted Python code**
   * - 
       .. code-block:: python

        # create a 1x2 layout
        dw = mv.plot_superpage(pages=mvl_regular_layout(mv.geoview(), 2, 1, 1, 1))
        
        # collect all the plot arguments into a list
        plt_data = []
        for i in range(len(dw)):
            plt_data.extend([dw[i], fs[i]])
        
        # call plot with all the arguments
        mv.plot(plt_data)

