geopotential_from_geometric_height
==================================

.. py:function:: geopotential_from_geometric_height(h)

   Compute the geopotential from geometric height.
   
   :param h: geometric height (m)
   :type z: number, ndarray or :class:`Fieldset`
   :rtype: same type as ``h``  
   
   The computation of geopotential is based on the following formula:

    .. math::
      
        z = \frac{h R g}{R + h}

    where:

    * R is the radius of the Earth (6378388 m)
    * g is the gravitational acceleration (9.81 m/s\ :sup:`2`)

    When a :class:`Fieldset` returned the ecCodes paramId of the resulting fields is
    set to 129 (geopotential).

    .. note::
       See also :func:`geometric_height_from_geopotential`.

.. mv-minigallery:: geopotential_from_geometric_height
