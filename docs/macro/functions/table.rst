.. _macro_table_fn:

Table functions
======================

.. note::

   For an overview, please see :ref:`ASCII tables <macro_table>`.


.. describe:: number count( table )

   Returns the number of columns contained in the table.


.. describe:: string name( table, number )

   Returns the name of the column indexed by the second parameter (the first column is number 1). If the column has no name, nil is returned. If the column index is out of bounds, an error message is generated.


.. describe:: list metadata_keys( table )

   Returns a list of meta-data keys available for the given table. Only valid if meta-data rows are specified when reading the table. If there is no meta-data, then nil is returned.


.. describe:: string or list metadata_value( table, string )
.. describe:: string or list metadata_value( table, list )

   Returns the value corresponding to the meta-data key given as the second argument; if the given key is not valid for the table, nil is returned. If provided with a list of keys, a list of values will be returned; for those keys which are not valid for the table, nil values will appear in the return list. If the table contains no meta-data, nil is returned.


.. describe:: table read_table( definition )

   Reads the given table into memory. See :func:`read_table`.


.. describe:: vector or list values( table, number )
.. describe:: vector or list values( table, string )

   Returns the given column specified either by an index (starting at 1) or a name (only valid if the table has a header row). If the column type is number, a vector is returned; if it is string, then a list of strings is returned. If the column cannot be found, an error message is generated.
