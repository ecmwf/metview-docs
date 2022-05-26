.. _flextra_at_ecmwf:

FLEXTRA at ECMWF
////////////////

The FLEXTRA environment
=======================

At ECMWF version 5.0 of FLEXTRA is *centrally installed* on ecgate, ATOS and on
some internal Linux-based systems. On these systems (with the exception of ATOS) Metview is
configured to pick up the FLEXTRA executable location automatically via this preset
environment variable::

   MV_FLEXTRA_EXE

On the ATOS supercomputer you need to set this variable manually for your Metview session.    

Hard-coded parameters
=====================

Some of the important FLEXTRA parameters cannot be specified at run time
but are hard-coded in the source. The FLEXTRA installation at ECMWF uses
the following set of hard-coded parameters:

.. list-table:: 
   :widths: 40 10 30 20
   :header-rows: 1
   
   * - Description
     - Value
     - Parameter in source
     - Source file
   * - Maximum number of grid points in E-W (input grid)
     - 512
     - nxmax 
     - includepar
   * - Maximum number of grid points in N-S (input grid)
     - 361
     - nymax 
     - includepar
   * - Maximum dimension of (u,v) wind fields in z direction (input grid) 
     - 138
     - nuwzmax 
     - includepar
   * - Maximum dimension of (w) wind fields in z direction (input grid) 
     - 138
     - nwzmax 
     - includepar


Compilation
===========

compiler: gfortran
compilation options::

    -march=native -O3

Necessary code modifications
============================

To make FLEXTRA work with ECMWF data in the desired way the following
modifications were made in the source code:

Make FLEXTRA work for 137 model levels
--------------------------------------

In **includepar** modify line 38:

.. image:: /_static/ug/flextra_at_ecmwf/image1.png
   :width: 5.90069in
   :height: 0.87738in

and also modify line 83 in **gridcheck.f**.

.. image:: /_static/ug/flextra_at_ecmwf/image2.png
   :width: 5.90069in
   :height: 0.776in

Increase file name buffer length
--------------------------------

In **includecom** modify line 264:

.. image:: /_static/ug/flextra_at_ecmwf/image3.png
   :width: 5.90069in
   :height: 0.71723in

Fix bug when a limited area domain is incorrectly detected as global
--------------------------------------------------------------------

In **gridcheck.f** add this code to line 276:

.. image:: /_static/ug/flextra_at_ecmwf/image4.png
   :width: 5.90069in
   :height: 1.55768in
