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
parameters in the :ref:`FLEXPART
Run <flexpart_run_icon>` icon
(these latter take precedence). The table below summarises what actually
is needed to set for Metview.

+---------------------+------------+----------------------------+----------------+
| Description         | How to get | Metview environment        | Flexpart Run   |
|                     | it/them    | variable                   | parameter file |
+=====================+============+============================+================+
| The FLEXPART        | Need to be | MV_FLEXPART_EXE_PATH       | User           |
| executable          | built from |                            | Exe            |
|                     | FLEXPART   |                            | Path           |
|                     | source     |                            |                |
+---------------------+------------+----------------------------+----------------+
| The directory       | These      | MV_FLEXPART_RESOURCES_PATH | User Resources |
| containing the      | files are  |                            | Path           |
| following files:    | d          |                            |                |
|                     | istributed |                            |                |
| - IGBP_int1.dat     | in the     |                            |                |
|                     | FLEXPART   |                            |                |
|                     | source     |                            |                |
| - OH_7lev_agl.dat   | inside     |                            |                |
|                     | folder     |                            |                |
|                     | **option** |                            |                |
| - surfdata.t        |            |                            |                |
|                     |            |                            |                |
| - surfdepo.t        |            |                            |                |
+---------------------+------------+----------------------------+----------------+
| The directory       | A set of   | MV_FLEXPART_SPECIES_PATH   | User Species   |
| containing the      | species    |                            | Path           |
| species             | are        |                            |                |
|                     | d          |                            |                |
|                     | istributed |                            |                |
|                     | in the     |                            |                |
|                     | FLEXPART   |                            |                |
|                     | source     |                            |                |
|                     | inside     |                            |                | 
|                     | folder     |                            |                |
|                     | **option   |                            |                |
|                     | /SPECIES** |                            |                |
+---------------------+------------+----------------------------+----------------+

To see the actual values of the Metview environment variables run
metview with the -h flag::

    metview -h                                                         

This will dump all the Metview environment variable to the stdout.
