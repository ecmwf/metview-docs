.. _3d_visualisation_with_vapor:

Overview of the VAPOR interface
/////////////////////////////////


What is VAPOR?
==============

VAPOR stands for **V**\ isualization and **A**\ nalysis **P**\ latform
for **O**\ cean, Atmosphere, and Solar **R**\ esearchers. It is a
software system providing an interactive 3D visualization environment
that runs on most UNIX, Windows and Mac systems equipped with modern 3D
graphics cards.

The home of the software is https://www.vapor.ucar.edu.

What VAPOR Version is required?
===============================

Version **2** (2.2.2 and later) is supported.

.. warning::

   VAPOR version **3** is not supported in Metview.


How to use VAPOR with Metview?
==============================

VAPOR has its *own internal data model* and NWP data has to be converted
into the VAPOR format.  There are a set of VAPOR command line tools that
can convert NetCDF input data into this format but there is no such tool
available for GRIB.

Metview's :ref:`VAPOR
Prepare <vapor_prepare_icon>`
icon helps to overcome this difficulty and allows converting GRIB data
into the VAPOR format.

.. image:: /_static/ug/3d_visualisation_with_vapor/image1.png
   :width: 0.68825in
   :height: 0.67371in

Once the conversion has been completed the :ref:`VAPOR
Prepare <vapor_prepare_icon>`
icon can be used to start up VAPOR to provide interactive 3D
visualisation for the data. The snapshots below show how ECMWF data is
actually displayed in VAPOR.

.. image:: /_static/ug/3d_visualisation_with_vapor/image2.png
   :width: 3.125in
   :height: 2.25858in

.. image:: /_static/ug/3d_visualisation_with_vapor/image3.png
   :width: 3.95833in
   :height: 2.23731in


Further details
===============

There is a
:ref:`tutorial <vapor_tutorial>`
available on the use of VAPOR with Metview. It explains both the data
preparation steps and the basics of the visualisation.

.. note::
  
    Details about setting up the Metview VAPOR interface *outside      
    ECMWF* can be accessed :ref:`here <vapor_setup>`.  
