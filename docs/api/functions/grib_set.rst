grib_set
=============


.. py:function:: grib_set(fs, keys_and_values, repack=False)

   Sets information in the GRIB header of ``fs`` and returns a new :class:`Fieldset`.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list keys_and_values: the ecCodes keys and values
   :param repack: repack data. Sometimes after setting some ecCodes keys (e.g. *packingType*) involving properties of the packing algorithm a repacking of data is needed. *New in Metview version 5.17.0*
   :type repack: bool
   :rtype: :class:`Fieldset`
   
   ``keys_and_values`` has to be a list of the ecCodes keys and their values following each other. The actual data types are deduced from the values passed (and not from the key name!). 

   :Examples:

      .. code-block:: python
         
         import metview as mv

         f = mv.read("my.grib")
         f = mv.grib_set(f, 
            ["date", 20150601,       # int
             "time", 0600,           # int
             "stepType", "avg",      # str
             "startStep", 0 ,        # int
             "endStep", 31,          # int
             "unitOfTimeRange", "D", # str
             "longitudeOfLastGridPointInDegrees", 100.5])  #  float

      .. code-block:: python
         
         import metview as mv

         # GRIB data with ccsds packing
         f = mv.read("ccsds.grib")
         # when we change the packing type repacking must be used
         f = mv.grib_set(f, ["packingType", "grid_simple"], repack=True)


.. py:function:: grib_set_long(fs, keys_and_values, repack=False)
.. py:function:: grib_set_double(fs, keys_and_values, repack=False)
.. py:function:: grib_set_string(fs, keys_and_values, repack=False)
.. py:function:: grib_set_long_array(fs, keys_and_values, repack=False)

   Sets information in the GRIB header of ``fs`` and returns a new :class:`Fieldset`.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list keys_and_values: the ecCodes keys and values
   :param repack: repack data. Sometimes after setting some ecCodes keys (e.g. *packingType*) involving properties of the packing algorithm a repacking of data is needed. *New in Metview version 5.17.0*
   :type repack: bool
   :rtype: :class:`Fieldset`
   
   ``keys_and_values`` has to be a list of the ecCodes keys and their values following each other. The actual values have to match the type of the function. ``grib_set_long_array`` expects a vector containing the values. If applied to a multi-field fieldset, then all fields are modified.

   :Example:

      .. code-block:: python

         f = mv.grib_set_long(f,
            ["centre", 99,
             "level", 200])


.. mv-minigallery:: grib_set

.. mv-minigallery:: grib_set_long
