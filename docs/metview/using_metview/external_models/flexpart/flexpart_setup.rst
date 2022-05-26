.. _flexpart_setup:

FLEXPART setup
//////////////

What Metview version is required?
=================================

Metview versions **5.0.0**. or later are required.

What FLEXPART version is required?
==================================

Only version **902** is supported.

.. note::

    Please note that FLEXPART is not an ECMWF development. FLEXPART is 
    *not distributed* with Metview, but it has to be installed         
    separately. Please visit the FLEXPART website for installation     
    instructions: https://www.flexpart.eu/.                            

Compilation
===========

Metview can only be compatible with FLEXPART if the size of the fortran
**record marker** in the unformatted FLEXPART output is set to 4 bytes.
Modern fortran compilers has an option to guarantee it. E.g. for
**gfortran**::

    -frecord-marker=4                                                  

Code modifications
==================

To make FLEXPART work with ECMWF data the following modifications has to
be made in the source code:

- Resolve type mismatch in err.f90 with newer gfortran compiler: see flextra ticket49

    This involves the modification in **err.f90** of line 106 and 111

    .. image:: /_static/ug/flexpart_setup/image1.png
    :width: 5.90069in
    :height: 1.49569in

    and line 140 and 145 as well.

    .. image:: /_static/ug/flexpart_setup/image2.png
    :width: 5.90069in
    :height: 1.60483in

- Make FLEXPART work for 137 model levels

    In **par_mod.f90** line 125 has to be modified:

    .. image:: /_static/ug/flexpart_setup/image3.png
    :width: 5.90069in
    :height: 0.70953in

FLEXPART paths
==============

The location of the FLEXPART executable and that of some other
files/directories have to be specified for Metview. These locations can
be defined either through a set of Metview environment variables or via
parameters in :func:`flexpart_run` (these latter take precedence). The table below summarises what actually
is needed to be set for Metview.


.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1
   
   * - Description
     - How to get it/them
     - Metview environment
     - :func:`flexpart_run()` parameter
   * - The FLEXPART executable
     - Need to be built from FLEXPART source 
     - MV_FLEXPART_EXE
     - ``user_exe_path``
   * - The directory containing the following files: *IGBP_int1.dat*, *OH_7lev_agl.dat*, *surfdata.t*, *surfdepo.t*
     - These files are distributed in the FLEXPART source inside folder **option**
     - MV_FLEXPART_RESOURCES
     - ``user_resources_path``
   * - The directory containing the species:
     - A set of species are distributed in the FLEXPART source inside folder **option/SPECIES**
     - MV_FLEXPART_SPECIES
     - ``user_species_path``

To see the actual values of the Metview environment variables run
metview with the -h flag::

    metview -h                                                         

This will dump all the Metview environment variable to the stdout.
