shear_deformation
=======================

.. py:function:: shear_deformation(fx, fy)

   *New in Metview version 5.13.0*.

   Computes the shear deformation of 2-dimensional vector fields.  *New in Metview version 5.13.0*.
   
   :param fx: zonal (west-east) vector component fieldset
   :type fx: :class:`Fieldset`
   :param fy: meridional (south-north) vector component fieldset
   :type fy: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   The computations for a vector field f=(fx,fy) are based on the following formula:

   .. math:: 
      
      d(f) = \frac{1}{R \ cos\phi}\frac{\partial f_y}{\partial \lambda} + \frac{1}{R}\frac{\partial f_x}{\partial \phi} + \frac{f_x}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles.  
   
   .. warning::
      :func:`shear_deformation` is only implemented for regular latitude-longitude grids.

   .. note::
      See also :func:`stretch_deformation`, :func:`divergence` and :func:`vorticity`.

.. mv-minigallery:: shear_deformation
