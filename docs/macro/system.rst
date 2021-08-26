System Functions
======================

.. describe:: none fail(string)

   Stops the execution of a macro, printing the input string to the main UI output area. Assigns error status to the macro icon (name turns red). Use to exit a macro on an error condition - input string should be a suitable error message.


.. describe:: any fetch (string)

   Retrieves an item stored in a cache under the name specified as the argument.

   .. code-block:: python

      s = fetch("wind speed")

   The fetch() function returns nil if the specified data is not in the cache.


.. describe:: string name ()

   This function returns the name of the macro being executed. It can be used in conjunction with the store() and fetch() functions.


.. describe:: string purge_mem ()

   This function frees up previously reserved memory and can be used at any time.


.. describe:: string runmode ()

   Returns the macro run mode - Execute, Visualise, Save, Examine, Edit, Batch, Prepare - as a string.


.. describe:: number runmode (string)

   Returns 1 if the macro run mode is the same as the one specified in the input string and 0 if not


.. describe:: none stop (string)

   Stops the execution of a macro, printing the input string to the main UI output area. Assigns OK status to the macro icon (name turns green). Use to exit a macro upon some non error condition - input string should be a suitable exit status message.


.. describe:: any store (string,any)

   Saves the item given as the second argument in a cache under the name specified as the first argument

   .. code-block:: python

      store("wind speed",s) 