.. _macro_netcdf_fn:

NetCDF Macro functions
=========================

.. note::
   
      For an overview of how to handle netCDF data in Metview, please see :ref:`NetCDF <macro_netcdf>`.


.. describe:: netcdf ( netcdf op netcdf )

   Operation between two netcdf data units. op is one of the following :

   * \+ Addition
   * \- Subtraction
   * \* Multiplication
   * / Division
   * ^ Power
	
   The netcdf returned by these boolean operators are boolean netcdf (containing only 1 where result is true, 0 where it is false) :

   * > Larger Than
   * < Smaller Than
   * >= Larger or Equal
   * <= Smaller or Equal
   * = Equal
   * <> Not Equal

.. describe:: netcdf ( netcdf op number )
.. describe:: netcdf ( number op netcdf )

   Operations between netcdf and numbers. op is any of the operations defined above.


.. describe:: netcdf ( netcdf and netcdf )
.. describe:: netcdf ( netcdf or netcdf )

   Conjunction and Disjunction. Boolean operators consider all null values to be false and all non null values to be true. The netcdf created by boolean operators are binary netcdf (containing only 1 where result is true, 0 where it is false). For example :

.. describe:: netcdf 3 = netcdf1 and netcdf2

   creates a netcdf netcdf3 with values of 1 where the corresponding values of netcdf2 and netcdf2 are both non zero, and 0 otherwise.


.. describe:: definition attributes( netcdf )

   This function returns a definition variable holding the metadata of the input netcdf, e.g. date, time, levels, etc.

   .. code-block:: python

      attr_list = attributes(netcdf)
      date = attr_list.DATE
      levelist = attr_list.LEVELIST


.. describe:: list dimensions( netcdf )

   This returns a list of numbers, each representing one of the dimensions of the data held in the netcdf :

   .. code-block:: python

      dim_list = dimensions(netcdf)

   e.g. if the current variable is a cross section, the output list would have two numbers, the first the number of levels, the second the number of points along the horizontal.


.. describe:: list dimension_names(netcdf)

   Returns a list of the dimension names for the current netcdf variable.


.. describe:: definition global_attributes( netcdf )

   Returns a definition variable holding the netcdf's global metadata.


.. describe:: netcdf max( netcdf,netcdf )
.. describe:: netcdf min( netcdf,netcdf )

   Returns the netcdf of maximum (minimum) value of the two input netcdf.


.. describe:: netcdf max( netcdf,number )
.. describe:: netcdf min( netcdf,number )

   Returns the netcdf of the maximum (minimum) of the number and the netcdf values.


.. describe:: netcdf mod( netcdf,netcdf )

   Returns a netcdf whose values are the remainder of the division of the first netcdf by the second netcdf. Where the values of the second netcdf are larger than those of the first, the output value is set to the integer part of the value of the first netcdf. Note that only the integer parts of the inputs are considered in the calculation, meaning that a second parameter of 0.5 would cause a division by zero.


.. describe:: none netcdf_auto_rescale_values_to_fit_packed_type( number )

   Sets whether Metview automatically rescales values if they overflow the packed data type of the current variable. Setting the input number to 1 enables the rescaling (which is the default behaviour), setting it to 0 disables it. If disabled, and the computed values overflow the data type, the macro will fail.


.. describe:: none netcdf_auto_translate_times( number )

   Sets whether Metview automatically translates time variables into dates when retrieving with the value() or values() functions. Setting the input number to 1 enables the translation (which is the default behaviour), setting it to 0 disables it. If disabled, these functions will instead return the raw numbers encoded in the netCDF variable. This is a global option, not specific to a particular netcdf file.


.. describe:: none netcdf_preserve_missing_values( number )

   Sets whether Metview correctly handles missing values by not including them in computations. Set the input number to 1 to ensure the correct treatment of missing values, or set it to 0 to revert to Metview 4's behaviour of considering them to be normal numbers. This is a global option, not specific to a particular netcdf file.


.. describe:: none netcdf_auto_scale_values( number )

   Sets whether Metview automatically applies scale_factor and add_set attributes if they are present. Setting the input number to 1 enables the scaling (which is the default behaviour), setting it to 0 disables it. If disabled, the the raw numbers encoded in the netCDF variable will be used in any calculations. This is a global option, not specific to a particular netcdf file.


.. describe:: none setcurrent( netcdf, number )
.. describe:: none setcurrent( netcdf, string )

   On multi-variable netcdfs this sets the variable specified by the number or name given as the second argument as the current variable. Functions and operators act on the current variable only.

   The netcdf produced by the Metview applications are uni-variable, so in their case this function need not be used. For multi-variable netcdf variables, setcurrent() can be usefully combined with the function variables() :

   .. code-block:: python

      var_list = variables(netcdf)
      for i = 1 to count(var_list) do
         setcurrent(netcdf, i)
         netcdf = netcdf - 273.15 # acts on current variable only
      end for


.. describe:: number or date or string value ( netcdf, number )

   Returns the nth (second parameter) value of the current netcdf variable.


.. describe:: vector or date or list values( netcdf )
.. describe:: vector or date or list values( netcdf,list )

   Returns a vector (if the current variable is numeric) a list of strings (if the current variable is character-based) or a list of dates (if the current variable is time-based, Metview 5) containing all the values of the current variable.

   In order to extract the values for specific values of some of the variable's dimensions, a second parameter may be supplied. This should be a list with the same number of elements as the number of dimensions of the current netCDF variable. The elements (except one) should be numbers, specifying the indexes (1-based) into the respective dimensions from where the value(s) are to be taken. If all elements are numbers, then they simply specify the coordinates for a single value (returned as a single-value vector). Optionally, one of the elements can be set to the string "all"; in this case, all the values from that dimension are returned in a vector. For example, if the current netCDF variable is defined with 3 dimensions: Q(time, region, exp) then we can obtain the values for all times, for the second region and the fifth exp with this syntax:

   .. code-block:: python

      v = values(nc, ["all", 2, 5])


.. describe:: list variables( netcdf )

   Extracts the variable names of the variables contained in a netcdf and returns them as a list of strings. Count the number of elements in the output list to give you the number of variables. The netcdf produced by the Metview applications are uni-variable, so in their case this returns a single element list.

   .. code-block:: python

      var_list = variables(netcdf)
      print ("netcdf contains ", count(var_list), " variables")


