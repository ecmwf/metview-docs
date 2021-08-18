plot_maps
=============

.. py:function:: plot_maps(*args, layout=None, view=None, area=None, title_font_size=0.4, legend_font_size=0.35, frame=-1, animate="auto")

    *New in metview-python version 1.8.0*.

    High level function to generate map-based plots.

    :param layout: specifies the grid layout as "RxC" where R is the number of rows while C is the number of columns. E.g. "2x1" means 2 rows and 1 column. If it is not set the layout is automatically guessed from the input arguments.
    :type layout: str
    :param view: specifies the map view as a :func:`geoview`. Cannot be used together with ``area``. 
    :type view:  :func:`geoview`
    :param area: specifies the map area. It can be either a named built-in area or a list in the format of [S, W, N, E]. When ``area`` is a list a cylindrical map projection is used. Cannot be used together with ``view``.  
    :type area: str or list
    :param title_font_size: specifies the font size in cm for the plot title
    :type title_font_size: number
    :param legend_font_size: specifies the font size in cm for the plot legend
    :type legend_font_size: number
    :param frame: specifies which animation frames should be plotted, -1 means all the frames will be plotted
    :type frame: number
    :param animate: controls the plotting of multiple animation frames
    :type animate: str or bool

    :func:`plot_maps` is a convenience function allowing plotting data in a simple way using predefined settings. While the data and map view styles can be fully customised, the title and legend are automatically built and no control is offered over them. 

Customising the map
++++++++++++++++++++++

    If we call :func:`plot_maps` without any arguments the result is a map with the default projection, area and style.

        .. code-block:: python

            mv.plot_maps()

        .. image:: /_static/api/plot_maps_1.png
            :width: 300px

    The input data has to be specified via the positional arguments. For example if we plot a 500 hPa geopotential :class:`Fieldset`

        .. code-block:: python

            import metview as mv
            f = mv.read("my.grib")
            g = f["z500"]
            mv.plot_maps(f)

    To overlay two fields

    specify the input data the plotting style applied to them. :func:`plot_maps` At locations where the interpolation is not possible a missing value is returned.
    