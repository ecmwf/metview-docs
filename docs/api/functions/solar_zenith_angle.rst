solar_zenith_angle
======================

..  py:function::  solar_zenith_angle(fs, to_cosine=False)

    *New in Metview version 5.14.0.*
    
    Computes the solar zenith angle for each gridpoint in ``fs``.
    
    :param fs: input fieldset
    :type fs: :class:`Fieldset`
    :param to_cosine: when this argument is True the cosine of the solar zenith angle is returned
    :type to_cosine: bool
    :rtype: :class:`Fieldset`

    The result is the solar zenith angle in degrees. However, if ``to_cosine`` is set True the cosine of the solar zenith angle is returned. The computations are based on the following formula:

    .. math:: 

        cos\theta_{s} = sin\phi\,  sin\delta + cos\phi\,  cos\delta\, cosh
    
    where:

    * :math:`\theta_{s}` is the solar zenith angle
    * :math:`\phi` is the latitude
    * :math:`\delta` is the declination of the Sun
    * h is the hour angle in local solar time

    The declination of the Sun is computed as:

     .. math:: 

        \delta = - arcsin\left(0.39779 cos(0.98565\unicode{xB0} (N+10) + 1.914\unicode{xB0} sin(0.98565\unicode{xB0} (N-2))\right)

    where:

    * N is the day of the year beginning with N=0 at midnight Universal Time (UT) as January 1. It is a floating point number allowing for fractional days.

    A missing value in any field in ``fs`` will result in a missing value in the corresponding grid point in the output fieldset. 

    The dates and times used in the computations are based on the "validityDate" and "validityTime" ecCodes keys. If these are not available for a given field the result will contain missing values for all the gridpoints for that field. 

    When ``to_cosine`` is False and the GRIB edition of the input field is 2 the ecCodes **paramId** in the output field is set to 260225 (shortName="solza"). For GRIB edition 1 this parameter is not defined.

    When ``to_cosine`` is True the ecCodes **paramId** in the output is set to 214001  (shortName="uvcossza").


.. mv-minigallery:: solar_zenith_angle
