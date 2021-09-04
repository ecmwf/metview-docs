specific_humidity_from_dewpoint
===================================

..  py:function:: specific_humidity_from_dewpoint(td, [p])

    *New in Metview version 5.13.0*.

    Computes the specific humidity from the given dewpoint (``td``) and pressure (``p``). 

    :param td: dewpoint temperature (K)
    :type td: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``td`` or None

    The result is the specific humidity in kg/kg units. On error None is returned. The following rules are applied when ``td`` is a :class:`Fieldset`:

    * if ``td`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``td`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``td``
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``td``

    When the result is a :class:`Fieldset` the ecCodes **paramId** in the output is set to 133 (=specific humidity).

    The computation is based on the following equation:
    
    .. math:: 
    
        e(q, p) = e_{wsat}(td)

    where:
        * e is the vapour pressure (see :func:`vapour_pressure`)
        * e\ :sub:`wsat` is the saturation vapour pressure over water (see :func:`saturation_vapour_pressure`)
        * td is the dewpoint temperature



.. mv-minigallery:: specific_humidity_from_dewpoint