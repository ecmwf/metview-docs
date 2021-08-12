mvl_geocircle
===============

.. py:function:: mvl_geocircle(lat, lon, radius, resolution)

   Plots a circle defined on Earth's surface with a given radius in km onto a map in any projections. It is possible to split the circle into disk sectors with different radii.
   
   :param lat: latitude of the centre of the circle
   :type lat: number
   :param lon: longitude of the centre of the circle
   :type lon: number
   :param radius: radius of the circle in km; or a list with the radii of the disk sectors the circle is split into
   :type radius: number or list
   :param resolution: number of line segments to make up the circle
   :type resolution: number
   :rtype: :func:`input_visualiser`
   
   Internally, the circle is split into ``resolution`` number of segments and the returned result is an :func:`input_visualiser` object which can be passed to :func:`plot` along with an optional :func:`mgraph` object.

   When ``radius`` is a list each item in the list defines a radius for a disk sector. E.g. when the list contains four items they define the quadrants the circle is to split into (see the  :ref:`Storm Wind Quadrants <gallery_storm_quadrants>` example).
   

.. mv-minigallery:: mvl_geocircle
