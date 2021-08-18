Geopoints Functions
======================


   For an overview, please see Geopoints.

.. describe:: geopoints ( geopoints op geopoints )

   Operation between two geopoints. op is one of the following :

   * \+ Addition
   * \- Subtraction
   * \* Multiplication
   * / Division
   * ^ Power
  
   The geopoints returned by these boolean operators are boolean geopoints (containing only 1 where result is true, 0 where it is false) :

   * > Larger Than
   * < Smaller Than
   * >= Larger or Equal
   * <= Smaller or Equal
   * = Equal
   * <> Not Equal


.. describe:: geopoints ( geopoints op number )
.. describe:: geopoints ( number op geopoints )

   Operations between geopoints and numbers. op is any of the operations defined above. Missing values retain their value of geo_missing_value .


.. describe:: geopoints ( geopoints op fieldsets )
.. describe:: geopoints ( fieldsets op geopoints )

   Operations between geopoints and fielsets. op is any of the operations defined above. Missing values, both in the fieldset and in the original geopoints variable result in a value of geo_missing_value .


.. describe:: geopoints ( geopoints and geopoints )
.. describe:: geopoints ( geopoints or geopoints )
.. describe:: geopoints ( not geopoints)

   Conjunction, Disjunction and Negation. Boolean operations on geopoints consider all null values to be false and all non null values to be true. Missing values retain their value of geo_missing_value.


.. describe:: geopoints ( geopoints & geopoints & ... )
.. describe:: geopoints ( nil & geopoints & ... )
.. describe:: geopoints ( geopoints & nil )


.. describe:: geopoints merge ( geopoints,geopoints,... )

   Merge several sets of geopoints. The output is the concatenation of each set of geopoints. Merging with the value nil does nothing, and can be used to initialise when building a set of geopoints in a loop. Note that only geopoints that are in the same format can be merged. See Geopoints for details of the different formats.
   
   
.. describe:: definition geopoints[ number ]

   Returns a definition with values of the nth point of the geopoints. Note that, unlike lists, the first geopoint is at index 0.


.. describe:: geopoints abs ( geopoints )

   Returns the geopoints of the absolute value of the input geopoints. Missing values retain their value of geo_missing_value.



.. describe:: geopoints asin ( geopoints )
.. describe:: geopoints acos ( geopoints )
.. describe:: geopoints atan  ( geopoints )

   Returns the geopoints of the arc trigonometric function of the input geopoints. Result is in radians. Missing values retain their value of geo_missing_value.


.. describe:: geopoints cos ( geopoints )

   Return the cosine of the input geopoints. These must be in radians. Missing values retain their value of geo_missing_value.


.. describe:: geopoints exp ( geopoints )

   Returns the geopoints of the exponential of the input geopoints. Missing values retain their value of geo_missing_value.


.. describe:: geopoints int ( geopoints )

   Returns the geopoints of the integer part of the input geopoints. Missing values retain their value of geo_missing_value.


.. describe:: number intbits ( geopoints,number )
.. describe:: number intbits ( geopoints,number,number )

   Takes the integer part of the geopoints values and extracts a specified bit (or number of bits if a second number parameter is specified), where bit number 1 is the least significant bit. A single bit will always be returned as 1 or 0, regardless of its position in the integer. A group of bits will be treated as if the first bit is the least significant bit of the result.

   A few examples from the number version of this function illustrate how it works:

   .. code-block:: python
   
        # To extract the 1st, 2nd and 3rd bits from a number separately:
        n = 6 # in bit-form, this is "00000110" with the least significant bit at the right
        
        flag = intbits (n, 1) # flag is now 0
        flag = intbits (n, 2) # flag is now 1
        flag = intbits (n, 3) # flag is now 1
        
        # To extract the 1st and 2nd bits together to make a single number:
        flag = intbits (n, 1, 2) # flag is now 2
        
        # To extract the 2nd and 3rd bits together to make a single number:
        flag = intbits (n, 2, 2) # flag is now 3
        
        #To extract the 3rd and 4th bits together to make a single number:
        flag = intbits (n, 3, 2) # flag is now 1

   The number of bits available depends on the machine architecture and Metview's compilation options, but at the time of writing it should be 32. This function does not treat missing values differently from any other values (for efficiency with large datasets).


.. describe:: geopoints log ( geopoints )

   Returns the geopoints of the natural log of the input geopoints. Missing values retain their value of geo_missing_value.


.. describe:: geopoints log10 ( geopoints )

   Returns the geopoints of the base 10 log of the input geopoints. Missing values retain their value of geo_missing_value.


.. describe:: geopoints neg ( geopoints )

   Returns the geopoints of the negative of the input geopoints. The same as (- geopoints). Missing values retain their value of geo_missing_value.


.. describe:: geopoints sgn ( geopoints )

   Returns the geopoints of the sign of the values of the input geopoints : -1 for negative values, 1 for positive and 0 for null values. Missing values retain their value of geo_missing_value.


.. describe:: geopoints sin ( geopoints )

   Return the sine of the input geopoints. These must be in radians. Missing values retain their value of geo_missing_value.


.. describe:: geopoints sqrt ( geopoints )

   Returns the geopoints of the square root of the input geopoints. Missing values retain their value of geo_missing_value.


.. describe:: geopoints tan ( geopoints )

   Return the tangent of the input geopoints. These must be in radians. Missing values retain their value of geo_missing_value.


.. describe:: list columns ( geopoints )

   Returns a list containing the names of the columns in the given geopoints variable.


.. describe:: number count ( geopoints )

   Returns the total number of elements in the geopoints.


.. describe:: geopoints create_geo ( number )
.. describe:: geopoints create_geo( number, string )
.. describe:: geopoints create_geo( number, string, number )
.. describe:: geopoints create_geo( number, string, number, list )
.. describe:: geopoints create_geo( ... )

   Creates a new geopoints variable with the given number of points, all set to default values and coordinates. It is intended that this function be used in conjunction with the set_xxx geopoints functions in order to populate the geopoints with data. If saved, the geopoints file will be in the "traditional" 6-column format. If another format is desired, supply a string as the second parameter, possible values being 'polar_vector ', 'xy_vector ', 'xyv ' and 'ncols'. If format 'ncols' is specified, then the number of value columns can be given as the third argument (default is 1). In this case, an optional fourth argument can be used to provide a list of names of the value columns.

   An alternative, and more efficient way to create a new geopoints variable if you already have the data to populate it, is to provide a set of named arguments as shown in the examples below. Using this syntax, you can completely create a new geopoints variable with all its column data in one go. This is much more efficient than creating an empty geopoints variable and then populating it using the set_ functions.

   Examples are shown below:

   .. code-block:: python

        g = create_geo(8) # default geopoints format, 8 values
        g = create_geo(9, 'xyv') # XYV formatted geopoints with 9 values
        g = create_geo(4, 'ncols', 3, ['t', 'z', 'precip']) # NCOLS format with 3 named columns, each containing 4 values
        g = create_geo(type:'standard',
                    latitudes:  |4, 5, 6|,
                    longitudes: |2.3, 1.1, 6.5|,
                    levels:     850,  # all rows will have 850 as their level
                    values:     |1.1, 2.2, 3.3|,
                    times:      nil)
        g = create_geo(type:'xyv',
                    latitudes:  |4, 5, 6|,
                    longitudes: |2.3, 1.1, 6.5|,
                    values:     |1.1, 2.2, 3.3|)
        g = create_geo(type:       'ncols',
                    latitudes:  |4, 5, 6|,
                    longitudes: |2.3, 1.1, 6.5|,
                    levels:     850,  # all rows will have 850 as their level
                    times:      nil,
                    stnids:     ['aberdeen', 'aviemore', 'edinburgh'],
                    temp:       |273.15, 269.78, 281.45|,
                    precip:     [4, 5, 1],  # lists also work, but are less efficient
                    speed:      |2, 3, 5| )


.. describe:: list dates ( geopoints )

   Extracts the date information of all the geopoints and returns it as a list of dates.


.. describe:: string or list db_info ( geopoints,string )
.. describe:: string db_info ( geopoints,string,string )

   Returns information about the database retrieval which generated the geopoints. The first string parameter specifies which piece of information you would like; possible values are:

   * "name": the name of the database system, e.g. "ODB"
   * "path": the path to the database
   * "query": a list of strings containing the multi-line data query
   * "column": the name of the database column used to populate a given element of the geopoints. A second string must be provided, naming the geopoints element of interest - possible values are "lat", "lon", "level", "date", "time", "value" and "value2".
   * "alias": similar to column above, but returns the name of the database alias used instead of the full column name

   Note that this information is derived from the DB_INFO section (if it exists) in the geopoints file header (see Storing Data Origin Information in a Geopoints File).


.. describe:: geopoints distance ( geopoints,number,number )
.. describe:: geopoints distance ( geopoints,list )

   Returns geopoints with the value of each point being the distance in meters from the given geographical location. The location may be specified by supplying either two numbers (latitude and longitude respectively) or a 2-element list containing latitude and longitude in that order. The location should be specified in degrees. A geopoint with either latitude or longitude set to missing value will have a distance of missing value.


.. describe:: geopoints filter ( geopoints,geopoints )

   A filter function to extract a subset of its geopoints input using a second geopoints as criteria. The two input geopoints must have the same number of values. The resulting output geopoints contains the values of the first geopoints where the value of the second geopoints is non-zero. It is usefully employed in conjunction with the comparison operators :

   .. code-block:: python

        freeze = filter(temperature,temperature < 273.15)

   The variable freeze will contain a subset of temperature where the value is below 273.15. The following example shows how to plot a geopoints set with different colours:

   .. code-block:: python

        # Filter from "temperature" points at, above, below 273.15
        cold = filter( temperature,temperature<273.15 )
        zero = filter( temperature,temperature=273.15 )
        warm = filter( temperature,temperature>273.15 

        # Create three symbol plotting definitions
        red = psymb( symbol_colour : "red" )
        blue = psymb( symbol_colour : "blue" )
        lack = psymb( symbol_colour : "black" )

        # Plot everything
        plot(zero,black,cold,blue,warm,red)


.. describe:: geopoints filter ( geopoints,vector )

   A filter function to extract a subset of its geopoints input using the values in a vector as criteria. The vector should contain the same number of elements as there are in the geopoints. An example, which uses a named column for the filter criteria is:

   .. code-block:: python
   
        new_gpt = filter(gpt, gpt['precip'] > 5)  # "gpt['precip'] > 5" returns a vector of 1s and 0s


.. describe:: geopoints filter ( geopoints,number )
.. describe:: geopoints filter ( geopoints,list )

   A filter function to extract a subset of its geopoints input using model levels as criteria.
    
   If the second argument is a number, the function extracts all the geopoints for which the level is equal to the number.
        
   If the second argument is a list of two numbers [n1,n2] , the function extracts all the geopoints for which the level lies in the n1-n2 interval.


.. describe:: geopoints filter ( geopoints,date )
.. describe:: geopoints filter ( geopoints,list )

   A filter function to extract a subset of its geopoints input using dates as criteria.

   If the second argument is a date, the function extracts all the geopoints for which the date is equal to the one specified as the second argument.
        
   If the second argument is a list of two dates [d1,d2] , the function extracts all the geopoints for which the date lies in the d1-d2 interval.


.. describe:: geopoints filter ( geopoints,list )

   A filter function to extract a subset of its geopoints input using a geographical area as criteria.

   The second argument is a list of four numbers (lat/long coordinates) defining a geographical area - [North,West,South,East] . The function extracts all the geopoints that fall within the specified area.


.. describe:: geopoints geosort ( geopoints )

   Returns a new geopoints variable that contains the input geopoints sorted geographically from North to South (and West to East in points with the same latitude value, then by height, with lowest numerical values first).


.. describe:: geopoints interpolate ( fieldset,geopoints )

   Generates a set of geopoints from a field. The first parameter must contain a single field. The field is interpolated for each position of the geopoints given as a second parameter. Where it is not possible to generate a sensible value due to lack of valid data in the fieldset, the internal geopoints missing value is used (this value can be checked for with the built-in variable geo_missing_value or removed with the function remove_missing_values ). This function will return a missing value where the geopoints have missing lat/lon.


.. describe:: vector latitudes ( geopoints )

   Extracts the latitudes of all the geopoints and returns them as a vector..


.. describe:: vector levels ( geopoints )

   Extracts the heights of all the geopoints and returns them as a vector.


.. describe:: vector longitudes ( geopoints )

   Extracts the longitudes of all the geopoints and returns them as a vector.



.. describe:: geopoints max ( geopoints,geopoints )
.. describe:: geopoints min ( geopoints,geopoints )

   Returns the geopoints of maximum (minimum) value at each point. Missing values retain their value of geo_missing_value.


.. describe:: geopoints max ( geopoints,number )
.. describe:: geopoints min ( geopoints,number )

   Returns the geopoints of the maximum (minimum) of number and the geopoints value at each point. Missing values retain their value of geo_missing_value.


.. describe:: geopoints max ( geopoints,fieldsets )
.. describe:: geopoints min ( geopoints,fieldsets )

   Returns geopoints of maximum (minimum) of the geopoints value and the geopoints value at each grid point or spectral coefficient. Missing values, either in the fieldset or in the original geopoints variable, result in a value of geo_missing_value.


.. describe:: number maxvalue ( geopoints )
.. describe:: number minvalue ( geopoints )

   Returns the maximum (minimum) value of all geopoints values. Missing values are bypassed in this calculation. If there are no valid values, then nil is returned.


.. describe:: number mean ( geopoints )

   Computes the mean of the geopoints. Missing values are bypassed in this calculation. If there are no valid values, then nil is returned.


.. describe:: geopoints mask ( geopoints,list )

   Creates a geopoints variable containing point values of 0 or 1 according to whether they are inside (1) or outside (0) a defined geographical area.

   The list parameter must contain exactly four numbers representing a geographical area. These numbers should be in the order north, west, south and east (negative values for western and southern coordinates). Points with missing latitudes or longitudes are considered to be outside any area. See the documentation for the fieldset version of this function to see how to compose more complex regions than a simple rectangular area.


.. describe:: geopoints nearest_gridpoint ( fieldset,geopoints[,string] )

   Generates a set of geopoints from a field. The first field of the input fieldset is used. The result is a set of geopoints whose locations are taken from the original geopoints, but whose values are those of the nearest gridpoints in the field to the geopoints given as a second parameter. By default, when the nearest gridpoint value is a missing value or the location is out of the grid area, the internal geopoints missing value is used (this value can be checked for with the built-in variable geo_missing_value or removed with the function remove_missing_values). If an extra parameter 'valid' is added to the function call, then of the surrounding points, the nearest valid one is returned; geo_missing_value will still be returned if all the surrounding points are missing. This function will return a missing value where the geopoints have missing lat/lon.


.. describe:: geopoints offset ( geopoints,number,number )
.. describe:: geopoints offset ( geopoints,list)

   Modifies the locations of a set of geopoints by specified amounts. The offsets can be specified either as two separate numbers or as a 2-element list. The original geopoints variable is unaffected; the functions return a new variable.


.. describe:: geopoints polar_vector ( geopoints, geopoints )

   Combines two single-parameter geopoints variables into a polar vector style geopoints variable. The first represents speed, the second represents direction. Both input geopoints variables should contain the same number of points.


.. describe:: geopoints remove_duplicates ( geopoints )

   Returns a new geopoints variable that contains just one instance of any duplicate geopoint. Two geopoints are considered to be duplicates of each other if the files have the same format and the points have the same coordinates, height, date, time and values.


.. describe:: geopoints remove_missing_latlons ( geopoints )

   Returns a new geopoints variable that contains just the points that do not have missing latitudes or longitudes from the input geopoints variable.



.. describe:: geopoints remove_missing_values ( geopoints )

   Returns a new geopoints variable that contains just the non-missing values from the input geopoints variable. A geopoint is considered to be missing if either its value or value2 members are missing.


.. describe:: geopoints set_latitudes ( geopoints, number or vector or list )
.. describe:: geopoints set_longitudes ( geopoints, number or vector or list )
.. describe:: geopoints set_levels ( geopoints, number or vector or list )
.. describe:: geopoints set_dates ( geopoints, number or vector or list )
.. describe:: geopoints set_stnids ( geopoints, list )
.. describe:: geopoints set_times ( geopoints, number or vector or list )
.. describe:: geopoints set_values ( geopoints, number or vector or list )
.. describe:: geopoints set_values ( geopoints, number or string, number or vector or list )

   Returns a new geopoints variable with either its latitude, longitude, level, date, time, stnid, value, value2 or another value column modified.

   All these functions take two or three parameters: first one must be a geopoints variable. If three parameters are given, the second should be either the index or name of the values column to update. The last parameter defines the new values, and can be a number, a vector or a list of numbers (or dates, if set_dates()). If a number is given then all the corresponding values (latitude, longitude, level, or ...) are replaced by the given value.

   If a vector or list is given as the last parameter then the corresponding values are replaced from the given vector or list. If the vector or list is shorter than the geopoints count then only the first values that have a corresponding value in the vector or list are changed.

   NOTE: for dates, 8 digit integers must be used. If the list contains non-numbers, then a missing value is written into the corresponding geopoints value.

   Examples of usage:

   .. code-block:: python

        new_gpt_a = set_latitudes(gpt_a, |30, 40, 50|)
        new_gpt_b = set_values(gpt_b, |12.4, 13.3, 1.1|)
        new_gpt_c = set_values(gpt_c, 4, |3.3, 4.4, 5.5|) # update the 4th value column
        new_gpt_d = set_values(gpt_d, 'precip', |0.3, 0.2, 0.1|) # update the column labelled 'precip'

        Note that the above functions generate a new geopoints variable, leaving the original one intact. If you wish to modify the original variable, then a more efficient way is to directly access the columns using the following syntax, following the examples above:
        gpt['latitude'] = |30, 40, 50|
        gpt['value'] = |12.4, 13.3, 1.1|
        gpt[name_of_column_4] = |3.3, 4.4, 5.5|
        gpt['precip'] = |0.3, 0.2, 0.1|


.. describe:: list stnids ( geopoints )

   Extracts the station id strings from all the geopoints and returns them as a list. If a given point does not have a station id, then a nil will be returned in its place in the list.


.. describe:: geopoints subsample ( geopoints, geopoints )

   Returns a geopoints variable containing the same locations (latitude, longitude and height) as the second geopoints variable, but whose values are from the first geopoints variable (or a missing value if point not found in the first variable). Note that the resulting geopoints variable is sorted in the same way as performed by the geosort() function. This means that you need to be careful if performing functions between the results of a subsample() operation and another geopoints variable; if the locations in the two geopoints are the same, then you should geosort() the second geopoints beforehand. Points with missing latitudes or longitudes will still be in the output, but the rule is that such a point is defined not to be at the same location as another point, even if its lat/lon are also missing. Advice: remove missing lat/lon points using remove_missing_latlons() before using subsample() or geosort().

   You can use function remove_missing_values() if you need to get rid of the missing valued points in the returned geopoints variable.


.. describe:: number sum ( geopoints )

   Computes the sum of the geopoints. Missing values are bypassed in this calculation. If there are no valid values, then nil is returned.


.. describe:: vector times ( geopoints )

   Extracts the times of all the geopoints and returns them as a vector.


.. describe:: vector or list values ( geopoints )
.. describe:: vector or list values ( geopoints, number )
.. describe:: vector or list values ( geopoints, string )

   Extracts the values of all the geopoints and returns them as a vector. If the values are strings, then the result is a list of strings. A value column other than the first one can be specified either by index (1-based in Macro or 0-based in Python) or by name, e.g. values(gpt, 4) or values(gpt, 'geopotential'). See the description of the NCOLS subformat on the Geopoints page for more details of storing multiple value columns. Another syntax is to use direct indexing, e.g.

   .. code-block:: python

        a = gpt['geopotential']


.. describe:: vector value2 ( geopoints )

   Extracts the second values of all the geopoints and returns them as a vector.


.. describe:: list value_columns ( geopoints )

   Returns a list containing the names of just the non-coordinate value columns in the given geopoints variable.


.. describe:: geopoints xy_vector ( geopoints, geopoints )

   Combines two single-parameter geopoints variables into a u/v style geopoints variable. Both input geopoints variables should contain the same number of points.

