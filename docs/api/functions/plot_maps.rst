plot_maps
=============

.. py:function:: plot_maps(*args, layout=None, view=None, area=None, title_font_size=0.4, legend_font_size=0.35, frame=-1, animate="auto")

   High level function to generate map-based plots.
   
   :param layout: specifies the grid layout as "RxC" where R is the number of rows while C is the number of columns. E.g. "2x1" means 2 rows and 1 column. If it is not set the layout is automatically guessed from the input arguments.
   :type layout: str
   :param view: specifies the map view as a :func:`geoview` or :class:`GeoView`. Cannot be used together with ``area``. 
   :type view:  :func:`geoview` or :class:`GeoView`
   :param area: specifies the map area. It can be either a named built-in area or a list in the format of [S, W, N, E]. When ``area`` is a list a cylindrical map projection is used. Cannot be used together with ``view``.  
   :type area: str or list
   :param title_font_size: specifies the font size in cm for the plot title
   :type title_font_size: number
   :param legend_font_size: specifies the font size in cm for the plot legend
   :type legend_font_size: number
   :param frame: specifies which animation frames should be plotted, -1 means all the frames will be plotted
   :type frame: number
   :param animate: controls plotting multiple animation frames.
   :type animate: str or bool

   At locations where the interpolation is not possible a missing value is returned.
    