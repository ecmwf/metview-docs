.. _macro_table:

ASCII Tables
=========================

.. note::

   Metview incorporates functionality to read, process and visualise data stored in ASCII table files. The Table Reader icon provides the means to generate Macro code to parse a table file. Once in memory, Macro's vector functions can be used to manipulate the data values. For visualisation, use the Table Visualiser icon. For a full list and details of functions and operators on vectors, see :ref:`Table functions <macro_table_fn>`.
   
   
Format Details
++++++++++++++++++

Many varieties of ASCII tables can be handled, but the simplest (and default) is the comma-separated value (CSV) style as shown in the example below::

   h1,h2,h3,h4
   34,23,54,Saturn
   76,34,65,10,Mars
   55,44,22,19,Jupiter

Each column contains a field and each row contains a record. The (optional) first row contains the name of each column. The remainder of the rows contain comma-separated values (other separator options are possible). The Table Reader icon allows the user to specify how their table is formatted, which columns to read and which data types are in each column. If no data types are specified, then the first row of data will be examined and an attempt made to identify the data type (number or string) of each column.

When delimiters are not combined, missing values are easily identified as the following three example rows show::

   6,,8
   ,7,8
   6,7,

When delimiters are combined, it is no longer possible to identify missing values. In the Macro language, the bitmap() function can be used to convert values to missing values.

Multiple rows containing meta-data can be included in a table file. The formatting of this meta-data is more strictly controlled and must be a space-separated list of PARAM=VALUE pairs. This meta-data can be accessed in the Macro language, and is also used when visualising the data.

The following example shows a table file with 5 rows of meta-data, followed by a header row, followed by combined-space-delimited data rows::

   type=FLEXTRA cfl=2.00 cflt=2.00 date=20111114 dx=1.00 dy=1.00
   east=30.00 integration=PETTERSSEN interpolation=LINEAR
   max_w_int=21600SECONDS model_comment=FLEXTRA normal_w_int=10800SECONDS
   north=75.00 south=30.00 start_comment=1 stop_index=4 time=90000
   tr_type=3-DIMENSIONAL west=-10.00
   SECS LONGIT LATIT ETA PRESS Z Z-ORO PV THETA
   0 -0.8300 51.5700 0.9518 963.5 500.0 405.7 1.450 282.8
   3600 -1.1573 51.6643 0.9532 964.1 491.8 393.7 1.095 282.7
   7200 -1.4730 51.7426 0.9540 964.0 489.7 387.3 0.781 282.7
   10800 -1.7778 51.8056 0.9541 963.3 493.5 386.1 0.509 282.8
   14400 -2.0913 51.8501 0.9548 961.8 502.9 380.4 0.468 282.9
   18000 -2.4282 51.8955 0.9564 960.3 511.7 366.1 0.499 283.1
   21600 -2.7885 51.9420 0.9590 959.0 519.3 343.5 0.596 283.3

The next section shows some Macro code to parse this table.

Using ASCII Tables in Macro
++++++++++++++++++++++++++++++++

After being read with the read_table() function, a table's columns can be accessed either by index or by name. A column will either be a vector of numbers or a list of strings. Meta-data can also be queried.

The following example code shows how to read a standard CSV file, such as the first example presented on this page, in Macro:

.. code-block:: python

   my_table = read_table(table_filename : "mytable.csv")
   print(values(my_table, 'h1'))

The default parameters of Metview's table reader are such that a standard CSV file (comma-separated, one header row) is read without additional arguments. We can then extract the values from the first row by using its name as an argument to the values() function.

The following example code shows how to read the FLEXTRA data file shown above in this page, how to extract its data, and how to access its meta-data.

.. code-block:: python

   my_table = read_table
   (
      table_delimiter             : " ",
      table_combine_delimiters    : "on",
      table_header_row            : 6,
      table_data_row_offset       : 1,
      table_filename              : "table_with_metadata.txt",
      table_meta_data_rows        : [1,2,3,4,5]
   )

   for i = 1 to count(my_table) do # print each column
   print(name(my_table, i), ' : ', values(my_table, i))
   end for

   keys = metadata_keys(my_table)
   print(keys)
   print(metadata_value(my_table, keys)) # print all keys/values
   print(metadata_value(my_table, 'type'))