.. _organising_macros:

Organising Macros
#################

**Download**
  
.. list-table::

  * - **File**
    - **Modified**

  * - File `organising macros.tar.gz <https://confluence.ecmwf.int/download/attachments/45758629/organising macros.tar.gz?api=v2>`_
    - Mar 19, 2015 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_

Functions
*********

The most basic way to group lines of Macro code is into a *function*. 
Let's write a function to compute wind speed given its U and V vector components.

We've already written code to compute wind speed:

.. code-block:: python

  speed = sqrt(u*u + v*v)
  
We can easily create a function around this code, taking ``u`` and ``v`` as input parameters. 
Create a new Macro icon and call it wind_speed. 
Enter the following into it:

.. code-block:: python
  
  function wind_speed(u, v)
    speed = sqrt(u*u + v*v)
    return speed
  end wind_speed
  
Within the same macro, read in some wind data and call the function, plotting the result:

.. code-block:: python
  
  u = read('wind_u.grib')
  v = read('wind_v.grib')
  speed = wind_speed(u,v)
  plot(speed)
  
Note that it does not matter where the function is defined in the macro - it will be found.

Notice that the function does not restrict the type of variables coming into it - they could be fieldsets, numbers, geopoints or any other data type which is compatible with the operations being performed by the function (square root, multiplication and addition). Try calling the function with plain numbers:

.. code-block:: python

  print(wind_speed(3, 4))
  
We could restrict the function so that it only accepts fieldset parameters:

.. code-block:: python

   function wind_speed(u:fieldset, v:fieldset)
   
This can be useful in some cases, but for this particular example the functionality is so general that it will work with fieldsets, geopoints, numbers and vectors - so we can leave this restriction out. 
See the supplied Syntax Sheet for more examples of how to define functions.

Including Other Macros
**********************

Now split the macro into two separate files: the *wind_speed* macro should have the function definition, and the *call_wind_speed* macro should read the GRIB data, call the function and plot the data (it should not work now, because it cannot find the function).

The include command *literally* includes the text of any macro at the insertion point. 
In our current example to make the function available to the ``call_wind_speed`` macro, it is enough to add the line:

.. code-block:: python

  include "wind_speed"
  
anywhere in the macro.

The included macro is read at the point where the ``include`` instruction is found. 
You can specify absolute or relative path names (relative to the position of the macro being run).

In this way you can place small libraries of functions in macro files, stored in a folder of your choice, ready for inclusion.

Inclusion does not require the included macro to be a self contained program or function - any partial fragment of code can be included, for example some variable declarations.

.. note::

  An ``include`` statement is interpreted before the macro is run.
  This means that you cannot, for instance, use a dynamically generated path to find the file to be included.

Functions in a User/System Library
**********************************

This is the method that can be really described as building a library of functions. 
Its principle is very simple - place macro functions in a particular folder which is searched by the function look-up procedure so they can be called from any macro program without the need for an ``include`` statement.

In our case, simply drag the *wind_speed* macro icon to the folder ``~/metview/System/Macros``. 
From then on you can call this function from within any of your macros. 
**Note that this only works when the name of the macro file is the same as the name of the function it contains**. Remove the ``include`` statement from your *call_wind_speed* macro and see if it still works (it should). 
If you rename the *wind_speed* macro, or the function inside it, it should no longer work.

This allows you to build your own personal function library. For a function to be available to other users, you can place the macros with the functions into shared folder on the file system; all users will need to set the environment variable ``METVIEW_MACRO_PATH`` to this location before starting Metview.

Extending the Macro Language
============================

It is possible to write your own C/C++/Fortran code and interface it with Metview Macro. 
In this way we can write functions in another language and call them directly from a macro, passing variables such as vectors, numbers and fieldsets between them. This is beyond the scope of this training course, but be aware that it is possible! It is currently documented in the `2014 Metview training course <tutorials>`, and examples are given in the solutions folder if you'd like to have a look.
