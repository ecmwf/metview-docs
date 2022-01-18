.. _missing_values_and_masks:

Missing Values and Masks
########################

**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - ZIP Archive `missing values.tar.gz <https://confluence.ecmwf.int/download/attachments/45758672/missing values.tar.gz?api=v2>`_
    - Sep 16, 2016 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_
    
Overview
********

.. image:: /_static/missing_values_and_masks/missing-values.png

Fields and observations can often contain missing values - it can be important to understand the implications of these, and also how to use them to remove unwanted data points. Using a mask of missing values can enable Metview to perform computations on a specific subset of points.

Computing the mean surface temperature over land
************************************************

.. image:: /_static/missing_values_and_masks/lsm-raw.png

.. image:: /_static/missing_values_and_masks/lsm-clean.png

As an example, we will use a land-sea mask field as the basis of performing a computation on only the land points, excluding all sea points.

Visualise the supplied *land_sea_mask.grib* icon using the *grid_shade* icon. 
This *Contouring* icon is set up to shade the grid points exactly as they are in the data with no interpolation. 
To help illustrate what's going on, we've chosen low-resolution fields - this one is 4x4 degrees. 
The values are 0 over the sea, 1 over the land and somewhere between 0 and 1 on points which are close to both sea and land. 
Before we can use this field as a mask, we must do something with those "in-between" points and decide whether they count as land or sea! 
Let's say that a value of 0.5 or more is land.

Create a new Macro icon and rename it land_points. Type the following code:

.. code-block:: python
  
  lsm = read('land_sea_mask.grib')
  lsm = (lsm >= 0.5)
  
The variable ``lsm`` has been replaced with a stricter mask. 
Applying boolean operators such as < and > returns a result consisting entirely of 1s (where the grid values pass the test) and 0s (where the grid values fail the test). Plot the result with *grid_shade* to confirm this change. 
The plots above show the 'raw' land-sea field and then the 'cleaned' one.

Now we want to read *t2m.grib* - this contains 2 metre temperature analysis data from 5 days. 
Add a line of code to read this file into a new variable ``t2m``. 
Compute the mean value of the points using the ``integrate()`` function. 
It will return a list of values - the mean value from each field.

We now want to 'deactivate' the points where the land-sea mask is 0 (the sea points).

.. note::

  When performing computations between two fields, they must be on the same grid, with the same number of points. 
  If this is not the case, you will need to use interpolation to transform one field onto the other's grid. 
  See :ref:`Processing Data <processing_data>`.

One way to do this could be to simply multiply the temperature field by the land-sea mask field - this would preserve the land points by simply multiplying them by 1, but would convert the other points to 0. 
In some cases this might be what we want, but not here for two reasons:

* zero might be a valid value for many meteorological parameters, so it can't be used as a mask

* if we want to compute the mean over the field, the sea points will still be used and will simply result in a lower mean because they are all zero

So we will convert the zeros in the ``lsm`` fieldset to *missing values* using the ``bitmap()`` and ``nobitmap()`` functions, whose `documentation <https://confluence.ecmwf.int/display/METV/Fieldset+Functions>`_ is reproduced here:

.. code-block:: python
  
  fieldset bitmap (fieldset,number)
  fieldset bitmap (fieldset,fieldset)
  
Returns a copy of the input fieldset (first argument) with zero or more of its values replaced with grib missing value indicators. 
If the second argument is a number, then any value equal to that number in the input fieldset is replaced with the missing value indicator. 
If the second argument is another fieldset with the same number of fields as the first fieldset, then the result takes the arrangement of missing values from the second fieldset. 
If the second argument is another fieldset with one field, the arrangement of missing values from that field are copied into all fields of the output fieldset. See also ``nobitmap``.
  
.. code-block:: python

  fieldset nobitmap ( fieldset,number )
  
Returns a copy of the input fieldset (first argument) with all of its missing values replaced with the number specified by the second argument. 
See also ``bitmap``.

Try the following steps:

* modify the ``lsm`` variable to have missing values where there are currently zeros (visualise to verify)

* copy the missing value mask from ``lsm`` to ``t2m`` (plot ``t2m`` to verify)

* compute and print the mean values of the fields in ``t2m`` - use the function ``integrate()``

* this result is now the means of only the land points

The code should in fact only be a few lines. 
All of Metview's functions will respect missing values and treat them properly.

.. image:: /_static/missing_values_and_masks/t2m-masked.png

As an experiment, try setting *all* the values to missing values (just change the threshold in the expression "(``lsm >= 0.5)`` ") to something silly. 
The integrate() function should now return nil as its result. 
This is a special variable in Macro, and trying to do anything with it (e.g. multiplying it by a number) will result in an error. 
To make your code bullet-proof, you can test for it with something like this:

.. code-block:: python
  
  result = integrate(....)
  if result = nil then
    print('No valid data points')
  else
    print('Mean value: ', result)
  end if

Missing values in geopoints
***************************

Make a copy of your macro and this time convert the masked ``t2m`` field to geopoints:
  
.. code-block:: python
  
  geo = grib_to_geo(data: t2m)
  return geo

If you examine the result, you will see that there are missing value indicators in much of the file. 
Metview will respect these, and computations performed on the geopoints will exclude these points. 
In fact, to make things more efficient, you can remove these points entirely from the geopoints. 
Try the following:

.. code-block:: python
  
  geo = grib_to_geo(data: t2m)
  print(count(geo))
  geo = remove_missing_values(geo)
  print(count(geo))

Extra Work
**********

Computing different means
=========================

Try computing the mean value over the sea points. 
This should be just one small change to your code.
Compute the mean value over a sub-area rather than over the whole globe. Note that the ``integrate()`` function can do this:

.. code-block:: python
  
  europe = [75,-12.5,35,42.5]
  x = integrate(field,europe) 

There is another function, ``average()``, to compute the mean value of a field. 
Find its documentation to see what the difference is. 
How different is the result?

Cheat: the ``integrate()`` function can accept an additional argument of a field of 1s and 0s, and will only compute the mean value where this field has 1s. 
Using this functionality, you can avoid using the bitmap functions altogether, at least in this particular computation! See `Fieldset Functions <https://confluence.ecmwf.int/display/METV/Fieldset+Functions>`_.

The Land-sea mask
=================

Write a line of macro code which will compute the number of land points in the ``lsm`` variable. 
There are two methods:

* ``accumulate()`` - adds all the values in a field to return a single number; this should do the job, since the values are 1 over land and 0 over sea

* ``datainfo()`` - returns information about the number of points and missing values in the field
