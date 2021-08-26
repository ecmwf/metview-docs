ODB Functions
======================


   For an overview, please see the ODB tutorial here. There is also a shorter tutorial available on this page.


.. describe:: number columns( odb )

   Returns a list of the names of the columns in the given ODB variable. If there are no columns, then nil is returned.


.. describe:: number count( odb )

   Returns the number of rows contained in the ODB.

 

.. describe:: odb odb_filter(...)

   Performs an ODB/SQL query resulting in a new ODB. This is a Metview icon function, for detailed documentation please see :func:`odb_filter`.


.. describe:: definition odb_visualiser(...)

   Defines an object to visualise ODB data using various techniques and plot types. Optionally can run a filter on the ODB data for visualisation. This is a Metview icon function, for detailed documentation please see :func:`odb_visualiser`.


.. describe:: odb read( path )

   Returns an ODB object representing an ODB file/database specified by its file system path.


.. describe:: vector or list values( odb, string )

   Returns the given column specified by its name. If the column type is number, a vector is returned; if it is string, then a list of strings is returned. If the column cannot be found, nil is returned.
