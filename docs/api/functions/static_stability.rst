static_stability
==================

..  py:function:: static_stability(t,  [p, layer=False])

    Computes the static stability used in the **quasi-geostrophic** theory.

    :param t: temperature (K)
    :type t: :class:`Fieldset` or ndarray
    :param p: pressure (Pa)
    :type p: :class:`Fieldset` or ndarray
    :param layer: enable layer mode
    :type layer: bool
    :rtype: same type as ``t`` or None

    The result is the static stability in :math:`m^{2} s^{-2} Pa^{-2}` units. On error None is returned. The following rules are applied when ``t`` is a :class:`Fieldset`:

    * if ``t`` is a pressure level :class:`Fieldset` no ``p`` is needed
    * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``t``.

    The computation is based on the following formula defined in Chapter 2.2. of [Lackman2012]_ : 

    .. math:: 

        \sigma = - \frac{R_{d} T}{p} log(\frac{\partial \Theta}{\partial p})
    
    where

    * :math:`R_{d}`` is the specific gas constant for dry air (287.058 J/(kg K)).
    * :math:`\theta` is the potential temperature (K)

    The ``layer`` argument specifies how the computations are carried out: 

    * when ``layer`` is False (this is the default) :math:`\sigma` is computed by  using :func:`pressure_derivative`
    * when ``layer`` is True ``t`` must contain exactly 2 levels defining the layer. The result will be a single level computed by the following formula:
  
    .. math:: 

            \sigma = - \frac{R_{d} \overline{T}}{\overline{p}} log(\frac{\Delta \theta}{\Delta p})

    where :math:`\overline{T}` and :math:`\overline{p}` are the mean layer values.
       

.. mv-minigallery:: static_stability
