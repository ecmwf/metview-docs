make_geoview
=============

.. py:function:: make_geoview(area=None, style=None)

    .. warning::
        
        This is an experimental feature. New in metview-python version 1.8.0.

        
    High level function to generate a :func:`geoview` with predefined settings. 

    :param area: specifies the map area. It can be either a named built-in area or a list in the format of [S, W, N, E]. When ``area`` is a list a cylindrical map projection is used. For the available named areas see :func:`map_area_gallery`.
    :type area: str or list
    :param style: specifies the map style. It has to be a named built-in map style. For the available styles see :func:`map_style_gallery`.
    :type area: str
    :rtype: :class:`geoview`

