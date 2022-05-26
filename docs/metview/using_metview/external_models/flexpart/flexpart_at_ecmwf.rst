.. _flexpart_at_ecmwf:

FLEXPART at ECMWF
/////////////////


The FLEXPART environment
========================

At ECMWF version 902 of FLEXPART is *centrally installed* on ecgate, ATOS and
on some internal Linux-based systems. On these systems (with the exception of ATOS) Metview is
configured to pick up the FLEXPART location automatically via these
environment variables:

-  **MV_FLEXPART_EXE_PATH**: defines the FLEXPART executable

-  **MV_FLEXPART_RESOURCES_PATH**: specifies the directory containing
   the following files **IGBP_int1.dat**, **OH_7lev_agl.dat**,
   **surfdata.t** and **surfdepo.t**

-  **MV_FLEXPART_SPECIES_PATH**: specifies the directory containing
   the species

On the ATOS supercomputer you need to set these variables manually for your Metview session. 

Hard-coded parameters
=====================

Some of the important FLEXPART parameters cannot be specified at run
time but are hard-coded in the source. The FLEXPART installation at
ECMWF uses the following set of hard-coded parameters:



.. list-table:: 
   :widths: 40 10 30 20
   :header-rows: 1
   
   * - Description
     - Value
     - Parameter in source
     - Source file
   * - Maximum number of grid points in E-W (input grid)
     - 1441
     - nxmax 
     - par_mod.f90
   * - Maximum number of grid points in N-S (input grid)
     - 721
     - nymax 
     - par_mod.f90
   * - Maximum dimension of (u,v) wind fields in z direction (input grid) 
     - 138
     - nuwzmax
     - par_mod.f90
   * - Maximum dimension of (w) wind fields in z direction (input grid) 
     - 138
     - nwzmax
     - par_mod.f90
   * - Maximum dimension in z direction (input grid) 
     - 138
     - nzmax
     - par_mod.f90
   * - Maximum number of species
     - 6
     - maxspec
     - par_mod.f90
   * - Maximum number of particles
     - 2000000
     - maxpart
     - par_mod.f90
   * - Maximum number of age classes
     - 10
     - maxageclass
     - par_mod.f90
   * - Maximum number of receptor sites
     - 200
     - maxreceptors
     - par_mod.f90
   * - Maximum number of output grid nests
     - 0
     - maxnests
     - par_mod.f90

Compilation
===========

compiler: gfortran
compilation options::

    -O3 -m64 -mcmodel=medium -fconvert=little-endian -frecord-marker=4 

Necessary code modifications
============================

To make FLEXPART work at ECMWF the following modifications had to be
made in the source code:

- Resolve type mismatch in err.f90 with newer gfortran compiler: see flextra ticket49

   This involved the modification in **err.f90** of line 106 and 111

   .. image:: /_static/ug/flexpart_at_ecmwf/image1.png
      :width: 5.90069in
      :height: 1.49569in

   and line 140 and 145 as well.

   .. image:: /_static/ug/flexpart_at_ecmwf/image2.png
      :width: 5.90069in
      :height: 1.60483in

- Make FLEXPART work for 137 model levels

   In **par_mod.f90** line 125 had to be modified:

   .. image:: /_static/ug/flexpart_at_ecmwf/image3.png
      :width: 5.90069in
      :height: 0.70953in

Additional code modifications
=============================

We changed the code to increase the maximum value of some parameters.

- Increase maximum number of age classes

   In **par_mod.f90**:

   .. image:: /_static/ug/flexpart_at_ecmwf/image4.png
      :width: 5.90069in
      :height: 0.48666in

- Increase maximum number of species

   In **par_mod.f90**:

   .. image:: /_static/ug/flexpart_at_ecmwf/image5.png
      :width: 5.26042in
      :height: 0.59375in
