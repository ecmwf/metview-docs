plot_maps
=============

.. py:function:: plot_maps(*args, layout=None, view=None, area=None, use_eccharts=False, title_font_size=0.4, legend_font_size=0.35, frame=-1, animate="auto")

    *New in metview-python version 1.8.0*
    
    High level function with automatic styling to generate map-based plots.

    :param layout: specifies the grid layout as "RxC" where R is the number of rows while C is the number of columns. E.g. "2x1" means 2 rows and 1 column. If it is not set the layout is automatically guessed from the input arguments.
    :type layout: str
    :param view: specifies the map view as a :func:`geoview`. If ``area`` is also specified the projection in the view is changed to cylindrical (but the map style is kept). See :func:`make_geoview` on how to build a view with predefined areas and map styles.
    :type view: :func:`geoview`
    :param area: specifies the map area. It can be either a named built-in area or a list in the format of [S, W, N, E]. When ``area`` is a list a cylindrical map projection is used. 
    :type area: str or list
    :param use_eccharts: when it is True the automatic styling mechanism is bypassed and an :func:`mcont` object with the ecCharts style and legend enabled is applied to all input :class:`Fieldset` data. 
    :type use_eccharts: bool
    :param title_font_size: specifies the font size in cm for the plot title
    :type title_font_size: number
    :param legend_font_size: specifies the font size in cm for the plot legend
    :type legend_font_size: number
    :param frame: specifies which animation frames should be plotted, -1 means all the frames will be plotted
    :type frame: number
    :param animate: controls the plotting of multiple animation frames
    :type animate: str or bool


:func:`plot_maps` is a convenience function allowing to plot data in a simple way using predefined settings. 
    
Data
++++++++++++++++++++++++

The data and the corresponding styles are defined by the positional arguments (``*args``). In the argument list a data object can be followed by any number of visual definitions, which define the plotting style for the given data. If no style is specified for a data object the style will be automatically generated using the currently loaded style configuration. 

Automatic data styling
+++++++++++++++++++++++++

The automatic styling is only available for :class:`Fieldset` and :class:`Track` data.

For a :class:`Fieldset` the assumption is that it only contains fields of the same parameter. The automatic styling is therefore only checks the first two fields to infer if it is scalar or vector data and what the parameter is. The style (:func:`mcont` or :func:`mwind` in this case) is then selected from the current style configuration. If no style configuration is loaded the built-in style is used, which for most of the parameters is equivalent to the ecCharts style.

If ``use_eccharts`` is True the above mentioned automatic styling mechanism is bypassed and an :func:`mcont` object with the ecCharts style and legend enabled is applied to all the :class:`Fieldset` data. This can be useful when a :class:`Fieldset` contains multiple parameters. Please note that the following :func:`plot_maps` calls are equivalent:

    .. code-block:: python

        import metview as mv
        g = mv.read("my.grib")

        c = mv.mcont(contour_automatic_settings="ecmwf", legend="on")
        mv.plot_maps(g, c)

        mv.plot_maps(g, use_eccharts=True)


Layout
+++++++++++++++++++

The positional arguments (``*args``) must either contain non-list values or all of them must be list. In the latter case each list is supposed to describe a sup-plot. The actual grid-layout is then automatically guessed unless ``layout`` directly prescribes it. The following example demonstrates the various layout options:

    .. code-block:: python

        import metview as mv
        
        # grib data with t, z and msl  
        g = mv.read("my.grib")
        t = g["t500"]
        z = g["z500"]
        msl = g["msl"]

        # overlay - single map
        mv.plot_maps(t, z)
        
        # two maps - guessed layout (1x2)
        mv.plot_maps([t], [z])
  
        # two maps - prescribed 2x1 layout
        mv.plot_maps([t], [z], layout="2x1")

        # two maps - overlay, prescribed 2x1 layout
        mv.plot_maps([msl], [t,z], layout="2x1")

    
Limitations
+++++++++++++++

While the data and map view styles can be fully customised, the title and legend are automatically built and no control is offered over them. 


.. mv-minigallery:: plot_maps