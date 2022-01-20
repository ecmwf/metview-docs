.. _flexpart_plotting_total_column_mass:

FLEXPART - Plotting total column mass
#####################################
 
For preparations and running the simulation needed for this tutorial :ref:`click here ... <flexpart_forward_simulation>`

.. note::

  To start this tutorial please enter folder 'forward'.
  
The total column integrated mass is not an output of FLEXPART so we need to compute it. 
The macro to do the computation and plot the resulting fields is 'plot_total.mv'.
  
In the macro first we call :func:`flexpart_total_column` to compute the "tcmd" fields:
  
.. code-block:: python
  
  dIn="result_fwd/"
  inFile=dIn  & "conc_s001.grib"
   
  #Compute the total column integrated mass
  g=flexpart_total_column(source: inFile, param: "mdc")
  
Next, we define the contouring. The "tcmd" fields have the units of "kg m**-2" but with the current value range "g m**-2" units would better fit for contouring. 
To achieve it we simply multiply the "tcmd" fieldset with 1000:
  
.. code-block:: python
  
  g=g*1000
  
The contour definition itself goes like this:
  
.. code-block:: python
  
  cont_list=[0.00001,0.0001,0.0005,0.001,0.002,0.005,0.01,0.05]
  
  #Define contour shading
  conc_shade = mcont(
      legend                          :   "on",
      contour                         :   "off",  
      contour_level_selection_type    :   "level_list",
      contour_level_list              :   cont_list,
      contour_label                   :   "off",
      contour_shade                   :   "on",
      contour_shade_method            :   "area_fill",
      contour_shade_max_level_colour  :   "red",
      contour_shade_min_level_colour  :   "RGB(0.14,0.37,0.86)",
      contour_shade_colour_direction  :   "clockwise",    
      contour_method                  :   "linear",
      grib_scaling_of_derived_fields  :   "off"
      )
  
Next, we build the title with :func:`flexpart_build_title`. 
Please note that we need to explicitly specify the plotting units!
  
.. code-block:: python
  
  title=flexpart_build_title(data: g,fontsize: 0.3,units: "g m**-2")   
  
Finally we define the map view:
  
.. code-block:: python
  
  #Define coastlines
  coast_grey = mcoast(
      map_coastline_thickness         :   2,
      map_coastline_land_shade        :   "on",
      map_coastline_land_shade_colour :   "grey",
      map_coastline_sea_shade         :   "on",
      map_coastline_sea_shade_colour  :   "RGB(0.89,0.89,0.89)",
      map_boundaries                  :   "on",
      map_boundaries_colour           :   "black",
      map_grid_latitude_increment     :   5,
      map_grid_longitude_increment    :   5
      )
  
  #Define geo view
  view = geoview(
      map_area_definition :   "corners",
      area                :   [40,-25,66,9],
      coastlines          : coast_grey
      )
  
and generate the plot:  

.. code-block:: python
  
  plot(view,g,conc_shade,title)
  
Having run the macro we will get a plot like this (after navigating to step 39h):

.. image:: /_static/flexpart_plotting_total_column_mass/image2017-10-25_16-46-40.png
