.. _flexpart_plume_trajectories:

FLEXPART - Plume trajectories
#############################
 
This tutorial demonstrates how to generate a single plume trajectory with FLEXPART and how to visualise the results in various ways.

Using FLEXPART with Metview
***************************

.. note::

  Please note that this tutorial requires Metview version **5.0** or later.
  
Preparations
************
  
First start Metview; at ECMWF, the command to use is metview (see `Metview at ECMWF <https://confluence.ecmwf.int/display/METV/Metview+at+ECMWF>`_ for details of Metview versions). 
You should see the main Metview desktop popping up.

The icons you will work with are already prepared for you - please download the following file:

**Download**

.. list-table::

  * - `flexpart_tutorial.tar.gz <http://download.ecmwf.org/test-data/metview/tutorial/flexpart_tutorial.tar.gz>`_

and save it in your ``$HOME/metview`` directory. 
You should see it appear on your main Metview desktop, from where you can right-click on it, then choose **execute** to extract the files.

Alternatively, if **at ECMWF** then you can copy it like this from the command line::

  cp -R /home/graphics/cgx/tutorials/flexpart_tutorial ~/metview
  
You should now (after a few seconds) see a *flexpart_tutorial* folder. 
Please open it up.

The input data
**************

The input data is already prepared for you and is located in folder 'Data'. 
You will find a :ref:`FLEXPART Prepare <flexpart_prepare_icon>` icon that was used to generate the data in folder 'Prepare'. 
The corresponding macro code can also be found there.

You do not need to run the data preparation. However, if you wish to do so please note that it requires MARS access and you must set the **Output Path** parameter accordingly.

.. note::

  Please enter folder 'plume_trajectory' to start working. In this example we will generate a forward trajectory by releasing atmospheric tracers from Newcastle.
  
The simulation itself is defined by the 'tr_run' :ref:`FLEXPART Run <flexpart_run_icon>` icon and the 'rel_ncastle' :ref:`FLEXPART Release <flexpart_release_icon>` icon, respectively. Both these are encompassed in a single macro called 'tr_run.mv'. For simplicity will use this macro to examine the settings in detail. 

The macro starts with defining the release like this:  

.. code-block:: python
  
  rel_ncastle = flexpart_release(
      name    :   "NEWCASTLE",
      starting_date   :   0,
      starting_time   :   15,
      ending_date :   0,
      ending_time :   18,
      level_units :   "agl",
      top_level   :   500,
      bottom_level    :   0,
      particle_count  :   10000,
      masses  :   1000,
      area    :   [54.96,-1.6,54.96,-1.6]
      )
  
This says that the release will happen over a 3 h period in the lower 500 m at Newcastle and we will release 1000 kg of material in total.

.. note::

  * the species is not defined here (will be defined in :func:`flexpart_run`)  
  * we used dates relative to the starting date of the simulation (see also in :func:`flexpart_run`).
  
The actual simulation is carried out by calling :func:`flexpart_run`:
  
.. code-block:: python
  
  #Run flexpart (asynchronous call!)
  r = flexpart_run(
      output_path         :   "result_tr",
    input_path          :   "../data",
      starting_date       :   20120517,
      starting_time       :   12,
      ending_date         :   20120519,
      ending_time         :   12,
      output_field_type   :   "none",
      output_trajectory   :   "on",
      output_area         :   [40,-25,66,10],
      output_grid         :   [0.25,0.25],
      output_levels       :   500,
      release_species     :   1,
      releases            :   rel_ncastle
   
  print(r)
  
Here we defined both the input and output paths and specified the simulation period and the output grid as well. 
We also told FLEXPART to only generate plume trajectories on output.

.. note::

  The actual species that will be released is defined as an integer number (for details about using the species see `here <https://confluence.ecmwf.int/display/METV/FLEXPART+species>`_). 
  With the default species settings number 1 stands for atmospheric  tracer.

If we run this macro (or alternatively right-click **execute** the :ref:`FLEXPART Run <flexpart_run_icon>` icon) the resulting CSV file, 'tr_r001.csv', will appear (after a minute or so) in folder 'result_tr'. 
For details about the FLEXPART trajectory outputs `click here. <https://confluence.ecmwf.int/display/METV/FLEXPART+output>`_

Step 1 - Plotting the mean track
********************************

The macro to plot the mean trajectories is 'plot_tr_step1.mv'. 
We will see how this macro works.First, we read the CSV file using a :ref:`Table Reader <read_table_icon>`:
  
.. code-block:: python
  
  #The input file
  dIn="result_tr"
  inFile=dIn  & "/tr_r001.csv"
   
  #Read table (CSV) data
  tbl=read_table(table_filename: inFile,
      table_header_row: "2",
      table_meta_data_rows: "1")
  
Next, we determine the trajectory (i.e. the release) start date and time from the table header (we will use them to construct the title):  
  
.. code-block:: python
  
  #Read runDate from table header
  runDate=date(metadata_value(tbl,"runDate"))
  runTime=number(metadata_value(tbl,"runTime"))
  runDate=runDate + hour(runTime/10000)
   
  #Read release start date from table header
  startSec=number(metadata_value(tbl,"start"))
  releaseDate=runDate + second(startSec)
  
Next, we read the coordinates of the mean track and use :ref:`Input Visualiser <input_visualiser_icon>` and :ref:`Graph Plotting <mgraph_icon>` to plot it:
  
.. code-block:: python
  
  #Read columns from table
  mLat=tolist(values(tbl,"meanLat"))
  mLon=tolist(values(tbl,"meanLon"))
   
  #visualiser
  iv_curve = input_visualiser(
         input_plot_type  :   "geo_points",
         input_longitude_variable :   mLon,
         input_latitude_variable  :   mLat          
      )
   
  #line attributes
  graph_curve=mgraph(graph_line_colour: "red",
           graph_line_thickness: "3",
           graph_symbol: "on",
           graph_symbol_marker_index: 15,
           graph_symbol_height: 0.5,
           graph_symbol_colour: "white",
           graph_symbol_outline: "on"
          ) 
  
Then we define the title:
  
.. code-block:: python
  
  txt="Mean trajectory starting at: " & 
               string(releaseDate,"yyyymmdd") & " " &
               string(releaseDate,"HH") & " UTC"
   
  title=mtext(text_line_1: txt,
              text_font_size: 0.4)
  
the mapview:
  
.. code-block:: python
  
  #Define coastlines
  coast_grey = mcoast(
      map_coastline_thickness :   2,
      map_coastline_land_shade    :   "on",
      map_coastline_land_shade_colour :   "grey",
      map_coastline_sea_shade :   "on",
      map_coastline_sea_shade_colour  :   "RGB(0.89,0.89,0.89)",
      map_boundaries  :   "on",
      map_boundaries_colour   :   "black",
      map_grid_latitude_increment :   5,
      map_grid_longitude_increment    :   5
      )
   
  #Define geo view
  view = geoview(
      map_area_definition :   "corners",
      area    :   [47,-16,57,0],
      coastlines: coast_grey
      )
  
and finally generate the plot:  
  
.. code-block:: python
  
  plot(view,iv_curve,graph_curve,title)
  
Having run the macro we will get a plot like this:

.. image:: /_static/flexpart_plume_trajectories/image2017-10-31_10-22-40.png

Step 2 - Plotting the dates along the mean track
************************************************

We will improve the trajectory plot by showing the waypoint dates along the track. 

The macro to use is 'plot_tr_step2.mv'. This macro is basically the same as the one in **Step 1**, but we have to modify and extend it a bit.

We start with loading the CSV file and determining the start date and time as before:  
  
.. code-block:: python
  
  #The input file
  dIn="result_tr"
  inFile=dIn  & "/tr_r001.csv"
   
  #Read table (CSV) data
  tbl=read_table(table_filename: inFile,
      table_header_row: "2",
      table_meta_data_rows: "1")
   
  #Read runDate from table header
  runDate=date(metadata_value(tbl,"runDate"))
  runTime=number(metadata_value(tbl,"runTime"))
  runDate=runDate + hour(runTime/10000)
  
Next we need to determine the middle of the release interval since the trajectory waypoint times are given in seconds elapsed since this date:
  
.. code-block:: python
  
  #Read release dates from table header
  startSec=number(metadata_value(tbl,"start"))
  endSec=number(metadata_value(tbl,"end"))
  releaseDate=runDate + second(startSec)
  releaseMidDate=runDate + second((endSec+startSec)/2)
  
The plotting of the track is the same as in **Step1**:  
  
.. code-block:: python
  
  #Read columns from table
  mLat=tolist(values(tbl,"meanLat"))
  mLon=tolist(values(tbl,"meanLon"))
   
  #visualiser
  iv_curve = input_visualiser(
         input_plot_type  :   "geo_points",
         input_longitude_variable :   mLon,
         input_latitude_variable  :   mLat          
      )
   
  #line attributes
  graph_curve=mgraph(graph_line_colour: "red",
           graph_line_thickness: "3",
           graph_symbol: "on",
           graph_symbol_marker_index: 15,
           graph_symbol_height: 0.5,
           graph_symbol_colour: "white",
           graph_symbol_outline: "on"
          ) 
  
Then we need to add a new plotting layer for the date labels. Here we use a loop to construct and plot the date labels one by one with :ref:`Input Visualiser  <input_visualiser_icon>` and :ref:`Symbol Plotting <msymb_icon>`:
  
.. code-block:: python
  
  #Read waypoint times from table
  #These are seconds elapsed since the middle of the release interval
  tt=values(tbl,"time")
   
  #Build and define the visualiser for the date strings
  #The plot definitions are collected into a list
  pltDateLst=nil
  for i=1 to count(tt) do
   
      d=releaseMidDate + second(tt[i])
      label="  " & string(d,"dd") & "/" & string(d,"HH")
      
      #visualiser
      iv_date = input_visualiser(
         input_plot_type  :   "geo_points",
         input_longitude_variable :   mLon[i],
         input_latitude_variable  :   mLat[i]           
      )
      
      #text attributes
      sym_date=msymb(symbol_type: "text",
           symbol_text_list: label,
           symbol_text_font_size: 0.3,
           symbol_text_font_colour: "navy"
          ) 
      
      #collect the plot definitions into a list  
      pltDateLst= pltDateLst & [iv_date,sym_date]          
   
  end for    
  
.. note::

  We had to define the plot for each date label individually (instead of defining just one plot object with a list of values), due to a current limitation for string plotting in Metview' plotting library. 
  Until this issue is resolved this is the recommended way to plot strings onto a map.

Finally we define the title and mapview in the same way as in **Step 1** and generate the plot:
  
.. code-block:: python
  
  plot(view,iv_curve,graph_curve,pltDateLst,title)
  
Having run the macro we will get a plot like this:

.. image:: /_static/flexpart_plume_trajectories/image2017-10-31_11-18-31.png

Step 3 - Plotting the cluster centres
*************************************

We will further improve the trajectory plot by indicating the particle distribution along the mean track. 

The macro to use is 'plot_tr_step3.mv' and is basically the same as the one in **Step 2** but contains an additional plot layer. 
In this plot layer we draw circles around the mean trajectory waypoints using the RMS (root mean square) of the horizontal distances of the particles to this waypoint. The code goes like this:  

.. code-block:: python
  
  #Get rms of the horizontal distances (in km) to the mean particle positions (i.e. waypoints)
  mRms=values(tbl,"rmsHBefore")
   
  #Draw an rms circle around every second waypoint
  iStart=1
  if mod(count(mRms),2)= 0 then
      iStart=2
  end if   
   
  pltRmsLst=nil
  for i=iStart to count(mRms) by 2 do
   
     if mRms[i] > 0 then
          
          #input visualiser defining the circle
          iv_rms=mvl_geocircle(mLat[i],mLon[i],mRms[i],100)
   
          #circle line attributes
          graph_rms=mgraph(           
              graph_line_colour: "magenta",
              graph_line_thickness: "2",
              graph_line_style: "dot",
              graph_symbol: "off"
              ) 
   
          #collect the plot definitions into a list  
          pltRmsLst=pltRmsLst & [iv_rms,graph_rms]
   
      end if
  end for
  
Please note that we use :func:`mvl_geocircle` to construct the circle and plotted the circle around every second waypoint to avoid cluttering. The only other change with respect to **Step 2** is that we need to extend the plot command with the new data layer (``pltRmsLst``):
  
.. code-block:: python
  
  plot(view,iv_track,graph_track,pltRmsLst,pltDateLst,title)
  
Having run the macro you will get a plot like this:

.. image:: /_static/flexpart_plume_trajectories/image2017-11-9_9-37-47.png

Step 4 - Plotting the cluster centres
*************************************

The trajectory output file also contains the coordinates of the cluster centres. 
In this step we will show a possible way to plot this extra bit of information together with the mean trajectory. Our approach is as follows:

* we plot the track as a curve

* we plot the mean trajectory points using symbols of different shape and colour at different times

* we use use the same symbols and colour-coding for the cluster centres but we use smaller a smaller symbol size for better readability

The macro to use is 'plot_tr_step4.mv'. 

This is a fairly long and advanced macro so we will not examine it here but try to encourage you to open it and study how it works.

Having run the macro you will get a plot like this:

.. image:: /_static/flexpart_plume_trajectories/image2017-11-9_11-0-19.png
