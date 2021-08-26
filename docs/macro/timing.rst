Timing functions
======================
   These functions allow some profiling of Macro's run times.


.. describe:: none stopwatch_start( string )

   Starts and names the macro stopwatch. Prints the current date and time. Only one stopwatch can be used at a time - the name is used only for the purpose of printing meaningful information. Starting a new stopwatch stops an existing stopwatch.


.. describe:: none stopwatch_laptime ( string )

   Prints the laptime since the previous call to stopwatch_laptime() , or from stopwatch_start() if there is no previous laptime. The string argument is used in the printout to identify the laptime.


.. describe:: none stopwatch_stop ()

   Stops the stopwatch and prints the total times since stopwatch_start() , or from stopwatch_reset() if that has been called. Also, prints the current date and time.


.. describe:: none stopwatch_reset ( string1 )

   Stops the stopwatch and restarts it with a new name. This is equivalent of calling stopwatch_stop() and then stopwatch_start() with a new name.