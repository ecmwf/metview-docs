.. _flextra_at_ecmwf:

FLEXTRA at ECMWF
////////////////

The FLEXTRA environment
=======================

At ECMWF version 5.0 of FLEXTRA is *centrally installed* on ecgb and on
some internal Linux-based systems. On these systems Metview is
configured to pick up the FLEXTRA executable location automatically via this preset
environment variable::

   MV_FLEXTRA_EXE_PATH

Hard-coded parameters
=====================

Some of the important FLEXTRA parameters cannot be specified at run time
but are hard-coded in the source. The FLEXTRA installation at ECMWF uses
the following set of hard-coded parameters:

+------------------------------------+-------+--------------+----------+
| Description                        | Value | Parameter in | Source   |
|                                    |       | source       | file     |
+====================================+=======+==============+==========+
| Maximum number of grid points in   | 721   | nxmax        | par      |
| E-W (input grid)                   |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of grid points in   | 361   | nymax        | par      |
| N-S (input grid)                   |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of model levels     | 138   |              | par      |
| (input grid)                       |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of species          | 6     | maxspec      | par      |
|                                    |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of particles        | 20    | maxpart      | par      |
|                                    | 00000 |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of age classes      | 10    | maxageclass  | par      |
|                                    |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of receptor sites   | 200   | maxreceptors | par      |
|                                    |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+
| Maximum number of output grid      | 0     | maxnests     | par      |
| nests                              |       |              | _mod.f90 |
+------------------------------------+-------+--------------+----------+

Compilation
===========

compiler: gfortran
compilation options::

    -O3 -m64 -mcmodel=medium -fconvert=little-endian -frecord-marker=4 

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