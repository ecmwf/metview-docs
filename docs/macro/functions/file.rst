File Functions
======================
   These functions work with files and other I/O tasks.


.. describe:: none append ( string,any,... )

.. describe:: none append ( filehandler,any,... )

   Writes output to a file specified by its name or by a filehandler previously assigned to it by the file() function. The output file type depends on the type that is being written - in exactly the same way as it does for the write() function (see below). As the name implies, append() never overwrites previously existing output. Note that special characters such as newline and tab can be written to text files.


.. describe:: number exist ( string )

   This function checks whether a file or directory exists. The single argument is the file or directory name - you must specify the full path . The function returns a number, 1 if the file exists and 0 otherwise. Use it combined with fail() or stop() for error checking :

   .. code-block:: python

      if (not(exist("/home/xy/xyz/metview/grib_file"))) then
      fail("specified input file does not exist!")
      end if
      (...)


.. describe:: filehandler file ( string )

   Assigns a file handler to a file whose name is the function argument. The file handler can be used in place of the file name in file output functions - write() and append() .


.. describe:: string filetype ( string )

   Returns the internal Metview type as a string of the specified file. When Metview cannot determine the type it returns the string "BAD".  For Metview icons not representing data it returns "NOTE".


.. describe:: none newpage ( display window )

   Forces a new page to be taken in the current PostScript file.


.. describe:: none print (...)

   Prints all its arguments to the output area of the main user interface (and to that of any opened macro editor window). Note that special characters such as newline and tab can be used here.


.. describe:: fieldset read ( string )
.. describe:: observations read ( string )
.. describe:: geopoints read ( string )
.. describe:: list read ( string )
.. describe:: netcdf read ( string )

   Reads a data file whose name is passed as the argument. If the file is the same folder as the macro program the path needn't be specified. The function returns a variable of the corresponding type. You needn't specify anyhing about the data type, it is automatically detected by the function.

   The variable of type list is used to hold the contents of an ASCII file - the elements of this list variable are themselves lists, each holding a line of text. The elements of these sub lists are the text line tokens (component strings) arising from the parsing of the text.


.. describe:: table read_table ( definition )

   Reads an ASCII table-based file such as a comma separated value (CSV) file. Use the Table Reader icon to construct the input definition for this function.


.. describe:: string tmpfile ( )

   Reserves and returns a unique file name (inside the Metview cache directory) for a temporary file. Returned filenames are unique even when there are several copies of the same macro being executed simultaneously.


.. describe:: none write ( string,any,... )
.. describe:: none write ( filehandler,any,... )

   Writes output to a file specified by its name or by a filehandler previously assigned to it by the file() function. The output file type depends on the type that is being written - if it is a fieldset then it creates a GRIB file, if it is observations it creates a BUFR file, if geopoints creates a geopoints file, if it is anything else it will create a text file with the current value of the variable(s) - an icon (associated with the corresponding file type) is also created if the files are saved to the Metview directory structure.

   If you use write() sequentially, note that it will overwrite any previous output if called with a file name, but will add to previous output if called with a filehandler.

   Note that special characters such as newline and tab can be written to text files.