.. _macro_date_fn:

Date Functions
======================

.. describe:: number ( date - date )

   Returns the number of days between two dates.


.. describe::  date ( date + number )
.. describe::  date ( date - number )

   Adds/subtracts a number of days to/from a date. Returns a date.


.. describe:: number ( date op date )

   Comparison between two dates, returning either 0 (false) or 1 (true); op is one of the boolean operators below :

   * \> Larger Than
   * \< Smaller Than
   * \>= Larger or Equal
   * \<= Smaller or Equal
   * \= Equal
   * \<> Not Equal

   Smaller, greater, equal applied to dates refer to earlier, later, same dates.


.. describe:: date addmonths ( date, number )

   Returns a date whose value is the input date plus the number of months specified as the second argument.


.. describe:: date date ( number )

   Creates a date from a number. If the number is negative or zero, the parameter is the number of days from the current day. Otherwise, the number must represent a date in the yymmdd, yyyymmdd or Julian format. If the number is between 1721426 and 3182030 (representing the dates 0001-01-01 and 4000-01-01 respectively), it will be interpreted as a Julian date. The hour, minute and second information of the output date is lost (set to 0). Use hour() , minute() , second() to specify/restore it.


.. describe:: number day ( date )
.. describe:: number dow ( date )

   Returns respectively the day of the month / day of week (monday is 1, sunday is 7) part of a date.


.. describe:: number hour ( number )

   Converts a number of hours into a number of days which can then be added to a date, e.g. to provide hour information to a date created by the date() function. Equivalent to dividing by 24.


.. describe:: number hour ( date )

   Returns the hour part of a date.


.. describe:: number julday ( date )
.. describe:: number juldate ( date )

   Returns a date as Julian day and Julian date, respectively.


.. describe:: number minute ( number )

   Converts a number of minutes into a number of days which can then be added to a date, e.g. to provide minute information to a date created by the date() function. Equivalent to dividing by 1440.


.. describe:: number minute ( date )

   Returns the minute part of a date.


.. describe:: number month ( date )

   Returns the month part of a date.


.. describe:: date now ( )

   Creates a date from the current day and time.


.. describe:: number number ( date,string )

   Converts a date to a number according to the number date format specified as the second input argument. See the same entry in Functions and Operators on Numbers.  


.. describe:: number second ( number )

   Converts a number of seconds into a number of days which can then be added to a date, e.g. to provide seconds information to a date created by the date() function. Equivalent to dividing by 86400.


.. describe:: number second ( date )

   Returns the second part of a date.


.. describe:: string string ( date,string )

   Converts a date to a string according to the string date format specified as the second input argument. See the same entry in String Functions.


.. describe:: number year ( date )

   Returns the year part of a date.


.. describe:: number yymmdd ( date )

   Returns a date as a 6 digit number - discards hours, minutes and seconds.


.. describe:: number yyyymmdd ( date )

   Returns a date as an 8 digit number - discards hours, minutes and seconds.