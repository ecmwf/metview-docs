.. _flexpart_at_ecmwf:

FLEXPART at ECMWF
/////////////////


The FLEXPART environment
========================

At ECMWF version 902 of FLEXPART is *centrally installed* on ecgate and
on some internal Linux-based systems. On these systems Metview is
configured to pick up the FLEXPART location automatically via these
environment variables:

-  **MV_FLEXPART_EXE_PATH**: defines the FLEXPART executable

-  **MV_FLEXPART_RESOURCES_PATH**: specifies the directory containing
   the following files **IGBP_int1.dat**, **OH_7lev_agl.dat**,
   **surfdata.t** and **surfdepo.t**

-  **MV_FLEXPART_SPECIES_PATH**: specifies the directory containing
   the species

Hard-coded parameters
=====================

Some of the important FLEXPART parameters cannot be specified at run
time but are hard-coded in the source. The FLEXPART installation at
ECMWF uses the following set of hard-coded parameters:

+-----------------------------+-------+-------+------------+----------+
| Description                 | Value |       | Parameter  | Source   |
|                             |       |       | in source  | file     |
+=============================+=======+=======+============+==========+
|                             | e     | linux |            |          |
|                             | cgate | de    |            |          |
|                             |       | sktop |            |          |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of grid      | 721   | 721   | nxmax      | par      |
| points in E-W (input grid)  |       |       |            | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of grid      | 361   | 361   | nymax      | par      |
| points in N-S (input grid)  |       |       |            | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of model     | 138   | 138   |            | par      |
| levels (input grid)         |       |       |            | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of species   | 6     | 6     | maxspec    | par      |
|                             |       |       |            | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of particles | 20    | 20    | maxpart    | par      |
|                             | 00000 | 00000 |            | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of age       | 10    | 10    | m          | par      |
| classes                     |       |       | axageclass | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of receptor  | 200   | 200   | ma         | par      |
| sites                       |       |       | xreceptors | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+
| Maximum number of output    | 0     | 0     | maxnests   | par      |
| grid nests                  |       |       |            | _mod.f90 |
+-----------------------------+-------+-------+------------+----------+

Compilation
===========

compiler: gfortran
compilation options::

    -O3 -m64 -mcmodel=medium -fconvert=little-endian -frecord-marker=4 

Necessary code modifications
============================

To make FLEXPART work at ECMWF the following modifications had to be
made in the source code:

1. Resolve type mismatch in err.f90 with newer gfortran compiler: see flextra ticket49
--------------------------------------------------------------------------------------

This involved the modification in **err.f90** of line 106 and 111

.. image:: /_static/ug/flexpart_at_ecmwf/image1.png
   :width: 5.90069in
   :height: 1.49569in

and line 140 and 145 as well.

.. image:: /_static/ug/flexpart_at_ecmwf/image2.png
   :width: 5.90069in
   :height: 1.60483in

2. Make FLEXPART work for 137 model levels
------------------------------------------

In **par_mod.f90** line 125 had to be modified:

.. image:: /_static/ug/flexpart_at_ecmwf/image3.png
   :width: 5.90069in
   :height: 0.70953in

Additional code modifications
=============================

We changed the code to increase the maximum value of some parameters.

1. Increase maximum number of age classes
-----------------------------------------

In **par_mod.f90**:

.. image:: /_static/ug/flexpart_at_ecmwf/image4.png
   :width: 5.90069in
   :height: 0.48666in

2. Increase maximum number of species
-------------------------------------

In **par_mod.f90**:

.. image:: /_static/ug/flexpart_at_ecmwf/image5.png
   :width: 5.26042in
   :height: 0.59375in
