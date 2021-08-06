second_derivative_y
=====================

.. py:function:: second_derivative_y(fs,  mode="fdiff",  poles_missing_values=False)

   Computes the second meridional (from South to North) partial derivative of each field in ``fs`` in */m\ :sup:`2` units. 
   
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
   * the computations for a field f are based on the following formula:
   
      .. math::
   
         \frac {\partial^2 f}{\partial y^2} = \frac{1}{R^2}\frac{\partial^2 f}{\partial \phi^2}

      where:

      * R is the radius of the Earth in m
      * :math:`\phi` is the latitude

   When ``mode`` is "felem":
   
   * a **finite-element** technique is used, and the the first derivative operator is invoked twice
   * works with (regular and reduced) latitude-longitude and Gaussian grids
   * no missing values are allowed in ``fs``!
   * the computations are performed by using :func:`regrid` with the nabla="scalar_gradient" option twice in a row

   .. note::
      See also :func:`second_derivative_x`, :func:`first_derivative_x`, :func:`first_derivative_y` and :func:`gradient`.

.. mv-minigallery:: second_derivative_y
