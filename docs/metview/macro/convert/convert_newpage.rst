Adjust newpage() calls
=========================

We can use :func:`newpage` to add a new page to a Postscript or PDF output. In Macro we can call it multiple times for a given :ref:`graphical output <toc_plot_output>`. However, in Python it behaves differently and can only be called as an argument of :func:`plot`. The converter is not able ensure this behaviour, instead a warning is placed to the top of the generated Python script and the adjustment has to be made manually. 

The following example demonstrates how this conversion can be done: 


.. list-table::

   * - **Macro**
   * - 
       .. code-block:: python

        # define PDF output
        setoutput(pdf_output(output_name: "my_output"))
        
        # create display window with one page
        dw = plot_superpage(pages: [plot_page(view: geoview())])
        
        # plot first page
        plot(dw, fs_1, visdef_1)

        # plot second page
        newpage()
        plot(dw, fs_2, visdef_2)
   * - **Python** 
   * - 
       .. code-block:: python

        # define PDF output
        mv.setoutput(mv.pdf_output(output_name="my_output"))

        # create display window with one page
        dw = mv.plot_superpage(pages=[mv.plot_page(view=mv.geoview())])

        # collect all the plot arguments into a list
        plt_data = []
        plt_data.extend([dw, fs_1, visdef_1])
        plt_data.append(mv.newpage())
        plt_data.extend([dw, fs_2, visdef_2])  

        # call plot with all the arguments
        mv.plot(plt_data)


