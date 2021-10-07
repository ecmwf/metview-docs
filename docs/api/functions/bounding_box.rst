bounding_box
=======================

.. py:function:: bounding_box(fs)

    Returns the geographical bounding box for each field in ``fs``.
   
    :param fs: input fieldset
    :type fs: :class:`Fieldset`
    :rtype: 1D or 2D ndarray 
  
    If ``fs`` contains a single field the result is a 1D ndarray containing the bounding box as S,W,N,E. As for the longitude values, it is guaranteed that they are always between -180 and 360 and W < E.

    If ``fs`` contains multiple fields the result is a 2D ndarray (one S,W,N,E array for each field).

    For a global field the result is always::
        
         array([-90, -180, 90, 180])


    .. warning::

        :func:`bounding_box` only works for regular/reduced latitude-longitude and Gaussian grids.


.. mv-minigallery:: bounding_box