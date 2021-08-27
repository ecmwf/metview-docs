.. _macro_number_fn:

Number Macro functions
===========================

   No distinction is made between integer or real numbers. All numbers are internally coded as double precision floating point reals.


.. describe:: number ( number op number )

   Operation between two numbers. op is one of the operators below. These either return a number:

   * \+ Addition
   * \- Subtraction
   * \* Multiplication
   * / Division
   * ^ Power
	
   or return 1 (result is true) or 0 (result is false):

   * > Larger Than
   * < Smaller Than
   * >= Larger or Equal
   * <= Smaller or Equal
   * = Equal
   * <> Not Equal


.. describe:: number ( number and number )
.. describe:: number ( number or number )
.. describe:: number ( not number )

   Conjunction, Disjunction and Negation. Boolean operators consider all null values to be false and all non null values to be true. Result is either 1 or 0.


.. describe:: number abs ( number )

   Returns absolute value of a number.


.. describe:: number acos ( number )
.. describe:: number asin ( number )
.. describe:: number atan ( number )

   Return the arc trigonometric function of a number. Result is in radians.


.. describe:: number cos ( number )

   Return the cosine of a number (angle in radians).


.. describe:: number exp ( number )

   Returns the exponential of a number


.. describe:: number int ( number )

   Returns integer part of a number (no rounding, e.g. int(1.999)=1.0 )


.. describe:: number intbits ( number,number )
.. describe:: number intbits ( number,number,number )

   Takes the integer part of the first number and extracts a specified bit (or number of bits if a third number parameter is specified), where bit number 1 is the least significant bit (lsb). A single bit will always be returned as 1 or 0, regardless of its position in the integer. A group of bits will be treated as if the first bit is the least significant bit of the result A few examples illustrate.

   To extract the 1st, 2nd and 3rd bits from a number separately:

   .. code-block:: python

         n = 6 # in bit-form, this is `00000110' with the lsb at the right
         flag = intbits (n, 1) # flag is now 0
         flag = intbits (n, 2) # flag is now 1
         flag = intbits (n, 3) # flag is now 1

         To extract the 1st and 2nd bits together to make a single number:
         flag = intbits (n, 1, 2) # flag is now 2

         To extract the 2nd and 3rd bits together to make a single number:
         flag = intbits (n, 2, 2) # flag is now 3

         To extract the 3rd and 4th bits together to make a single number:
         flag = intbits (n, 3, 2) # flag is now 1

   The number of bits available depends on the machine architecture and Metview's compilation options, but at the time of writing it should be either 32 or 64.


.. describe:: number log ( number )

   Returns the natural logarithm of a number.


.. describe:: number log10 ( number )

   Returns the logarithm base 10 of a number.


.. describe:: number max ( number,number,... )
.. describe:: number min ( number,number,... )

   Returns maximum / minimum of the input values.


.. describe:: number mod ( number,number )


   Returns the remainder of the division of the first value by the second. If the second number is larger than the first, it returns the integer part of the first number. Note that only the integer parts of the inputs are considered in the calculation, meaning that a second parameter of 0.5 would cause a division by zero.


.. describe:: number neg ( number )

   Returns the negative of a number. The same as (- number).


.. describe:: number number ( date,string )

   Converts a date to a number according to the number date format specified as the second input argument.

   If date = 1997-04-01 02:03:04 (say), the available number date formats result in: ::

      yy gives 97
      yyyy gives 1997
      m or mm give 4
      d or dd give 1
      D or DDD give 91 (4th of April is the 91st day of the year).
      H or HH give 2
      M or MM give 3
      S or SS gives 4


.. describe:: number precision ( )
.. describe:: number precision ( number )

   Sets the printing precision for floating point values, i.e. how many significant digits are used when printing or writing to a file. The value returned is the current precision value. Called with no arguments, it resets the precision to its default value, i.e. 12. Examples of printed output for print(1234.56789): ::

      precision( 12 ) gives 1234.56789
      precision( 6 ) gives 1234.57
      precision( 4 ) gives 1235
      precision( 2 ) gives 1.2e+03


.. describe:: number random ()

   Returns a randomly selected non-negative double-precision floating-point value. The return values are uniformly distributed between [0.0, 1.0). There is no need to "seed" this random function, as this is done automatically the first time it is called.


.. describe:: number round ( number,number )

   Rounds off spurious decimals in a value. The first number is the value to be rounded, the second is the number of decimal places to leave. Examples of values returned by round(v,n) for v = 1234.56789: ::

      round( v, 1 ) gives 1234.6
      round( v, 3 ) gives 1234.568
      round( v, -2 ) gives 1200


.. describe:: number sgn ( number )

   Returns the sign of a number as a number : -1 for negative values, 1 for positive and 0 for null values.


.. describe:: number sin ( number )

   Return the sine of a number (angle in radians).


.. describe:: number sqrt ( number )

   Returns the square root of a number.


.. describe:: string string ( number )

   Returns the string equivalent of a number.


.. describe:: number sum ( number,number,... )

   Returns the sum of the input values.


.. describe:: number tan ( number )

   Return the tangent of a number (angle in radians).