relative_humidity_from_dewpoint
==================================

..  py:function::  relative_humidity_from_dewpoint(t, td)

    Computes the relative humidity from the given temperature (``t``) and dewpoint temperature (``td``).

    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param td: dewpoint temperature (K)
    :type td: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``t`` or None

    The result is the relative humidity in % units. On error None is returned. The computation is based on the following formula:

    .. math:: 
      
        r = 100 \frac {e_{wsat}(Td)}{e_{wsat}(T)}

    where e w\ :sub:`sat` is the saturation vapour pressure over water (see :func:`saturation_vapour_pressure`).

    When the result is a :class:`Fieldset` the ecCodes **paramId** in the output is set to 157 (=relative humidity).

.. mv-minigallery:: relative_humidity_from_dewpoint
