rmask
=========

.. py:function:: rmask(fs, circle, missing=False)
.. py:function:: rmask(fs, lat, lon, radius, missing=False)
   :noindex:

   For each field in ``fs`` creates a field containing grid point values of 0 or 1 according to whether
   their distance to a given geographical location is larger or smaller than a given radius. 0 is
   assigned to points outside the radius and 1 to points inside the radius.  An additional named
   argument, ``missing`` set to ``True`` will change the behaviour so that points outside the area
   will become missing values and points inside the area retain their original value.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param circle: circle as a list of [lat, lon, radius]
   :type circle: list[number]
   :param number lat: latitude coordinate of the centre of the circle
   :param number lon: longitude coordinate of the centre of the circle
   :param number radius: radius of the circle in m
   :param missing: set to ``True`` to change the behaviour as described above. *New in Metview version 5.13.0*.
   :type missing: bool
   :rtype: :class:`Fieldset`

   .. note::
      
      See also :func:`mask`, :func:`poly_mask`, :func:`bitmap` and :func:`nobitmap`.

.. mv-minigallery:: rmask
