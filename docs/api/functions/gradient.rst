gradient
===========

.. py:function:: gradient(fs, mode="fdiff",  poles_missing_values=False, vector=False)

   Computes the horizontal gradient of each field in a :class:`Fieldset`. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param mode: specifies the computation mode (see below)
   :type mode: {"fdiff", "felem"}, default: "fdiff"
   :param poles_missing_values: puts missing values at the poles when ``mode`` is "felem".
   :type poles_missing_values: bool, default: False
   :param vector: indicates if ``fs`` is a vector field when ``mode`` is "felem" 
   :type vector: bool, default: False
   :rtype: :class:`Fieldset`  
   

   The computation are based on the value of ``mode``.

   When ``mode`` is "fdiff":

   * a second order **finite-difference** approximation is used 
   * the output fields contain missing values at the poles
   * only works for regular latitude-longitude grids

   When ``mode`` is "felem":
   
   * a **finite-element** technique is used
   * works with (regular and reduced) latitude-longitude and Gaussian grids
   * no missing values are allowed in ``fs``!
   * please note that in this mode the computations are performed by :func:`regid` using the nabla option. If ``vector`` is False :func:`regid` is invoked with nabla="scalar_gradient" otherwise  nabla="uv_gradient" is used.
  
   The resulting fieldset contains two fields for each input field: the zonal derivative followed by the meridional derivative.

   The computations for a field f are based on the following formula:

      .. math::

         \nabla f = (\frac {\partial f}{\partial x}, \frac {\partial f}{\partial y}) = (\frac{1}{R \ cos\phi}\frac{\partial f}{\partial \lambda}, \frac{1}{R}\frac{\partial f}{\partial \phi} )
   
   where:

   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.


.. mv-minigallery:: gradient
