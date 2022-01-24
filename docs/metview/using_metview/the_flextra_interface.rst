.. _the_flextra_interface:

The FLEXTRA interface
/////////////////////

What is FLEXTRA?
================

**FLEXTRA** is an atmospheric trajectory model used by a large user
community. It can be driven by meteorological input data from a variety
of global and regional models including ECMWF analyses and forecasts.
FLEXTRA can compute both **forward** and **backward** trajectories using
**various trajectory types** such as: three-dimensional, model level,
mixing layer, isobaric and isentropic trajectories.

.. note::

    FLEXTRA is a **free software** system released under the GNU       
    General Public License V3.0. The home of the software is           
    https://www.flexpart.eu.                                           

How to use FLEXTRA with Metview?
================================

Metview provides a high level interface to **prepare** input data for
FLEXTRA from ECMWF's MARS archive (via the :ref:`FLEXTRA
Prepare <flextra_prepare_icon>`
icon),

.. image:: /_static/ug/the_flextra_interface/image1.png
   :width: 0.5592in
   :height: 0.55792in

perform a FLEXTRA **simulation** (via the :ref:`FLEXTRA
Run <flextra_run_icon>` icon)

.. image:: /_static/ug/the_flextra_interface/image2.png
   :width: 0.58071in
   :height: 0.53686in

and visualise the resulting output files (using the :ref:`FLEXTRA Visualiser <flextra_visualiser_icon>`)

.. image:: /_static/ug/the_flextra_interface/image3.png
   :width: 0.5592in
   :height: 0.54739in

The snapshots below show some FLEXTRA plots generated with Metview:

.. image:: /_static/ug/the_flextra_interface/image4.png
   :width: 4.27441in
   :height: 2.60417in

.. image:: /_static/ug/the_flextra_interface/image5.png
   :width: 3.40187in
   :height: 2.60417in


.. note::

    There is a                                                         
    `tutorial <https://confluence.ecmwf.int/display/METV/FLEXTRA+tutorial>`__ 
    available on the use of FLEXTRA with Metview. It explains both the 
    data preparation steps and the basics of the visualisation.        

What FLEXTRA versions are supported?
====================================

Please note that the Metview interface was written for **version 5.0 of
FLEXTRA**.

FLEXTRA at ECMWF
================

FLEXTRA is installed *at ECMWF* to be directly used from within Metview.
You can find out more about it
`here <https://confluence.ecmwf.int/display/METV/FLEXTRA+at+ECMWF>`__.

FLEXTRA outside ECMWF
=====================

Details about setting up the Metview FLEXTRA interface *outside ECMWF*
can be accessed :ref:`here <flextra_setup>`.
