.. _flexpart_species:

FLEXPART species
////////////////

The species (chemical elements) released during a simulation are
specified as integer numbers in the **Release Species** parameter in
:ref:`FLEXPART
Run <flexpart_run_icon>`. The
integer ID of the individual species are taken from the name of the
species definition files.These have to be located in the directory
defined

-  via the **User Species Path** parameter in :ref:`FLEXPART
   Run <flexpart_run_icon>`

-  or if it is left **blank** (this is the default value) Metview will
   use the **MV_FLEXPART_SPECIES** environment variable.

The species distributed with FLEXPART
=====================================

Folder **option/SPECIES** in the FLEXPART distribution contains a
default set of species definitions. Here each species is represented by
a file called SPECIES\_\ *NNN* , where NNN is the integer ID of the
given species.The table below summarises what species are available:

+----------+----------+---+----------+----------+---+-----------+------------+
| File     | Des      |   | File     | Des      |   | File      | D          |
|          | cription |   |          | cription |   |           | escription |
+==========+==========+===+==========+==========+===+===========+============+
| SPE      | TRACER   |   | SPE      | NH3      |   | SP        | Xe-133     |
| CIES_001 |          |   | CIES_011 |          |   | ECIES_021 |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | O3       |   | SPE      | SO4-areo |   | SPE       | CO         |
| CIES_002 |          |   | CIES_012 |          |   | CIES_022: |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | NO       |   | SPE      | SO4-areo |   | SP        | AIRTRACER  |
| CIES_003 |          |   | CIES_013 |          |   | ECIES_024 |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | NO2      |   | SPE      | I2-13    |   | SP        | A          |
| CIES_004 |          |   | CIES_014 |          |   | ECIES_025 | ERO-TRACER |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | HNO3     |   | SPE      | I-131    |   |           |            |
| CIES_005 |          |   | CIES_015 |          |   |           |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | HNO2     |   | SPE      | Cs-137   |   |           |            |
| CIES_006 |          |   | CIES_016 |          |   |           |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | H2O2     |   | SPE      | Y-91     |   |           |            |
| CIES_007 |          |   | CIES_017 |          |   |           |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | SO2      |   | SPE      | Ru-106   |   |           |            |
| CIES_008 |          |   | CIES_018 |          |   |           |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | HCHO     |   | SPE      | Kr-85    |   |           |            |
| CIES_009 |          |   | CIES_019 |          |   |           |            |
+----------+----------+---+----------+----------+---+-----------+------------+
| SPE      | PAN      |   | SPE      | Sr-90    |   |           |            |
| CIES_010 |          |   | CIES_020 |          |   |           |            |
+----------+----------+---+----------+----------+---+-----------+------------+

At ECMWF 
=========

The species are located in the directory specified by environment
variable **MV_FLEXPART_SPECIES**. The contents of this directory is the
same as that of folder **option/SPECIES** in the FLEXPART distribution.

At other sites
==============

Instructions to setup the species path can be found
:ref:`here <flexpart_setup>`.

Using your own definitions
==========================

If you want create your own species definition you need make a copy of
this directory and add your own species to it. Then set the path in
**User Species Path** so that FLEXPART could pick up your definitions.
