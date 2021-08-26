.. _macro_string_fn:

String functions
======================

.. describe:: string ( string op string )

   Comparison between two strings, returning either 0 (false) or 1 (true); op is one of the boolean operators below:

   * \> Larger Than
   * \< Smaller Than
   * \>= Larger or Equal
   * \<= Smaller or Equal
   * = Equal
   * <> Not Equal

   Smaller, greater, equal applied to strings refer to lower, higher, same alphabetical order. The com­parison is case sensitive and is done using the ASCII code of each letter, hence the following expression is true (returns 1): ::

   "ABC" < "abc"

   Type man ascii at the UNIX prompt to know more about the ASCII encoding of characters.


.. describe:: string ( string & string & ... )
.. describe:: string ( string & number & ... )
.. describe:: string ( number & string & ... )
.. describe:: string ( string & date & ... )
.. describe:: string ( date & string & ... )

   Returns a string equal to the concatenation of strings or strings and numbers and/or dates. If con­catenating a date, the date is first converted to a string using the default string date format.



.. describe:: string ascii( number )

   Returns a string consisting of one character whose ASCII code has been provided as the single parameter to the function. For example:

   .. code-block:: python

      linefeed = ascii (10)


.. describe:: number length( string )

   This function returns the length of a string.
   
   .. code-block:: python
   
      word = "hello"
      print (word, " is ", length(word), "characters long")


.. describe:: string lowercase( string )

   Returns a lowercase copy of the input string.


.. describe:: number number( string )

   Converts a string into a number; if a string cannot be converted into a number, then  zero is returned. Example: 
   
   .. code-block:: python
   
      a = number('123.4')


.. describe:: list parse( string )
.. describe:: list parse( string,string )
.. describe:: list parse( string,string,string )

   This function splits the first input string at each occurrence of any of the field separators specified as the second string. It returns a list whose elements are the split tokens of the input string.

   Macro assigns a type to each of these components (i.e. number or string) unless a third parameter is supplied which gives the desired type to be returned; currently 'string' is the only allowed option. Space (" ") is the default separator when none is specified by the user, but any combination of characters can be specified as the set of separators.
   
   .. code-block:: python

      # specify a comma and space as separator
      s = "test1, 512.0, 498.0, 10.0"
      f = parse(s, ", ")
      # now access each retrieved element by indexing the list
      print ("result of ", f[1], " : ", (f[2]-f[3])/f[4])

   this prints: ::

      result of test1 : 1.4

   Supplying an empty string as the second parameter causes a complete list of the string's characters to be returned. For example:

   .. code-block:: python

      parse ("Metview", "")

   returns a list: ::

      [M,e,t,v,i,e,w]

   The parse() function is useful to parse text input when reading ASCII files within a macro program. Note that for ASCII data structured in columns (such as CSV files), Metview has some specific tools available - see ASCII Tables for more information.


.. describe:: string search (string,string)

   Searches the first string for the second string. The return value is the index of the first occurrence of the second string in the first. If the search fails, then it returns -1. Note that the comparison is case- sensitive.

   For example :

   .. code-block:: python
      
      filename = 'z_t2m_u_v_20060717.grib'
      t2m_index = search (filename, 't2m')

   returns the value 3.


.. describe:: string substring (string,number,number)

   Returns a substring of the input string. The second parameter specifies the index of the first charac­ter to be retrieved (1 is the first character). The third parameter specifies the index of the last char­acter to be retrieved. For example :

   .. code-block:: python
   
      substring ("Metview", 2, 4)

   returns the string "etv".


.. describe:: string string( date,string )

   Converts a date to a string according to the string date format specified as the second input argu­ment.

   If date = 1997-04-01 02:03:04 (say), the available string date formats result in:
 
   * yy gives 97
   * yyyy gives 1997
   * m gives 4
   * mm gives 04
   * mmm gives Apr
   * mmmm gives April
   * d gives 1
   * dd gives 01
   * ddd gives Tue
   * dddd gives Tuesday
   * D gives 91 (4th of April = julian day 91; 92 for a leap year).
   * DDD gives 091
   * H gives 2
   * HH gives 02
   * M gives 3
   * MM gives 03
   * S gives 4
   * SS gives 04

    Any other character is copied as such.


.. describe:: string uppercase( string )

   Returns an uppercase copy of the input string.