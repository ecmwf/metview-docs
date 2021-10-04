plot_diff_maps
=================

.. py:function:: plot_diff_maps(fs1, [vd1], fs2, [vd2], view=None, area=None, overlay=None, diff_style=[], pos_values=[], title_font_size=0.4, legend_font_size=0.35, frame=-1, animate="auto")

    High level function to generate difference plots between two :class:`Fieldset` objects (``fs1`` and ``fs2``).

    :param fs1: specifies the first input :class:`Fieldset`. Has to contain the same number of fields on the same grid as ``fs2``.
    :type fs1:  :class:`Fieldset`
    :param fs2: specifies the second input :class:`Fieldset`. Has to contain the same number of fields on the same grid as ``fs1``.
    :type fs2:  :class:`Fieldset`
    :param view: specifies the map view as a :func:`geoview`. If ``area`` is also specified the projection in the view is changed to cylindrical (but the map style is kept). See :func:`make_geoview` on how to build a view with predefined areas and map styles.
    :type view:  :func:`geoview`
    :param area: specifies the map area. It can be either a named built-in area or a list in the format of [S, W, N, E]. When ``area`` is a list a cylindrical map projection is used. 
    :type area: str or list
    :param overlay: specifies the data and the corresponding style that should be plotted as an overlay onto each map
    :type overlay: data-like, list or tuple
    :param diff_style: user defined contouring style for the difference plots. If it is not defined a predefined style is used.
    :type diff_style: an :func:`mcont` or list of these
    :param pos_values: all the predefined difference contour styles use two :func:`mcont` objects; the first defining the negative value range while the other the positive one. The value ranges are symmetrical i.e. mirrored to 0. ``pos_values`` allows to define a new value range for the default style; it sets the positive value range and the negative one is automatically generated from it.
    :type pos_values: a style or list of styles
    :param title_font_size: specifies the font size in cm for the plot title
    :type title_font_size: number
    :param legend_font_size: specifies the font size in cm for the plot legend
    :type legend_font_size: number
    :param frame: specifies which animation frames should be plotted, -1 means all the frames will be plotted
    :type frame: number
    :param animate: controls the plotting of multiple animation frames
    :type animate: str or bool


:func:`plot_diff_maps` is a convenience function allowing to plot the difference between the ``fs1`` and ``fs2`` :class:`Fieldset` objects in a simple way using predefined settings.


Layout 
+++++++++++++++++

The layout is fixed: ``fs1`` and ``fs2`` are always  plotted in the bottom row while their difference (``fs1`` - ``fs2``) will appear in the top row, as the snapshot below illustrates it:

    .. image:: /_static/api/plot_diff_maps_1.png
            :width: 400px


Styling the input data maps
++++++++++++++++++++++++++++++

The corresponding styles for ``f1`` and ``f2`` are defined by the positional arguments (``*args``). In the argument list both ``f1`` and ``f2`` can be followed by any number of visual definitions, which define the plotting style for the given data. If no style is specified for a data object the style will be automatically generated using the currently loaded style configuration. 

Styling the difference map
++++++++++++++++++++++++++++++

The contouring style for the difference plot is defined by ``diff_style``: it can be a single :func:`mcont` or a list of it. If no style is specified the it will be automatically generated using the currently loaded style configuration. In this case ``pos_values`` can be used to adjust the contour value range.

Limitations
++++++++++++++

While the data and map view styles can be fully customised, the title and legend are automatically built and no control is offered over them. 

.. mv-minigallery:: plot_diff_maps

