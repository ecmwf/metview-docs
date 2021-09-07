specific_humidity_from_relative_humidity
===================================================

..  py:function:: specific_humidity_from_relative_humidity(t, r, [p])

    *New in Metview version 5.14.0*.

    Computes the specific humidity from the given temperature (``t``), relative_humidity (``r``) and pressure (``p``). 

    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param r: relative_humidity (%)
    :type r: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``t`` or None

    The result is the specific humidity in kg/kg units. On error None is returned. The following rules are applied when ``t`` and ``r`` are :class:`Fieldset` objects:

    * if ``t`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``t`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``t``
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``t``

    When the result is a :class:`Fieldset` the ecCodes **paramId** in the output is set to 133 (=specific humidity).

    The computation is based on the following equation:
    
    .. math:: 
    
        r = 100 \frac {e(q, p)}{e_{msat}(t)}

    where:
        * e is the vapour pressure (see :func:`vapour_pressure`)
        * e\ :sub:`msat` is the saturation vapour pressure based on the "mixed" phase (see :func:`saturation_vapour_pressure`)
        * t is the temperature
        * r is the relative humidity


    .. note::

        See also :func:`relhum` and :func:`relative_humidity_from_specific_humidity`.


.. mv-minigallery:: specific_humidity_from_relative_humidity