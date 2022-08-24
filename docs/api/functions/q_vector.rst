q_vector
==================

..  py:function:: q_vector(t, z, static_stability=2E-6, coriolis=None)

    Computes the Q-vector used in the quasi-geostrophic (QG) theory. It can determine the forcing for vertical motion in mid-latitude synoptic scale weather systems.
    
    :param t: temperature (K) on pressure levels
    :type t: :class:`Fieldset`
    :param z: geopotential (:math:`m^{2} s^{-2}`) on the same pressure levels as ``t``
    :type z: :class:`Fieldset`
    :param static_stability: :func:`static_stability` parameter (:math:`m^{2} s^{-2} Pa^{-2}`). In the QG theory this is a constant on a given pressure level. If it is specified as an ndarray it must define a value for each pressure level in ``t`` and ``z``. It is also possible to use a :class:`Fieldset` here. In this case ``static_stability`` must contain either a single field or as many fields as there are in ``t`` and ``z``.
    :type static_stability: number or ndarray or :class:`Fieldset`
    :param coriolis: set a constant Coriolis parameter value (1/s) for the :func:`geostrophic_wind` computations. If it is None (the default) the real Coriolis parameter is computed for each gridpoint.
    :type coriolis: number
    :rtype: :class:`Fieldset`

    The result is the Q-vector in :math:`m^{-2} s^{-1} Pa` units as defined in [Bluestein1992]_:
    
    .. math:: 

            \vec{Q} = - \frac{R_{d} {T}}{\sigma} (\frac{\partial \vec{v_{g}}}{\partial x} \nabla T, \frac{\partial \vec{v_{g}}}{\partial y} \nabla T)

    where
    
    * :math:`R_{d}` is the specific gas constant for dry air (287.058 J/(kg K))
    * :math:`\sigma` is the :func:`static_stability`
    * :math:`\vec{v_{g}}` is the :func:`geostrophic_wind` computed as:

        .. math::

            \vec{v_{g}} = (-\frac{1}{f_{0}} \frac{\partial z}{\partial y}, \frac{1}{f_{0}} \frac{\partial z}{\partial x})

        where :math:`f_{0}` is a constant Coriolis parameter defined by ``coriolis``. However, if ``coriolis`` is not specified the real Coriolis parameter is used in each gridpoint.
  
    The Q-vector gains importance because the QG omega equation can be written as:

    .. math::

        (\nabla^{2} + \frac{f^{2}_{0}}{\sigma} \frac{\partial^{2}}{\partial p^{2}}) \omega = -2 \nabla \vec{Q}

    (after ignoring the term containing :math:`\frac{\partial f}{\partial y}` on the right-hand side). Thus :math:`-2 \nabla \vec{Q}` determines the forcing for vertical motion. 
   
    Some remarks on the use of :func:`q_vector`:

    * when using NWP fields to compute the Q-vector (or the :math:`-2 \nabla \vec{Q}` term) the results are usually extremely noisy due to the product of spatial derivatives. Therefore it is advised to apply a smoothing or spatial filter on the input data even when the grid resolution is low (see Chapter 2.3. of [Lackman2012]_).
    * the equations in the QG theory are derived in an orthogonal Descartian co-ordinate system. However, in Metview the horizontal derivatives are always computed on the sphere. Therefore some of the assumptions in the QG theory, e.g. the divergence of the geostrophic wind as defined above is always zero, will not be true.
    * the derivatives are computed with a second order finite-difference approximation. The resulting fieldset contains two fields for each input field: the x and y Q-vector components. In each output field the points close to the poles and the Equator are bitmapped (they contain missing values). 
   
    .. warning::

      :func:`q_vector` is only implemented for regular latitude-longitude grids.

    .. note::

      See also :func:`static_stability` and :func:`geostrophic_wind`.

.. mv-minigallery:: q_vector
