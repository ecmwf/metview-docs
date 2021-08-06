divergence
==============

.. py:function:: divergence(fx, fy, mode="fdiff",  poles_missing_values=False)

   Computes the divergence of 2-dimensional vector fields. 
   
   :param fx: zonal (west-east) vector component fieldset
   :type fx: :class:`Fieldset`
   :param fy: meridional (south-north) vector component fieldset
   :type fy: :class:`Fieldset`
   :param mode: specifies the computation mode (see below)
   :type mode: {"fdiff", "felem"}, default: "fdiff"
   :param poles_missing_values: puts missing values at the poles when ``mode`` is "felem".
   :type poles_missing_values: bool, default: False
   :rtype: :class:`Fieldset`  
   
   The numerical method to compute the divergence is based on the value of ``mode``.

   When ``mode`` is "fdiff":

   * a second order **finite-difference** approximation is used 
   * the output fields contain missing values at the poles
   * only works for regular latitude-longitude grids

   When ``mode`` is "felem":
   
   * a **finite-element** technique is used
   * works with (regular and reduced) latitude-longitude and Gaussian grids
   * no missing values are allowed in ``fs``!
   * the computations are performed by using :func:`regrid` with the nabla="uv_divergence" option

   The computations for a vector field f=(fx,fy) are based on the following formula:

   .. math:: 
      
      div(f) = \frac{1}{R \ cos\phi}\frac{\partial f_x}{\partial \lambda} + \frac{1}{R}\frac{\partial f_y}{\partial \phi} - \frac{f_y}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   If ``fx`` and ``fy`` are horizontal wind components the ecCodes **paramId** of the resulting field is set to 155 (=divergence). 
   
   .. note::
      See also :func:`vorticity`, :func:`shear_deformation` and :func:`stretch_deformation`.


.. mv-minigallery:: divergence
