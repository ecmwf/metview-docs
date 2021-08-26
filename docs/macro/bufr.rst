BUFR Functions
======================


   Due to the nature of the data, the macro language provides little in the way of functions to process BUFR data - you can only merge and/or plot them.

   If you need to do more, you have to convert them to geopoints using the obsfilter() request. .


.. describe:: bufr (observations & observations)
.. describe:: bufr merge (bufr, bufr)

   Merges two sets of BUFR.


.. describe:: bufr obsfilter ( definition )
.. describe:: geopoints obsfilter ( definition )

   This function accepts BUFR input, filters out part of that input (optional) and returns BUFR data (default) or geopoints (if user so specifies) in one of three :class:`Geopoints` formats. See :func:`obsfilter` for details.

   
