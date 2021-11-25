.. _macro_date:

Dates in Macro
=================

.. note::

    The macro language defines dates as a type. A date contains information about the year, month, day, hour, minute and second. For a list and details of functions and operators on numbers, see :ref:`Date functions <macro_date_fn>`.


Creating
++++++++++++

Dates can be created as literals using the following syntax::

    yyyy-mm-dd
    yyyy-DDD

Where yyyy is a four digit year, mm is a two digit month, dd is a two digit day, and DDD is a three digit julian day (day ordinal in the year, the 1st of January being day 1). Two digit years (yy ) were valid but are now deprecated and illegal in some requests (e.g. MARS retrievals) and functions.

To introduce time of the day information, use the following syntax::

    HH:MM
    HH:MM:SS

where HH , MM and SS are respectively the hour, minute, and second, using two digits. This information is simply appended to the date specification, e.g.

.. code-block:: python

    my_date = 2000-01-04 09:50:24


Alternatively, you can create dates from numbers, using the function date() . This function works with negative (and zero) numbers or with 8 digit positive numbers.

The function date() interprets negative numbers as days before today and a zero value as today, e.g.:

.. code-block:: python

    today = date(0)
    yesterday = date(-1)


and it interprets an 8 digit number as yyyymmdd:

.. code-block:: python

    d1 = date(20000104)
    print("date is : ", d1)


This prints::

    date is : 2000-01-04 00:00:00


This clearly shows that the date() function creates dates where the hour, minute and second components are zero. To create a full date, use decimal dates or the functions hour() , minute() and second(). All following examples:

.. code-block:: python

    d = date(20000104.41)
    d = 2000-01-04 + 0.41
    d = 2000-01-04 + hour(9) + minute(50) + second(24)


assign the same date to variable d. When printed it gives::

    2000-01-04 09:50:24

    
To create a date variable holding both the current date and time, use the now() function:

.. code-block:: python

    d = now()
    print ("Now the date and time are ", d)


This gives:: 

    Now the data and time are 2005-06-20 16:40:31


Dates in Metview MARS requests
+++++++++++++++++++++++++++++++++++++++

The MARS language (for retrieval of data from ECMWF archives) automatically converts numbers to dates. This applies also to the Metview icons. For consistency, the macro language also accepts dates specified as numbers without the need to use the date() function :

.. code-block:: python

    r = retrieve(date : -1, ...)
    r = retrieve(date : 20000104, ...)


Users should bear in mind that when passing a date to Metview requests that interface with MARS, such as retrieve() , obsfilter() or read() , the hour, minute and second information are lost, as MARS can only handle integral dates. Thus the time has to be passed as an extra parameter :

.. code-block:: python

    d = 2000-09-07 12:00:00
    x = retrieve(
        date : d,
        time : hhmm(d),
        ...)


Converting dates to strings and numbers
+++++++++++++++++++++++++++++++++++++++++++++

General Conversion
------------------------

Dates can easily be converted to strings or numbers in Metview Macro. This conversion is handled by the functions::

    string(date, format)
    number(date, format)


They both take a date as the first argument and a format specifier as an optional second argument. The simplest conversion does not use the format specifier explicitly :

.. code-block:: python

    dd = date(20000104.41)
    ds = string(dd)
    dn = number(dd)
    print(type(dd), " : ", dd)
    print(type(ds), " : ", ds)
    print(type(dn), " : ", dn)


The print commands of this short piece of code yield::

    date : 2000-01-04 09:50:24
    string : 2000-01-04 09:50:24
    number : 20000104

Note that although the first two variables print identically their type is different - you cannot use the string variable ds in functions requiring a date variable. Note as well that the function number() returns an integer, discarding the time stamp. When you do not use the format specifier string as a second argument, a default one is implicitly used - this default is customisable, see Configuring Date Formats .
Converting date components

A date is a multidimensional variable in the sense of being composed of year, month, day, hour, minute, second. You may need to extract one (or more) of these components from a given date and to express these components in a variety of ways, e.g. you may need day of the month or day of the year, number of the month, month as a string, etc,.

Both the extraction of a date component and its expression in a variety of formats are handled by the string() and number() functions as well - their second argument (format specifier) which determines which component is extracted and in which format. E.g. if you need the year of a date as a four digit number :

    .. code-block:: python

        dd = date(20000104.41)
        yrn = number(dd, "yyyy")
        yrs = string(dd, "yyyy")
        print(type(yrn), " : ", yrn)
        print(type(yrs), " : ", yrs)


the format specification ("yyyy" in this case) is always a string given as the second argument to the number() or string() functions. The output of the above is::

    number : 2000
    string : 2000

A full list of the format specification strings is given below using the date of the above examples - 09h50m24s of the 04th of January 2000. The available format specification strings used in the string() and number() functions when applied to this date yield :

    * yy gives 00 (string) or 0 (number)
    * yyyy gives 2000
    * m gives 1
    * mm gives 01 (string) or 1 (number)
    * mmm gives Jan (string only)
    * mmmm gives January (string only)
    * d gives 1
    * dd gives 01 (string) or 1 (number)
    * ddd gives Tue (string only)
    * dddd gives Tuesday (string only)
    * D gives 4 (4th of January = julian day 4; leap years accounted for)
    * DDD gives 004 (string) or 4 (number)
    * H gives 9
    * HH gives 09 (string) or 9 (number)
    * M gives 50
    * MM gives 50
    * S gives 24
    * SS gives 24
    * Any other character is copied as such

All of the above are applicable in a conversion to string. Only those which produce a numerical format are valid for a conversion to number as indicated (e.g. m is applicable, mmm is not).

You can mix your own bits of text with the above string formats in order to print full dates in a reader friendly way. e.g.::

.. code-block:: python

    dd = date(20000104.41)
    sdate = string(dd, "dddd, ddth mmmm yyyy")
    print (sdate)


will output::

    Tuesday, 04th January 2000


Format specifiers can also be used to perform date calculations in a very efficient way :

.. code-block:: python

    today = date(0)
    last_day = date(string(today,"yyyy") & "1231")
    n = number(last_day,"D") - number(today,"D")
    print("number of days to the new year : ", n)


This outputs the number of days from today to the end of the current year - you set up the date of today and of the last day of the year as date variables, express them as Julian day numbers (using number(date, "D") ) and subtract them to obtain the required output. Note also that subtracting one date from another gives the number of days between the dates. The above example could be rewritten:

.. code-block:: python

    today = date(0)
    last_day = date(string(today,"yyyy") & "1231")
    print("number of days to the new year : ", last_day - today)


Configuring date formats
+++++++++++++++++++++++++++++

You have a degree of control over the date formats used by Metview Macro. You can:

* modify the default format specification string for conversion to string and number - the default format specification string for conversion to string is "yyyy-mm-dd HH-MM-SS" and for conversion to number is "yyyymmdd " (yielding a string "2000-01-04 09:50:24" and number 20000104 , respectively, for the example we have been using).
* replace the default English string date components (names of the week days and of months) - the default month names are January , February , ..., while the default week days' names are Monday , Tuesday , ...,. You can replace these by those in any language of your choice, e.g. Janvier , Janeiro , Enero (no accents though!).

Both the default format specifications and default string date components are specified in the Preferences option of the File menu in the menubar of any Metview desktop. When you select this option the Preferences editor is launched - simply type in the required default format specification and/or the month/weekday names in the language of your choice. When you save the result they will come into use immediately.

    
Loops with dates
++++++++++++++++++++++

It is possible to do loops with dates using a for loop, with increments of any number of days or of fractions of day :

.. code-block:: python

    # using default increment (1 day) 
    for d = 1997-09-01 to 1997-09-10 do
        (...)
    end for

    # using a non default increment of 2 days
    for d = 1997-09-01 to 1997-09-10 by 2 do
        (...)
    end for

    # using a non default increment of 6 hours
    for d = 1997-09-01 to 1997-09-10 by hour(6) do
        x = retrieve(
            date : yymmdd(d),
            time : hhmm(d),
            ...)
        (...)
    end for


Creating a list of months
++++++++++++++++++++++++++++++++++++++

If we want to create a list of dates such as::

    [19930601,19930701,19930801,
     19940601,19940701,19940801,
     .........,
     20160601,20160701,20160801]
    
where for each year we have the first day of the same three months, the following code snippet will create such a list:

.. code-block:: python

    d1 = 1993-06-01
    d2 = 2016-08-01
    d = d1
    datelist2 = []
    while d <= d2 do
        datelist2 = datelist2 & [d, addmonths(d, 1), addmonths(d, 2)]
        d = addmonths(d, 12)
    end while
    print(datelist2)




