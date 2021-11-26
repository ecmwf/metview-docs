map_area_gallery
==================

.. py:function:: map_area_gallery()
    
    *New in metview-python version 1.8.0*

    Generates a gallery of the built-in map areas in a Jupyter notebook.

    The list of available areas depends on the actual style configuration. By default, when no custom style configuration is loaded, the area list comprises of:
    
    * the core areas available under the ``area_name`` parameter in :func:`geoview`
    * the area called "base", which is the same as the "global" core area  

    All the area names can be used with :func:`make_geoview` to create map-based views, e.g.:

    .. code-block:: python

        view = mv.make_geoview(area="pacific")

    
    Additionally, the core areas (these are highlighted in orange in the gallery) can be used in :func:`geoview` too, e.g.:

    .. code-block:: python

        view = mv.geoview(area_mode="user", area_name="central_europe")

    The default map area gallery looks like this:
    
    .. image:: /_static/api/map_area_gallery.png
        :width: 800px
