.. _version_4.0_updates:

Version 4.0 Updates
///////////////////

Metview

Exported on Jan 24, 2022

Table of Contents
=================

1 User Version 4.0.8 `3 <#user-version-4.0.8>`__

2 Test Version 4.0.8 `4 <#test-version-4.0.8>`__

3 Test Version 4.0.7 `5 <#test-version-4.0.7>`__

4 Export Version 4.0.6 `6 <#export-version-4.0.6>`__

5 User Version 4.0.6 `7 <#user-version-4.0.6>`__

6 Test Version 4.0.6 `8 <#test-version-4.0.6>`__

7 User Version 4.0.5 `9 <#user-version-4.0.5>`__

8 Test Version 4.0.5 `10 <#test-version-4.0.5>`__

9 User Version 4.0.4 `11 <#user-version-4.0.4>`__

10 Export Version 4.0.3 `12 <#export-version-4.0.3>`__

11 Test Version 4.0.3 `13 <#test-version-4.0.3>`__

12 Test Version 4.0.2 `14 <#test-version-4.0.2>`__

13 User Version 4.0.1 `17 <#user-version-4.0.1>`__

14 Test Version 4.0.1 `18 <#test-version-4.0.1>`__

15 Version 4.0.0 `19 <#version-4.0.0>`__

User Version 4.0.8
==================

**Upgrade 2011-10-05 (all platforms)**

-  Version 4.0.8 became *User Version* at ECMWF

Test Version 4.0.8
==================

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2011-09-13**
(all platforms)

-  Installed as *metview4_new*

-  Rebuilt with latest Mars client code, GRIB_API 1.9.10 and emoslib
   000390

Test Version 4.0.7
==================

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2011-06-20**
(Linux desktops, lxab cluster, ecgate)

-  Installed as *metview4_new*

-  Macro functions pressure(), thickness(), vertint() and univertint()
   updated to work with GRIB 2 data

-  Built with Magics++ 2.12.10

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-07-14**

-  New macro library function mvl_geopotential_on_ml() for computing
   geopotential on model levels. Example usage:

-  

.. note::

 r = (date: -\ 1, time: 12, levtype: "ml", grid: [1.5,1.5])    
                                                                       
 T = retrieve(r,levelist: [1,"to",91],param: "t")                  
                                                                       
 q = retrieve(r,levelist: [1,"to",91],param: "q")                  
                                                                       
 zs = retrieve(r,levelist: 1,param: "z")                           
                                                                       
 lnsp = retrieve(r,levelist: 1,param: "lnsp")                      
                                                                       
 z_ml = mvl_geopotential_on_ml(T, q, lnsp, zs)                     

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-07-18**
(ecgate only)

-  Rebuilt Qt libraries with antialiasing support. This results in a
   much nicer user interface for all Qt-based modules in Metview 4 (e.g.
   the data examiners, the Display Window and the Macro editor).

Export Version 4.0.6
====================

**External release 2011-06-17**

-  Version 4.0.6-export became available

User Version 4.0.6
==================

**Upgrade 2011-06-06 (all platforms)**

-  Version 4.0.6 became *User Version* at ECMWF

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-06-09**

-  New macro functions sum(vector) and mean(vector). Return either the
   sum or the mean of all non-missing values in their input vectors. If
   all values are missing, then nil is returned.

-  Fix in set_gridvals() function when fieldset contains multiple fields

-  Note: these updates were applied directly to version 4.0.6 (currently
   *metview4* and *metview4_new*)

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-06-14**

-  | List functions now available include unary operators such as abs(),
   | cos(), etc and binary operators such as +, -, >, min, etc. These
     are the
   | same set of basic operators and functions that are available for
     fieldsets,
   | geopoints, numbers and vectors. Binary operators between two lists
   | will fail if the lists contain different numbers of elements;
     otherwise,
   | the result will be a new list, where each element is the result of
   | applying the operator to each of the corresponding elements in the
   | input lists. List elements can be of any type, as long as it is
     legal
   | to perform the operation on elements of that type.
   | Lists are not recommended for computations with many (hundreds) of
     values;
   | for this, the vector data type is significantly more efficient.

   Examples of the new list operations:

+-----------------------------------------------------------------------+
| a = [1,2,3]                                                           |
|                                                                       |
| b = [4,1,6]                                                           |
|                                                                       |
| c = [|1,2,3|, \|4,5,6|, [7,8,9]] # vector,vector,list                 |
|                                                                       |
| d = [10, 20, 30]                                                      |
|                                                                       |
| print (a + b) : output is [5,3,9]                                     |
|                                                                       |
| print (max(a,b)) : output is [4,2,6]                                  |
|                                                                       |
| print (max(a,2)) : output is [2,2,3]                                  |
|                                                                       |
| print (a - 5) : output is [-4,-3,-2]                                  |
|                                                                       |
| print (sqrt(b)) : output is [2,1,2.44948974278]                       |
|                                                                       |
| print (c + 10) : output is [|11,12,13|,|14,15,16|,[17,18,19]]         |
|                                                                       |
| print (c + d) : output is [|11,12,13|,|24,25,26|,[37,38,39]]          |
+=======================================================================+
+-----------------------------------------------------------------------+

| The complete list of operators is: +,-,/,*,^,>,<,>=,<=,=,<>,and,or,
| mod,div,max,min,neg,not,sgn,int,log10,log,exp,sqrt,sin,cos,tan,asin,acos,
| atan,abs.

`scroll-bookmark-1 <#user-version-4.0.8>`__

Test Version 4.0.6
==================

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2011-05-25**
(Linux desktops, lxab cluster, ecgate)

-  Installed as *metview4_new*

-  Uses latest Mars client code, GRIB_API 1.9.10 and emoslib 000382

-  Built with Magics++ 2.12.8

-  Small updates to the WMS client module

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-06-03**

-  Rebuilt ODB modules using latest ODB libraries (CY37R3.001 and 0.8.5)

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-06-06**

-  Added ODB to the command-line version of the data examiners, invoked
   with:

-  metview4 -e odb /path/to/ODB-database

User Version 4.0.5
==================

**Upgrade 2011-05-16 (all platforms)**

-  Version 4.0.5 became *User Version* at ECMWF

Test Version 4.0.5
==================

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2011-05-10**
(Linux desktops, lxab cluster, ecgate)

-  Installed as *metview4_new*

-  Uses latest Mars client code, GRIB_API 1.9.10 and emoslib 000382

-  Built with Magics++ 2.12.7

-  Fixed issue in Potential Temperature module which affected
   computations involving multiple fields

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-05-12**

-  New 'standalone' data examiner mode - to examine a data GRIB or BUFR
   data file, use the command syntax:

-  metview4 -e grib /path/to/grib/file

-  metview4 -e bufr /path/to/bufr/file

User Version 4.0.4
==================

**Upgrade 2011-04-06 (all platforms)**

-  Version 4.0.4 became *User Version* at ECMWF

Export Version 4.0.3
====================

**External release 2011-03-24**

-  Version 4.0.3-export became available

Test Version 4.0.3
==================

**Introduced 2011-03-24** (Linux desktops)

-  Rebuilt with latest Mars client, GRIB_API 1.9.9 and emoslib 000381
   for GRIB 2 transformation / interpolation.

-  Menory leak fixed in macro function datainfo().

Test Version 4.0.2
==================

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2010-12-08**
(Linux desktops, lxab cluster ; ecgate 2011-01-06)

-  Installed as *metview4_new*

-  Uses latest Mars client code

-  Uses a snapshot version of GRIB_API 1.9.7

**Update 2011-01-06**\ (Linux desktops, lxab cluster, ecgate)

-  Large expansion of the *vector* macro data type:

-  | In functions such as gridvals() which return a large list of
     numbers, the
   | use of the vector data type is much more efficient. As the
     accessing of
   | vector elements is identical to the accessing of list elements, it
     was
   | decided to change a number of macro functions which currently
     return
   | a list of numbers to return instead a vector. This also prompted a
   | development of the functions available on vectors.

   | **New vector functionality**
   | Vector functions now available include unary operators such as
     abs(),
   | cos(), etc and binary operators such as +, -, >, min, etc. These
     are the
   | same set of basic operators and functions that are available for
     fieldsets,
   | geopoints and numbers.

   | **New macro functions**
   | The following are new macro functions:

   -  | set_gridvals(fieldset, vector) - takes a vector or a list of
        vectors;
      | if a single vector, then it is applied to all fields; if a list
        of vectors, then there must be the same number of vectors as
        there are fields.

   -  gridlats(fieldset), gridlons(fieldset) - return vectors.

   -  tolist(vector) - convert a vector to a list of numbers (missing
      values become nil)

..

   | **Revised functions**
   | In addition, the following existing functions were modified in
     order
   | to return or accept vectors instead of lists:
   | gridvals(), grib_get_long_array(), grib_get_double_array(),
     average_ew(), average_ns(), level(geopoints), latitude(geopoints),
     longitude(geopoints), value(geopoints), value2(geopoints),
     value(odb).The following functions on geopoints now accept either a
     list of
   | numbers or a vector as input:
   | set_latitude(), set_longitude(), set_level(), set_date(),
     set_time(),
   | set_value(), set_value2().

   | **Missing values**
   | New functions are available for converting missing values:
   | bitmap(vector,number) and nobitmap(vector,number).
   | A new global variable, vector_missing_value, now exists for the
     purpose
   | of testing vector elements. Missing values derived from fieldsets
     and
   | geopoints variables are honoured.

   | **Concatenation**
   | Can concatenate 2 vectors, e.g. c = a & b
   | Can append a number to a vector, e.g. v = v & 7

   | **Building a vector**
   | The most efficient way to build a vector is to pre-allocate and
     then fill:

+-----------------------------------------------------------------------+
|    a = vector(num_elements)                                           |
|                                                                       |
|    **for** i = 1 to num_elements **do**                               |
|                                                                       |
|    a[i] = i                                                           |
|                                                                       |
|    **end** forSimple vector definition:                               |
|                                                                       |
|    a = \|1, 2, 3, 4, 5\|                                              |
+=======================================================================+
+-----------------------------------------------------------------------+

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-01-17**
(Linux desktops, lxab cluster, ecgate)

-  More expansion of the *vector* macro data type:

-  Macro function values(netcdf) now returns a vector.

-  The full set of ways to access a subset of a list was added to the
   vector data type in Macro, ie vector[i], vector[first, last],
   vector[first, last, step].

-  | Also, a additional fourth parameter is now accepted (for vectors
     only): if supplied, it specifies how many elements to extract from
     the current step. For example, while vector[1, 20, 5] will create a
     new vector with elements from these indexes: 1,6,11,16,
   | vector[1, 20, 5, 2] will create a new vector with elements from
     these indexes: 1,2,6,7,11,12,16,17. If a vector is actually holding
     data from a rectangular structure, this form could be used to
     extract a 'sub-area'.

-  Additionally, it is now possible to assign a vector to an indexed
   position in another vector, for example: v[4] = \|99,99,99|. In this
   example, elements 4, 5 and 6 of v will be replaced.

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-01-31**
(Linux desktops, lxab cluster, ecgate)

-  ODB examiner has a new tab which enables the inspection of data
   values

-  Improved performance of scrolling large message lists in GRIB and
   BUFR examiners

-  Small fixes in the Macro editor

-  Rebuilt with emoslib 000377, new GRIB_API 1.9.7 and Mars code for
   GRIB interpolation

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-02-07**
(Linux desktops, lxab cluster, ecgate)

-  Updated with the latest emoslib 000377 and Mars code

-  WMS client editor redesigned and improved in 'plain mode'

-  Macro/fortran interface issue resolved for 64-bit systems

-  Magics errors now being reported when run in batch mode

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-02-09**
(Linux desktops, lxab cluster, ecgate)

-  | New macro function: fieldset indexes(fieldset, vector)
   | Given a fieldset and a vector of target values, this function finds
   | for each gridpoint the indexes of the nearest values in the target.
   | Indexes are zero-based and will always have a minimum value of zero
   | and a maximum value equal to the index of the last element of the
   | target vector. A value lying between two values in the vector will
   | use the index of the nearest value; if equidistant, then the higher
   | value is used.
   | The input vector MUST be sorted in ascending order.
   | Example: if these are our inputs:

   | GRIB: 10,20,30,40 VECTOR: \| 5,10,15,20,25,30 \|
   | 15,25,35,45
   | 8, 4,20,11

   then our output would be a new GRIB, with values equal to the input
   values' positions in the input vector:

   | GRIB: 1,3,5,5
   | 2,4,5,5
   | 1,0,3,1

-  Macro function nearest_gridpoint()now accepts vector locations.

   | New mode:
   | vector or list nearest_gridpoint(fieldset, vector, vector)
   | Updated function description:
   | Returns the value of the nearest point to a given location in each
     field
   | of a fieldset. If a list is given, it must contain two numbers -
   | latitude and longitude. If two numbers or vectors are given, the
     first
   | is the latitude(s), the second the longitude(s).The field must be a
     lat-long
   | field. If the fieldset has only one field, a number or vector is
     returned;
   | otherwise a list is returned. Where it is not possible to generate
     a sensible
   | value due to lack of valid data in the fieldset, a 'nil' is
     returned in
   | the case of a single coordinate, or vector_missing_value in the
     case of
   | a vector.
   | A performance test which extracted 20000 points from a set of 6
     fields
   | showed that the vector version took 0.27u/0.01s CPU, whereas
     performing
   | a loop to extract the same points took 46.02u/1.63s CPU.

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Update 2011-03-01**
(Linux desktops, lxab cluster; *ecgate 2011-03-02* )

-  New macro functions: minvalue(vector) and maxvalue(vector). Both
   functions return a number; if there are no valid values in the input
   vector, then nil is returned.

-  Passing vector arguments to inline C/Fortran code in a macro is now
   much more efficient for large data sets.

-  The Reprojection module has been re-introduced (the module was never
   documented - please ask the Visualisation Section for more
   information on it).

-  The resulting ODB of the ODB/SQL query in the ODB Manager icon can
   now be examined and saved.

-  Certain icons have a "save" item in their context menu. This brings
   up a file selection dialog of which initial directory is now set to
   the folder of the icon.

-  The WMS Client can now be used in macro via the wmsclient() macro
   command.

-  Rebuilt with GRIB_API 1.9.8 and the latest Mars client code.

`scroll-bookmark-1 <#user-version-4.0.8>`__

User Version 4.0.1
==================

**Upgrade 2010-12-07 (all platforms)**

-  Version 4.0.1 became *User Version* at ECMWF

Test Version 4.0.1
==================

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2010-12-06**
(Linux desktops, lxab cluster and ecgate)

-  Installed as *metview4_new*

-  Export version available

-  Display Window has a new section to display meta-data about a layer;
   currently only used for WMS layers

-  Various fixes in WMS client

-  New macro function grib_set_string()

-  Added 'Insert Code Template' functionality to Macro editor

-  Macro editor can now be used to edit and run shell commands

-  DivRot module been partially re-written, and now has a new mode,
   UVWIND, macro function uvwind(), for more efficient computation of
   U/V from VO/D

-  Improvements to ODB interface

-  Various fixes

-  Some small compilation issues fixed

Version 4.0.0
=============

`scroll-bookmark-1 <#user-version-4.0.8>`__\ **\ Introduced 2010-09-27**
(Linux desktops, lxab cluster and ecgate)

-  First official release of Metview 4

-  Export version available

-  This version is for evaluation, and we value any feedback

-  It is not intended for operational use
