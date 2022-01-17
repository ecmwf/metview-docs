Utility Macro functions
======================================

.. note::

    This is a collection of various system and utility functions:

    * to convey information about expressions and other macro functions
    * to allow some profiling of Macro's run times
    * to interface with the Unix environment
    * to provide run control for macros


.. describe:: list arguments ()

   Returns the list of the arguments with which the current function was called. Used to retrieve the arguments passed to functions which are declared without an argument list and to retrieve arguments passed to a macro program run in batch mode.


.. describe:: none describe ( string )

   Prints a terse one-line description of the function whose name is passed as the argument.


.. describe:: list dictionary ()

   Returns a list of all the available functions.


.. describe:: none fail(string)

   Stops the execution of a macro, printing the input string to the main UI output area. Assigns error status to the macro icon (name turns red). Use to exit a macro on an error condition - input string should be a suitable error message.

.. describe:: any fetch (string)

   Retrieves an item stored in a cache under the name specified as the argument.

   .. code-block:: python

      s = fetch("wind speed")

   The fetch() function returns nil if the specified data is not in the cache.


.. describe:: any getenv( string )

   Returns the value of an environment variable given its name as the argument.


.. describe:: string getenv ( string, number )

   Returns the value of an environment variable given its name as the argument. If a second argument (number) is given and the number is zero, the function returns a string, even if the environment variable content looks like a date or a number.


.. describe:: number is_feature_available(string)

   Queries whether the specified feature is available in this version of Metview. Returns 1 if it is, or 0 if it is not. Currently, only the following string is accepted as the query term: "odb". 

.. describe:: string name ()

   This function returns the name of the macro being executed. It can be used in conjunction with the store() and fetch() functions.

.. describe:: none nice ( number )

   Lower the priority of the macro by calling the nice() system call.


.. describe:: string purge_mem ()

   This function frees up previously reserved memory and can be used at any time.


.. describe:: string runmode ()

   Returns the macro run mode - Execute, Visualise, Save, Examine, Edit, Batch, Prepare - as a string.


.. describe:: number runmode (string)

   Returns 1 if the macro run mode is the same as the one specified in the input string and 0 if not


.. describe:: string putenv ( string,string )

   Sets the value of an environment variable, given its name as the first argument and its value as the second argument.


.. describe:: number shell ( ... )

   Returns the exit status of the command invoked.


.. describe:: none sleep ( number )

   Stops the macro for a given number of seconds

.. describe:: none stop (string)

   Stops the execution of a macro, printing the input string to the main UI output area. Assigns OK status to the macro icon (name turns green). Use to exit a macro upon some non error condition - input string should be a suitable exit status message.


.. describe:: none stopwatch_start( string )

   Starts and names the macro stopwatch. Prints the current date and time. Only one stopwatch can be used at a time - the name is used only for the purpose of printing meaningful information. Starting a new stopwatch stops an existing stopwatch.


.. describe:: none stopwatch_laptime ( string )

   Prints the laptime since the previous call to stopwatch_laptime() , or from stopwatch_start() if there is no previous laptime. The string argument is used in the printout to identify the laptime.


.. describe:: none stopwatch_stop ()

   Stops the stopwatch and prints the total times since stopwatch_start() , or from stopwatch_reset() if that has been called. Also, prints the current date and time.


.. describe:: none stopwatch_reset ( string1 )

   Stops the stopwatch and restarts it with a new name. This is equivalent of calling stopwatch_stop() and then stopwatch_start() with a new name.


.. describe:: any store (string,any)

   Saves the item given as the second argument in a cache under the name specified as the first argument

   .. code-block:: python

      store("wind speed",s) 

 
.. describe:: string type (any)

    Returns the type of an expression as a string.
   

.. describe:: definition version_info ()

    Returns a definition containing version information about Metview and the libraries it was built with. Note that these versions are queried at run-time.
 