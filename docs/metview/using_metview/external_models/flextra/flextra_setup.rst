.. _flextra_setup:

FLEXTRA setup
/////////////

What Metview version is required?
=================================

Metview versions **5.0.0**. or later are required.

What FLEXTRA version is required?
=================================

Only version **5.0** is supported.

.. note::

    Please note that FLEXTRA is not an ECMWF development. FLEXTRA is   
    *not distributed* with Metview, but it has to be installed         
    separately. Please visit the following website for installation    
    instructions: https://www.flexpart.eu.                             

How to specify the FLEXTRA executable in Metview?
=================================================

In Metview we can run FLEXTRA using :func:`flextra_run`. The
FLEXTRA executable is either defined via the ``flextra_exe_path``
parameter in this function or via the  **MV_FLEXTRA_EXE** environment
variable (this has to be set before starting up Metview).

Code modifications
==================

To make FLEXTRA work with ECMWF data the following modifications has to
be made in the source code:

Make FLEXTRA work for 137 model levels
--------------------------------------

In **includepar** modify line 38:

.. image:: /_static/ug/flextra_setup/image1.png
   :width: 5.90069in
   :height: 0.87738in

and also modify line 83 in **gridcheck.f**.

.. image:: /_static/ug/flextra_setup/image2.png
   :width: 5.90069in
   :height: 0.776in

Increase file name buffer length
--------------------------------

In **includecom** modify line 264:

.. image:: /_static/ug/flextra_setup/image3.png
   :width: 5.90069in
   :height: 0.71723in

Fix bug when a limited area domain is incorrectly detected as global
--------------------------------------------------------------------

In **gridcheck.f** add this code to line 276:

.. image:: /_static/ug/flextra_setup/image4.png
   :width: 5.90069in
   :height: 1.55768in
