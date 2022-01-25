.. _vapor_tutorial:

VAPOR Tutorial
##############
 
This tutorial explains how to convert ECMWF GRIB data into VAPOR format and how to :ref:`visualise <vapor_tutorial_visualisation>` the resulting data in VAPOR.

.. note::

  Please note that this tutorial requires Metview version **4.4.6** or later. 
  Also for users outside ECMWF the Metview VAPOR interface should be properly set up as described `here <https://confluence.ecmwf.int/display/METV/VAPOR+Setup>`_.

Preparations
************

First start Metview; at ECMWF, the command to use is metview (see `Metview at ECMWF <https://confluence.ecmwf.int/display/METV/Metview+at+ECMWF>`_ for details of Metview versions). 
You should see the main Metview desktop popping up.

You will create some icons yourself, but some are supplied for you - please download the following file: 

.. list-table:: 
  
  * - `vapor_tutorial.tar.gz <https://confluence.ecmwf.int/download/attachments/29328811/vapor_tutorial.tar.gz?api=v2&modificationDate=1390381084784&version=1>`_

Alternatively, if at ECMWF then you can copy it like this from the command line::
  
    cp /home/graphics/cgx/tutorials/vapor_tutorial.tar.gz $HOME/metview
    
and save it in your ``$HOME/metview`` directory. You should see it appear on your main Metview desktop, from where you can right-click on it, then choose **execute** to extract the files. 
You should now (after a few seconds) see a *vapor_tutorial* folder which contains the solutions and also some additional icons required by these exercises. 
You will work in the *vapor_tutorial* folder so open it up. You should see the following contents:

.. image:: /_static/vapor_tutorial/image2014-1-22_9-9-14.png

VAPOR Basics
************

VAPOR stands for Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers. 
It is a software system providing an interactive 3D visualization environment. 
The home of the software is `https://www.vapor.ucar.edu <https://www.vapor.ucar.edu/>`_.

VAPOR input files
=================

VAPOR input data is described by **.vdf** (VAPOR Data Format) files. 
These are XML files containing the name and dimension of all the variables and the path of the actual data files storing the data values.  
VAPOR stores its data values in **.vdc** (VAPOR Data Collection) files. 
These are NetCDF files containing wavelet compressed 3D data. 
There is a separate file for each variable and timestep organized into a folder hierarchy.

There are a set of VAPOR command line tools that can convert NetCDF input data into this format but there is no such tool available for GRIB. 
This tutorial shows you how to use Metview's :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon to convert GRIB data into the VAPOR format.

VAPOR grids
===========

VAPOR input data must be defined on a 3D grid, which has to be regular horizontally (on a map projection).

It is crucially important to understand the vertical coordinate types of the input data VAPOR can use. 
Here we discuss only the two types that the Metview VAPOR interface supports

* For **layered** grids VAPOR expects a parameter specifying the elevation of each 3D level in the input data. 
  This is typically the case for  pressure or model level (n levels) data with height or geopotential available (or it can be computed).
  
* For **regular** grids the 3D levels are supposed to be equidistant (in the user coordinate space). 
This type can be used when the data is available on equidistant height levels.

When pressure or model level data is present without height information the situation is somewhat special. 
The grid in this case is not **layered** but can be regarded as **regular** in its own coordinate space (pressure or model levels) letting the z axis simply represent pressure or model levels in the 3D scene rendered in VAPOR.

VAPOR uses a right-handed coordinate system which means that :

* the horizontal grid has to start at the SW corner
* the vertical coordinates have to increase along the z axis (upwards)

Supported GRIBs
===============

Only GRIB fields on a **regular lat-lon grid** are supported at the moment. 
However, please note that  GRIBs can be internally interpolated to a regular lat-lon grid by using the **VAPOR_AREA_SELECTION** parameter. 
The parameters to be converted are supposed to have the same validity date and time and the same vertical levels. They also have to be valid on the same grid.

Converting pressure level data with elevation
*********************************************

This exercise demonstrate how to use pressure level ECMWF GRIB data with VAPOR when elevation (as geopotential) is available. We will work with fields on a low resolution grid over Europe.

Getting the GRIB data
=====================

The GRIB data is already in its place. 
In your folder you will find the two GRIB files you need to use for this exercise:

* pl.grib: contains z, t, r, u and v on pressure levels
* pl_surf.grib: contains z, 2t ,10u and 10v on surface

Please note that both these files were retrieved from MARS by using the 'ret_pl' and 'ret_pl_surf' *MARS retrieval* icons in the *solutions* folder.

Running Vapor Prepare
=====================

Create a :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon (right-click in the desktop when no icons are selected and use the New icon ... menu).

.. image:: /_static/vapor_tutorial/doc1.png

Rename it 'vapor_pl' and open up its editor.

First, ensure that **Vapor Input Mode** is set to 'Icon' then drop the two *Mars Retrieval* icons into the **Vapor Input Data** field.

.. image:: /_static/vapor_tutorial/image2014-1-22_9-53-31.png

Then you need to define the list of GRIB parameters you want to see in VAPOR.

.. list-table::

  * - **Vapor 2d Params**
    - z/2t/10u/10v
    
  * - **Vapor 3d Params**
    - t/u/v/r

.. note::

  Internally :ref:`VAPOR Prepare <vapor_prepare_icon>` icon converts surface geopotential to metres and rename it **HGT**.

The vertical coordinate system has to be set carefully:

.. list-table::

  * - **Vapor Vertical Grid Type**
    - Layered
    
  * - **Vapor Elevation Param**
    - z
    
  * - **Vapor Bottom Coordinate**
    - 0
    
  * - **Vapor Top Coordinate**
    - 16000
    
Here you set the vertical grid type to 'Layered' and defined geopotential (z) as the parameter holding the elevation of the vertical layers (pressure levels). 
You also specified the vertical coordinate range (in metres) that VAPOR will display.

.. note::

  Internally :ref:`VAPOR Prepare <vapor_prepare_icon>` icon converts geopotential to metres and rename it ELEVATION (this is required by VAPOR).

The last step is to specify the name and location of the results of the conversion:

.. list-table::

  * - **Vapor Vdf Name**
    - tut_pl
  
  * - **Vapor Output Path**
    - *your_path_on_the_filesystem*
    
With these settings a **VDF file** called 'tut_pl.vdf' will be created in the directory you specified. 
All the other VAPOR data files will be placed into a subdirectory called 'tut_pl_data'.

.. note::

  This tutorial works only with a small amount of data. 
  However, real life examples can easily result in huge VAPOR files (gigabytes). 
  Therefore you should always **carefully select the output path** for the GRIB to VAPOR conversion.

Now save your :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon then right click Execute to run the conversion. 
The icon will first turn orange then green when the conversion finishes.

To visualise the VAPOR data generated please follow the instructions :ref:`here <vapor_tutorial_visualisation>`.

Converting model level data with elevation
******************************************

This exercise demonstrate how to use model level ECMWF GRIB data with VAPOR when elevation available/can be derived. We will work with fields on the same low resolution grid over Europe as we used for the pressure levels.

Getting the GRIB data
=====================

The GRIB data is already in its place. 
In your folder you will find the three GRIB files you need for this exercise:

* ml.grib: contains q, t, u and v on model levels 137-60

* ml_lnsp.grib: contains lnsp on the bottommost model level (level 137)

* ml_surf.grib: contains z, 2t ,10u and 10v on surface).

Please note that these files were retrieved from MARS by using the 'ret_ml', 'ret_ml_lnsp' and 'ret_ml_surf' *MARS retrieval* icons in the *solutions* folder.

.. note::

  Please note that upper level geopotential (z) is not available in the input files because it is not archived in MARS for model levels. However, :ref:`VAPOR Prepare <vapor_prepare_icon>` icon can derive it if tempreature (t), specific humidity (q) and logarithm of surface pressure (lnsp) are available (it is the case for our input data).

Running Vapor Prepare
=====================

Create a :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon. Rename it 'vapor_ml' and open up its editor.

First, ensure that **Vapor Input Mode** is set to Icon then drop your three Mars Retrieval icons into the **Vapor Input Data field**.

.. image:: /_static/vapor_tutorial/image2014-1-22_10-12-0.png

Then you need to define the list of GRIB parameters you want to see in VAPOR.

.. list-table::

  * - **Vapor 2d Params**
    - z/2t/10u/10v
    
  * - **Vapor 3d Params**
    - t/u/v/q
    
The vertical coordinate system has to be set carefully:

.. list-table::

  * - **Vapor Vertical Grid Type**
    - Layered
  
  * - **Vapor Elevation Param**
    - z
  
  * - **Vapor Bottom Coordinate**
    - 0
  
  * - **Vapor Top Coordinate**
    - 16000
  
Here you set the vertical grid type to layered and defined **geopotential** (z) as the parameter holding the elevation of the vertical layers (model levels). 
We also specified the vertical coordinate range (in metres) that VAPOR will display for this data.

.. note::

  Although geopotential (z) is not available on model levels in the input data :ref:`VAPOR Prepare <vapor_prepare_icon>` icon computes it automatically if tempreature (t), specific humidity (q) and logarithm of surface pressure (lnsp) are available. 
  Geopotential then gets converted into metres units and renamed to ELEVATION.

Last, we specify the name and location of the results of the conversion:

.. list-table::**

  * - **Vapor Vdf Name**
    - tut_ml
  
  * - **Vapor Output Path**
    - *your_path_on_the_filesystem*
    
Now save your :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon then right click Execute to run the conversion. The icon will first turn orange then green when the conversion finishes.

To visualise the VAPOR data generated please follow the instructions in the next chapter.

.. _vapor_prepare_visualisation:

Visualisation
*************

.. note::

  Giving detailed instructions about VAPOR visualisation goes beyond the scope of this tutorial. 
  Here you will learn only the basics about how to visualise 3D data with VAPOR. F
  or an in depth introduction please study the VAPOR tutorials at:
   
    `https://www.vapor.ucar.edu/docs/vapor-tutorials <https://www.vapor.ucar.edu/docs/vapor-tutorials>`_


Stating up VAPOR
================

Right click **Visualise** your :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon to start up VAPOR. 
You will see this window popping up:

.. image:: /_static/vapor_tutorial/image2014-1-10_11-33-41.png

Your **vdf file** (that you have created with your :ref:`VAPOR Prepare <vapor_prepare_icon>` icon icon) is now loaded into VAPOR and you can see a cube representing your 3D data volume.

Adjusting the view volume
=========================

If you rotate the cube in the display window (left mouse button) you will see it is flat. 
We need to scale the vertical axis to get a better view of the whole 3D volume. 
Go to the **Edit** -> **Edit Visualiser Features** menu and set the **Z Scene Stretch Factor** to 200:

.. image:: /_static/vapor_tutorial/image2014-1-10_11-39-35.png

.. image:: /_static/vapor_tutorial/image2014-1-10_11-45-48.png

Now the full 3D volume is visible:

.. image:: /_static/vapor_tutorial/image2014-1-10_11-52-1.png

Setting up the map image
========================

We can load a pre-installed map image to get a better geographical reference for the domain we are looking at. Open the **Image** tab and load 'BigBlueMarble.tiff' by using the **Select Installed Image** button. Then tick **Instance: 1**, tick **Apply to Terrain** and set **Z** to 0. The scene has now changed like this:

.. image:: /_static/vapor_tutorial/image2014-1-10_14-51-33.png

The VAPOR session file
======================

.. note::

The current scene settings can be saved into a **VAPOR session file** (with a **.vss** suffix) by using the **File**  -> **Save Session (As)** menu. 
Then next time we start up VAPOR the saved session files can be loaded to initialise the scene with the saved settings.

Direct volume rendering (DVR)
=============================

Having set up the view you can now visualise our data. 
Click on the **DVR** (Direct Volume Rendering) tab, select **Variable to relative** humidity (r), tick **Instance 1**. 
Then change the opacity in the **Transfer Function** editor like this (drag the control points of the white curve and use the vertical slide on the right of the histogram):

.. image:: /_static/vapor_tutorial/image2014-1-22_11-44-16.png

Having done so you should get this scene:

.. image:: /_static/vapor_tutorial/doc8.png

Please note that this scene was generated by using only low resolution data. 
The see more details change the **Refinement** level first to 1 then to 2.

.. image:: /_static/vapor_tutorial/image2014-1-22_11-49-6.png

You should see more details appear in the scene:

.. image:: /_static/vapor_tutorial/doc9.png

.. image:: /_static/vapor_tutorial/doc10.png

Further rendering types
=======================

There are other types of renderers which we just list here and present a small gallery made with the data used for this tutorial:

* wind barb plotting: see the **Barbs** tab
* 2D field plotting: see the **2D** tab
* cross sections: see the **Probe** tab
* flow visualisation (streamlines): see the **Flow** tab 
* iso surfaces: see the **Iso** tab

.. note::

  For further details please study the VAPOR tutorials at: 
  
    `https://www.vapor.ucar.edu/docs/vapor-tutorials <https://www.vapor.ucar.edu/docs/vapor-tutorials>`_

.. image:: /_static/vapor_tutorial/doc4.png

.. image:: /_static/vapor_tutorial/doc5.png

.. image:: /_static/vapor_tutorial/doc6.png

.. image:: /_static/vapor_tutorial/doc7.png
