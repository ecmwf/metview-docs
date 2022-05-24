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

    The LCL is the level where the parcel becomes saturated during an adiabatic ascend. First, the LCL temperature is computed with the formula [DaviesJones1983]_ (it is also used by the IFS model):

        .. math::

            t_{LCL} =  td - (0.212 + 1.571\times 10^{-3} (td - t_{0}) - 4.36\times 10^{-4} (t - t_{0})) (t - td)

        where :math:`t_{0}` is the triple point of water (273.16 K).

    Then the LCL pressure is computed from :math:`t_{LCL}` using the dry adiabatic equations.
    
    The result is a dict with two members: "t" and "p", containing the temperature and pressure of the LCL, in K and Pa units, respectively. On error or if the LCL does not exist None is returned.

.. mv-minigallery:: lifted_condensation_level
