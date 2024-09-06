vorticity
============

.. py:function:: vorticity(fx, fy, mode="fdiff",  poles_missing_values=False)

   Computes the vertical component of the curl differential operator for 2-dimensional vector fields. For wind fields (i.e. when the input fieldsets are u and v wind components) it computes the relative vorticity (:math:`\zeta`).
   
   :param fx: zonal (west-east) vector component fieldset
   :type fx: :class:`Fieldset`
   :param fy: meridional (south-north) vector component fieldset
   :type fy: :class:`Fieldset`
   :param mode: specifies the computation mode (see below). *New in Metview version 1.5.3*.
   :type mode: {"fdiff", "felem"}, default: "fdiff"
   :param poles_missing_values: puts missing values at the poles when ``mode`` is "felem". *New in Metview version 1.5.3*.
   :type poles_missing_values: bool, default: False
   :rtype: :class:`Fieldset`  

   The numerical method to compute the vorticity is based on the value of ``mode``.

   When ``mode`` is "fdiff":

   * a second order **finite-difference** approximation is used 
   * the output fields contain missing values at the poles
   * only works for regular latitude-longitude grids

   When ``mode`` is "felem":
   
   * a **finite-element** technique is used
   * works with (regular and reduced) latitude-longitude and Gaussian grids
   * no missing values are allowed in ``fs``!
   * the computations are performed by using :func:`regrid` with the nabla="uv_vorticity" option


   The computations for a vector field f=(fx,fy) are based on the following formula:

   .. math::
      
      \zeta =\frac{1}{R \ cos\phi}\frac{\partial f_y}{\partial \lambda} - \frac{1}{R}\frac{\partial f_x}{\partial \phi} + \frac{f_x}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude

   If the input fields are horizontal wind components the ecCodes paramIds of the resulting field are set to 138 (relative vorticity).

   .. note::
      See also :func:`divergence`, :func:`shear_deformation` and :func:`stretch_deformation`.

.. mv-minigallery:: vorticity
