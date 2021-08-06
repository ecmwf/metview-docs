first_derivative_x
====================

.. py:function:: first_derivative_x(fs, mode="fdiff",  poles_missing_values=False)
   
   Computes the zonal (from West to East) partial derivative of each field in ``fs`` in */m units. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :param mode: specifies the computation mode (see below)
   :type mode: {"fdiff", "felem"}, default: "fdiff"
   :param poles_missing_values: puts missing values at the poles when ``mode`` is "felem".
   :type poles_missing_values: bool, default: False
   :rtype: :class:`Fieldset`
   
   The numerical method to compute the derivative is based on the value of ``mode``. 
   
   When ``mode`` is "fdiff":

   * a second order **finite-difference** approximation is used 
   * the output fields contain missing values at the poles
   * only works for regular latitude-longitude grids

   When ``mode`` is "felem":
   
   * a **finite-element** technique is used
   * works with (regular and reduced) latitude-longitude and Gaussian grids
   * no missing values are allowed in ``fs``!
   * please note that in this mode the computations are performed by :func:`regrid` using the nabla="scalar_gradient" option. 

   The computations for a field f are based on the following formula:

   .. math::

      \frac {\partial f}{\partial x} = \frac{1}{R \ cos\phi}\frac{\partial f}{\partial \lambda} 

   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   .. note::
      See also :func:`first_derivative_y`, :func:`second_derivative_x`, :func:`second_derivative_y` and :func:`gradient`.


.. mv-minigallery:: first_derivative_x
