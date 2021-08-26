Plotting Functions
======================

.. describe:: definition mvl_flexpart_title(...)

   Generates a Text Plotting object to provide title for plotting FLEXPART output GRIB fields. This function uses this set of named keyword arguments:

    source: The FLEXPART output GRIB file.
    data: The FLEXPART output GRIB as a fieldset. It takes precedence over source.
    fontsize: Is the character height in cm. The default is 0.3 cm.
    units: The units string to display. If it is set to "header" the units are taken from the GRIB header. The default is an empty string

   Example:

   .. code-block:: python

      # if g is a fieldset containing FLEXPART output
      title=flexpart_build_title(data: g,fontsize: 0.3,units: "ng m**-3")
      plot(g,title)


.. describe:: definition mvl_geocircle(lat : number, lon : number,radius : number, resolution : number)

   Plots a circle with a given radius in km onto any map projections. Internally, the circle is split into a number of segments and the returned result is an Input Visualiser object which can be passed to the plot() command along with an optional Graph Plotting object.

   The first three parameters specify the centre and the radius (in km) of the circle. Parameter resolution defines the number of line segments to use to make up the circle.

   The usage of this function is demonstrated via the Geocircle on Map Example from the Gallery.


.. describe:: definition mvl_geoline(lat1 : number, lon1 : number, lat2 : number, lon2 : number,  incrm : number)

   Plots a straight line onto any map projections. Internally, the line is split into a number of segments and the returned result is an Input Visualiser object which can be passed to the plot() command along with an optional Graph Plotting object.

   The first four parameters define the end-points of the line. Parameter incrm specifies the increment, in degrees, into which the line should be split.

   The usage of this function is demonstrated via the Geoline on Map Example from the Gallery.


.. describe:: definition mvl_geopolyline(lat: vector, lon: vector, incr: number)

.. describe:: definition mvl_geopolyline(lat: list, lon: list, incr: number)

   Plots a polyline sampled on the cylindrical projection onto any map projections. Internally, each line section is split into a number of segments and the returned result is an Input Visualiser object which can be passed to the plot() command along with an optional Graph Plotting object.

   Parameter incrm specifies the increment, in degrees, into which the line sections should be split.

   The usage of this function is demonstrated via the Geopolyline on Map Example from the Gallery.

   This function was introduced in version 5.10.0.


.. describe:: plot(...)

   Generates a plot using the specified output device.


.. describe:: definition mvl_regular_layout(view: definition, page_columns: number, page_rows: number, subpage_columns: number, subpage_rows: number)

.. describe:: definition mvl_regular_layout(view: definition, page_columns: number, page_rows: number, subpage_columns: number, subpage_rows: number, plot_area: list)

   Creates a list of plot pages arranged in a regular grid using the specified view. Each plot page contains a set of (one or more) subframes, each arranged in a regular grid. The output is suitable for input into the function plot_superpage(). When a 6th argument is specified it defines the plot area the layout will occupy in the output. It is given as a list of [TOP, BOTTOM, LEFT, RIGHT] where the values are specified in percentages (0-100).

   Example:

   .. code-block:: python

      # create a 2x1 layout with the default geo view
      page_list = mvl_regular_layout(geoview(), 1, 2, 1, 1)

      # create a display window using this set of pages
      dw = plot_superpage(pages: page_list)


.. describe:: definition thermo_parcel_area(parcel: definition)

.. describe:: definition thermo_parcel_area(parcel: definition, pos_colour: string, neg_colour: string)

   Returns a set of coloured areas from a thermo parcel path object (the result of the thermo_parcel_path() function). The function returns a list of Input Visualiser and Graph Plotting icons that can be directly used in a plot() command. See the Parcel method on Skew-T Example from the Gallery for its usage.


.. describe:: definition xs_build_curve(xs_d: cross_section_data, fs: fieldset, colour: string, style:string, thickness: number)

   Convenience function to build a curve to be plotted in a Cross Section View with the given colour, style and thickness. The curve values are extracted from the first field in fieldset fs and they must be in the same units as the vertical axis of the cross section. The cross section definition itself is taken from the xs_d  Cross Section Data object (xs_d).  The function returns a list containing an Input Visualiser and a Graph Plotting icon, which can be directly used in a plot() command.

   The usage of this function is demonstrated via the Cross Section in Pressure with Orography and Boundary Layer Height Example example from the Gallery.

   This property was introduced in version 5.10.0.


.. describe:: definition xs_build_orog(xs_d: cross_section_data, orog_fs: fieldset, bottom_level: number, colour: string)

   Convenience function to build an orography area object to be plotted in a Cross Section View with the given colour. The orography values are extracted from the first field in fieldset orog_fs and they must be in the same units as the vertical axis of the cross section. The cross section definition itself is taken from the xs_d  Cross Section Data object (xs_d). The function returns a list containing an Input Visualiser and a Graph Plotting icon, which can be directly used in a plot() command.

   The usage of this function is demonstrated via the Cross Section in Height for Model Level Data with Orography example from the Gallery.

   This function was introduced in version 5.10.0.


.. describe:: definition xy_area(x:vector, y: vector, colour: string)

   Convenience function to build an area (i.e. a polygon) to be plotted in a Cartesian View with the given colour. The function returns a list containing an Input Visualiser and a Graph Plotting icon, which can be directly used in a plot() command.

   The usage of this function is demonstrated via the ENS Tephigram Example from the Gallery.

   This function was introduced in version 5.10.0.


.. describe:: definition xy_curve(x:vector, y: vector, colour: string, style: string, thickness: number)

.. describe:: definition xy_curve(x: list, y: list, colour: string, style: string, thickness: number)

   Convenience function to build a curve to be plotted in a Cartesian View with the given colour, style and thickness. The function returns a list containing an Input Visualiser and a Graph Plotting icon, which can be directly used in a plot() command.