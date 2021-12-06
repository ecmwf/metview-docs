.. _part_5_netcdf:

Part 5 - NetCDF
###############

Full documentation on NetCDF functionality in Metview is `here <https://confluence.ecmwf.int/display/METV/NetCDF+Overview>`_.

Setup
*****

Navigate into the *4_netcdf* folder within Metview where you will find some data files and other icons.

Examine and visualise a geomatrix style netCDF file
***************************************************

Right-click on the file *era5_2000_aug.nc* and choose **examine** to see the structure of the file:

.. image:: ../_static/metview_90_minute_introduction_part_5_netcdf/netcdf-examiner-3.png

For more complete information, click on the **NcDump** tab.

You will need to tell Metview how to visualise this data, as there are multiple variables. 
Create a new `NetCDF Visualiser <https://confluence.ecmwf.int/display/METV/NetCDF+Visualiser>`_ icon, edit it and set the following parameters:

.. list-table::

  * - **Parameter**
    - **Value**

  * - **Netcdf Data**
    - Drop the *era5_2000_aug.nc* icon into this box

  * - **Netcdf Plot Type**
    - Geomatrix

  * - **Netcdf Latitude Variable**
    - latitude

  * - **Netcdf Longitude Variable**
    - longitude

  * - **Netcdf Value Variable**
    - t2m

Save the icon and visualise it. For fun, drop the supplied icons `contour_t2m <https://confluence.ecmwf.int/display/METV/Contouring>`_ and `mollweide <https://confluence.ecmwf.int/display/METV/Geographical+View>`_ into the plot window to obtain the following:

.. image:: ../_static/metview_90_minute_introduction_part_5_netcdf/netcdf-plotted-1.png

Examine and visualise a geopoints style netCDF file
***************************************************

Examine the file *madis-maritime.nc*. 
We will plot the **temperature variable**. 
As you can see, there are 1-dimensional variables for **temperature**, **latitude**, and **longitude**. Create a copy of your previous NetCDF Visualiser icon and edit it as follows:

.. list-table::

  * - **Parameter**
    - **Value**

  * - **Netcdf Data**
    - Right-click/remove the existing netCDF file from there, then drop *madis-maritime.nc* into this box

  * - **Netcdf Plot Type**
    - Geo Points

  * - **Netcdf Latitude Variable**
    - latitude

  * - **Netcdf Longitude Variable**
    - longitude

  * - **Netcdf Value Variable**
    - temperature

Visualise it to get a default plot. 
In the solutions folder is a script called *gallery_example_nc_maritime_obs.py*, which converts from Kelvin to Celcius and adds some stying to the plot (generated as PDF - simply remove the ``mv.setoutput()`` command to get an on-screen visualisation).

.. image:: ../_static/metview_90_minute_introduction_part_5_netcdf/netcdf-plotted-2.png

Extract data and convert to pandas
**********************************

Have a look in the solutions folder and edit and run the script *netcdf_to_pandas.py*. 
This shows how to extract some metadata from the previous netCDF file, and also some value arrays and convert into a pandas dataframe. 
The code is also here:

.. code-block::

  import metview as mv
  import pandas as pd
 
  nc = mv.read("madis-maritime.nc")
 
  # print some global fields
  print('Variables: \n', nc.variables())
  print('Global attributes: \n', nc.global_attributes())
 
  # extract certain variables - setcurrent() followed by values()
  nc.setcurrent('latitude')
  lats = nc.values()
  nc.setcurrent('longitude')
  lons = nc.values()
  nc.setcurrent('temperature')
  temps = nc.values()
  print('temperature attributes: \n', nc.attributes())
 
  # create a dictionary in order to convert to pandas
  pddict = {'latitude'    : lats,
            'longitude'   : lons,
            'temperature' : temps}
 
  df = pd.DataFrame(pddict)
  print('Dataframe: \n', df)
  print('temperature describe: \n', df.temperature.describe())
