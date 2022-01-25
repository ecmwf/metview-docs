.. _the_flexpart_interface:

Overview of the FLEXPART interface
//////////////////////////////////////

What is FLEXPART?
=================

FLEXPART is a Lagrangian particle dispersion model developed and used by
a scientific community. It can be driven by meteorological input data
from a variety of global and regional models including ECMWF analyses
and forecasts.

The home of the software is https://www.flexpart.eu/.

What Metview version do I need for FLEXPART?
============================================

.. note::

    The minimum Metview version to use is **5.0.**                     

How to use FLEXPART with Metview?
=================================

Metview provides a high level interface to **prepare** input data for
FLEXPART from ECMWF's MARS archive (via the :ref:`FLEXPART
Prepare <flexpart_prepare_icon>`
icon),

.. image:: /_static/ug/the_flexpart_interface/image1.png
   :width: 0.54167in
   :height: 0.54167in

perform a FLEXPART **simulation** (via the :ref:`FLEXPART
Run <flexpart_run_icon>` icon)

.. image:: /_static/ug/the_flexpart_interface/image2.png
   :width: 0.54167in
   :height: 0.51042in

and visualise the resulting output files. For the **visualisation** the
gridded outputs in FLEXPART's custom binary format are **converted** to
GRIB (click
:ref:`here <flexpart_output>` for
details).

Tutorial
--------

There is
a :ref:`tutorial <using_flexpart_with_metview>`
available on the use of FLEXPART with Metview explaining both the basics
of the FLEXPART simulations and the related visualisation techniques.
The snapshots below showcase a few of the FLEXPART plot types that can
be generated with Metview:

.. image:: /_static/ug/the_flexpart_interface/image3.png
   :width: 220px

.. image:: /_static/ug/the_flexpart_interface/image4.png
   :width: 220px

.. image:: /_static/ug/the_flexpart_interface/image5.png
   :width: 220px

.. image:: /_static/ug/the_flexpart_interface/image6.png
   :width: 4.16667in
   :height: 3.04829in

.. image:: /_static/ug/the_flexpart_interface/image7.png
   :width: 4.16667in
   :height: 2.9313in


What FLEXPART version is supported in Metview?
==============================================

.. note::

    Please note that the Metview interface was written for **version   
    9.02 of FLEXPART**.                                                

FLEXPART at ECMWF
=================

FLEXPART is installed *at ECMWF* to be directly used from within
Metview. You can find out more about it
:ref:`here <flexpart_at_ecmwf>`.

FLEXPART outside ECMWF
======================

Details about setting up the Metview FLEXPART interface *outside ECMWF*
can be accessed
:ref:`here <flexpart_setup>`.

.. |\_scroll_external/attachments/image2017-10-31_14-1-40-13629f06620a01d9f0de0f73d570db666830f08b513411e363586b52ec8f72b5.pn.. image:: /_static/ug/the_flexpart_interface/image3.png
   :width: 3.25423in
   :height: 2.60417in
.. |\_scroll_external/attachments/image2017-10-31_14-2-10-cf1ac92a6c6ad064f99c52a18f2c5e1d7734508fa2e0ad4bd9ed596a2fe08699.pn.. image:: /_static/ug/the_flexpart_interface/image4.png
   :width: 3.28196in
   :height: 2.60417in
.. |\_scroll_external/attachments/image2017-10-31_14-2-43-fc3e4a2859b9b34a0c4425f8b77ec9128f632072b0dc7f2b5f484ea9c58e6cf0.pn.. image:: /_static/ug/the_flexpart_interface/image5.png
   :width: 3.27634in
   :height: 2.60417in
.. |\_scroll_external/attachments/image2017-11-9_10-59-5-790bc3730849a451e01296eab3dea964b53f3e020846f3bcfb5ce377f7ebd98a.pn.. image:: /_static/ug/the_flexpart_interface/image6.png
   :width: 4.16667in
   :height: 3.04829in
.. |\_scroll_external/attachments/image2017-10-31_15-6-34-593e313688f7333707edaee95a50833f6ee5d5b3c51be838cbb6e1692c3be12b.pn.. image:: /_static/ug/the_flexpart_interface/image7.png
   :width: 4.16667in
   :height: 2.9313in
