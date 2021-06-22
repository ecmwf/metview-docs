map
=========

.. py:function:: style.map(area="base", style=None)

   Convenience function to create a :class:`GeoView` for map based plotting.
   
   :param area: map area
   :type area: str or list
   :param style: map style
   :type style: str
   :rtype: :class:`GeoView`
   
   ``area`` is either the name of a built in area or a list in [S, W, N, E] format specifying a rectangular area on the cylindrical projection.
   