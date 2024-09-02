geometric_height_from_geopotential
==================================

.. py:function:: geometric_height_from_geopotential(z)

   Compute the geometric height from geopotential.
   
   :param z: geopotential (m2/s2)
   :type z: number, ndarray or :class:`Fieldset`
   :rtype: same type as ``z``  
   
   The computation of geometric height is based on the following formula:

    .. math::
      
        h = \frac{R \frac{z}{g}}{R - \frac{z}{g}}
    
    where:

    * R is the radius of the Earth (6378388 m)
    * g is the gravitational acceleration (9.81 m/s\ :sup:`2`)

    When a :class:`Fieldset` returned the ecCodes paramId of the resulting fields is
    set to 3008 (geometric height).

    .. note::
      See also :func:`geopotential_from_geometric_height`, :func:`ml_to_hl`.

.. mv-minigallery:: geometric_height_from_geopotential
