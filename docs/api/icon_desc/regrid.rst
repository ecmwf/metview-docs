Takes data from a GRIB source and performs a variety of operations on it, including spectral to grid conversion, regridding using a large variety of powerful and flexible interpolation techniques, nabla operators and special consideration of wind fields. :func:`regrid` is designed with re-use in mind. The first time a particular interpolation is performed, it might take some time to compute, but it will create cache files that can be re-used, meaning that the same interpolation will be much faster on subsequent runs.

.. tip::

    There is a :ref:`in-depth introduction <regrid_explained>` available on the use of various Regrid parameters. 