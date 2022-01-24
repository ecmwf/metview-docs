.. _using_the_mars_web_api_from_metview:

Using the MARS Web API from Metview
///////////////////////////////////

Introduction
============

The Web API provides a way to access ECMWF's data archives in batch from
outside ECMWF (**users working at ECMWF or through ecgate should use
their normal local MARS access**). There are two services at present:

-  Access to the ECMWF Public Datasets requires self-registration and
   allows access to the datasets described
   `here <http://apps.ecmwf.int/datasets/>`__

-  Access to the MARS archive is only available to registered users

See `ECMWF Web API
Home <https://confluence.ecmwf.int/display/WEBAPI/ECMWF+Web+API+Home>`__
for more information, including how to set up the service by installing
an ECMWF key. Metview versions from 4.4.3 onwards have support for this
service (but version 4.4.7 is recommended). See the
`Releases <https://confluence.ecmwf.int/display/METV/Releases>`__ page
for download.

Setup
=====

First, whichever service you want, ensure that you have access to it by
following the steps in `Access ECMWF Public
Datasets <https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets>`__.
Ensure that you have set up your ~/.ecmwfapirc key and that you are
registered for the datasets you wish to access. If you can retrieve some
data using a sample script provided there, then you are 90% of the way
to accessing the service from within Metview. It is not required to
install the Python client libraries, but it can help with testing the
service before trying it with Metview.

Second, ensure that your Metview installation was built with Mars Web
Access enabled. When configuring with CMake (Metview version 4.5.x),
Mars Web Access will be automatically enabled if the curl development
library is found on the system.

Using
=====

Data can be retrieved using the *Mars Retrieval* icon or its Macro
language equivalent, the retrieve() function. Either start with a
`supplied example icon <#scroll-bookmark-5>`__, or `create a new
instance <#example-retrievals>`__, either from the icon drawers at the
bottom of the Metview desktop, or from the **New Icon** context menu.
Edit the icon by selecting **Edit** from its context menu (or
double-click the icon).

The important parameter to set in order to use the public datasets is
the **Dataset** parameter. Otherwise, the retrieval should be as
described in the Web API guide.

To perform the retrieval, use the context menu of the icon: **Execute**
will retrieve and cache the data; **Visualise**, **Examine** and
**Save** will do the same, but will then perform more actions on the
data. Please see the introductory
Metview `Tutorials <https://confluence.ecmwf.int/display/METV/Tutorials>`__
for more information on how to use these features of Metview.

Example retrievals
==================

It is beyond the scope of the Metview documentation to give detailed
assistance on formulating MARS requests. Please see the MARS Web API
page: `Brief request
syntax <https://confluence.ecmwf.int/display/WEBAPI/Brief+request+syntax>`__.
However, here are some examples to help get things started.

Users who have started Metview for the first time with version 4.4.x
onwards should already have some example icons and a macro in their
*Getting Started* folder. The icons are also available for `separate
download <https://confluence.ecmwf.int/download/attachments/32704008/example-metview-mars-web-api-icons.tar.gz?api=v2&modificationDate=1466083351641&version=2>`__
- untar these into a Metview folder to start exploring them.

Example retrieval for TIGGE data (icon parameters)
--------------------------------------------------

The following is the text behind an example *Mars Retrieval* icon for
requesting TIGGE data (in this case, surface pressure - param 134).
Either copy the values shown into the appropriate places in the icon
editor, or switch the icon editor to Text View mode and copy the request
in its entirety.

.. code-block:: python

   RETRIEVE,
      DATASET    = tigge,
      CLASS      = ti,
      EXPVER     = PROD,
      TYPE       = CF,
      LEVTYPE    = SFC,
      PARAM      = 134,
      DATE       = 2016-06-12,
      TIME       = '00:00:00',
      STEP       = 12/18,
      ORIGIN     = rjtd,
      GRID       = 0.5/0.5

Example retrieval for core archive data (icon parameters)
---------------------------------------------------------

.. code-block:: python

   RETRIEVE,
      PARAM      = T,
      DATE       = -2,
      GRID       = 1/1

Example retrieval for ERA Interim data (Macro language code)
------------------------------------------------------------

The following Macro code retrieves some ERA Interim data and plots it.

.. code-block:: python

   # Metview Macro
   
   #  **************************** LICENSE START ***********************************
   #
   #  Copyright 2016 ECMWF. This software is distributed under the terms
   #  of the Apache License version 2.0. In applying this license, ECMWF does not
   #  waive the privileges and immunities granted to it by virtue of its status as
   #  an Intergovernmental Organization or submit itself to any jurisdiction.
   #
   #  ***************************** LICENSE END ************************************
   
   era_data = retrieve
   (
      dataset  : "interim",
      stream   : "oper",
      type     : "fc",
      class    : "ei",
      levtype  : "sfc",
      param    : "235.128",
      date     : 2013-05-01,
      step     : 12,
      time     : 12
   )
   
   plot(era_data)   
   

Creating a Mars Retrieval icon
==============================

The following steps show how to use Metview's :ref:`user
interface <mv_desktop_overview>`
to create and edit a new Mars Retrieval icon.

1. Right-click / Create new Icon 
   
.. image:: /_static/ug/using_the_mars_web_api_from_metview/image1.png
   :width: 2.64546in
   :height: 2.84222in

2. Select Mars Retrieval

.. image:: /_static/ug/using_the_mars_web_api_from_metview/image2.png
   :width: 2.8928in
   :height: 5.5476in

3. The new icon appears on the Metview desktop 

.. image:: /_static/ug/using_the_mars_web_api_from_metview/image3.png
   :width: 2.89444in
   :height: 1.99579in

4. Edit the icon to set the retrieval parameters

.. image:: /_static/ug/using_the_mars_web_api_from_metview/image4.png
   :width: 2.89444in
   :height: 2.85276in

