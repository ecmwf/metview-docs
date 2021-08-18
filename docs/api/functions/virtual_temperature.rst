virtual_temperature
==================================


..  py:function:: virtual_temperature(t, q)

    *New in Metview version 1.5.3*.

    Computes the virtual temperature from the given temperature (``t``) and specific humidity (``q``).

    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param q: specific humidity (kg/kg)
    :type q: number, ndarray or :class:`Fieldset`
    :rtype: same type as ``t`` or None

    The result is the virtual temperature in K units. On error None is returned. 
    
    When the result is a :class:`Fieldset` the ecCodes **paramId** in the output is set to 300012 (=virtual temperature).
    
    The computation is based on the following formula:

    .. math:: 

        T_{v} = T (1 + \frac{1 - \epsilon}{\epsilon} q)

    where

        * T is the temperature
        * q is the specific humidity
        * :math:`\epsilon = \frac{R_{dry}}{R_{vapour}} = 0.621981`


.. mv-minigallery:: virtual temperature
