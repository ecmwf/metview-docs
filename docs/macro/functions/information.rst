Information Functions
======================

   Here are listed a few functions which convey information about expressions and other macro functions.
 
.. describe:: string type (any)

   Returns the type of an expression as a string.


.. describe:: list arguments ()

   Returns the list of the arguments with which the current function was called. Used to retrieve the arguments passed to functions which are declared without an argument list and to retrieve arguments passed to a macro program run in batch mode.


.. describe:: none describe ( string )

   Prints a terse one-line description of the function whose name is passed as the argument.


.. describe:: list dictionary ()

   Returns a list of all the available functions.


.. describe:: number is_feature_available(string)

   Queries whether the specified feature is available in this version of Metview. Returns 1 if it is, or 0 if it is not. Currently, only the following string is accepted as the query term: "odb".

.. describe:: definition version_info ()

   Returns a definition containing version information about Metview and the libraries it was built with. Note that these versions are queried at run-time.
