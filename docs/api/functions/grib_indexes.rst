grib_indexes
============

.. py:function:: grib_indexes(fs)

   Extracts the information required to locate the GRIB messages contained in a Fieldset. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: list of lists
 
   A call to :func:`grib_indexes` with a Fieldset of N fields will return a list of N lists, where each of those N lists
   contains the path, file offset (in bytes) and length (in bytes) of the GRIB message for that field.

