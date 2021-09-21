
saturation_mixing_ratio
=========================

..  py:function:: saturation_mixing_ratio(t, p, [phase])

    Computes the saturation mixing ratio for a given temperature (``t``), pressure (``p``) and ``phase``.

    :param t: temperature (K)
    :type t: number, ndarray or :class:`Fieldset`
    :param p: pressure (Pa)
    :type p: number, ndarray or :class:`Fieldset`
    :param phase: is either "water", "ice" or "mixed". When it is not specified the "water" phase is used.
    :type phase: str
    :rtype: same type as ``t`` or None

    The result is the saturation mixing ratio in kg/kg units. On error None is returned. The following rules are applied when ``t`` is a :class:`Fieldset`:

    * if ``t`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * if ``t`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``t``
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``t``
  
    The computation is implemented via calling :func:`mixing_ratio` and :func:`saturation_vapour_pressure`:

    .. code-block:: python

        ws = mv.mixing_ratio(p, mv.saturation_vapour_pressure(t, phase))

.. mv-minigallery:: saturation_mixing_ratio
