relative_humidity_from_specific_humidity
===========================================

..  py:function::  relative_humidity_from_specific_humidity(t, q, [p])

    *New in Metview version 5.14.0*.

    Computes the relative humidity from the given temperature (``t``) and specific humidity (``q``) and pressure (``p``).

    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param q: specific humidity (kg/kg)
    :type q: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``t`` or None

    The result is the relative humidity in % units. On error None is returned. The following rules are applied when ``t`` and ``q`` are :class:`Fieldset` objects:

    * if ``t`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``t`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``t``
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``t``

    When the result is a :class:`Fieldset` the ecCodes **paramId** in the output is set to 157 (=relative humidity).
    
    The computation is based on the following formula:

    .. math:: 
      
        r = 100 \frac {e(q, p)}{e_{msat}(t)}

    where:
        * e is the vapour pressure (see :func:`vapour_pressure`)
        * e\ :sub:`msat` is the saturation vapour pressure based on the "mixed" phase (see :func:`saturation_vapour_pressure`)
        * q is the specific humidity
        * p is the pressure
        * t is the temperature


    .. note:: 

        For :class:`Fieldset` data on pressure and model levels :func:`relative_humidity_from_specific_humidity` gives equivalent results to :func:`relhum`.

    .. note::

        See also :func:`relhum` and :func:`specific_humidity_from_relative_humidity`.


.. mv-minigallery:: relative_humidity_from_specific_humidity
