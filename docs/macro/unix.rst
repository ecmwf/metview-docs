Unix Functions
======================

.. describe:: any getenv( string )

   Returns the value of an environment variable given its name as the argument.


.. describe:: string getenv ( string, number )

   Returns the value of an environment variable given its name as the argument. If a second argument (number) is given and the number is zero, the function returns a string, even if the environment variable content looks like a date or a number.


.. describe:: none nice ( number )

   Lower the priority of the macro by calling the nice() system call.


.. describe:: string putenv ( string,string )

   Sets the value of an environment variable, given its name as the first argument and its value as the second argument.


.. describe:: number shell ( ... )

   Returns the exit status of the command invoked.


.. describe:: none sleep ( number )

   Stops the macro for a given number of seconds