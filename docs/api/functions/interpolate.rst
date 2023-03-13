interpolate
=============


.. py:function:: interpolate(fs, lats, lons)
.. py:function:: interpolate(fs, location)
   :noindex:
.. py:function:: interpolate(fs, gpt)
   :noindex:

   Interpolate the values of ``fs`` to a given location(s) using **bilinear** interpolation. 
     
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lats: target latitude(s)
   :type lats: number or ndarray
   :param lons: target longitudes(s)
   :type lons: number or ndarray
   :param location: single target location defined as a list of [lat, lon]
   :type location: list
   :param gpt: input geopoints
   :type gpt: :class:`Geopoints`
   :rtype: number or ndarray or :class:`Geopoints` or None

   The interpolated point extraction depends on the arguments:
  
   * ``location`` defines a single location. The return value is a number when ``fs`` only contains one field, and a list otherwise. Where it is not possible to generate a sensible value due to lack of valid data in ``fs``, None is returned.

   * ``lats`` and ``lons`` can define either a single location (as number) or multiple locations (as ndarray). If a single location is specified the return value is the same as for ``location``. For multiple locations an ndarray is returned (or a list of ndarrays if there are multiple fields).
   * when ``gpt`` is specified only the first field of ``fs`` is used. The result is a :class:`Geopoints` containing the the nearest gridpoint values for all the locations in ``gpt`` and taking the date, time and level from ``fs``.  Where it is not possible to generate a sensible value due to lack of valid data in ``fs``, NaN is used (this value can be removed from the output with the function :func:`remove_missing_values`).


   .. note::
      
      See also :func:`nearest_gridpoint`.


.. mv-minigallery:: interpolate
