lifted_condensation_level
===========================

..  py:function:: lifted_condensation_level(t, td, p)

    Computes the Lifted Condensation Level (LCL) for a parcel ascending from a given temperature, dewpoint and pressure.
   
    :param t: initial temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param td: initial dew point temperature (K)
    :type td: number, ndarray or :class:`Fieldset`
    :param p: initial pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :rtype: dict or None

    The LCL is the level where the parcel becomes saturated during an adiabatic ascend. First, the LCL temperature is computed with the formula from [Bolton1980]_:

        .. math::

            t_{LCL} = 56.0 +  \frac{1}{\frac{1}{td - 56} + \frac{log(\frac{t}{td})}{800}}


    Then the LCL pressure is computed from :math:`t_{LCL}` using the dry adiabatic equations.
    
    The result is a dict with two members: "t" and "p", containing the temperature and pressure of the LCL, in K and Pa units, respectively. On error or if the LCL does not exist None is returned.

.. mv-minigallery:: lifted_condensation_level
