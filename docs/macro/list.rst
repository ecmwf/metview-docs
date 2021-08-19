List Functions
======================
   
.. note::

   If using a list for holding a large set of numbers, consider using a vector instead, which will be much more efficient for this purpose.

.. describe:: list ( list op list )

   Operation between two lists. op is one of the operators below :

   * \+ Addition
   * \- Subtraction
   * \* Multiplication
   * / Division
   * ^ Power

   The boolean operators are :

   * > Larger Than
   * < Smaller Than
   * >= Larger or Equal
   * <= Smaller or Equal
   * = Equal
   * <> Not Equal
 

.. describe:: list ( list op number )
.. describe:: list ( number op list )

   Operations between lists and numbers. op is any of the operations defined above.


.. describe:: list ( list and list )
.. describe:: list ( list or list )
.. describe:: list ( not list )

   Conjunction, Disjunction and Negation.


.. describe:: list ( list and number ) list ( number or list )

   Boolean operations between lists and numbers.


.. describe:: any list[number]
.. describe:: list list[number,number]
.. describe:: list list[number,number,number]

   Apply the [] to a list to return element(s) from that list. Note that array indices start at 1:

   .. code-block:: python

         mylist[n] returns the nth element of mylist

         mylist[n,m] returns the nth to the mth elements of mylist

         mylist[n,m,i] returns every ith of the nth to the mth elements of mylist

         # copies elements 1, 5, 9, 13, 17 of x into y
         Y = X[1,20,4]


.. describe:: list list[vector]

   Extract a selection of elements from a list. The vector supplied as the argument provides the set of indices to be used. For example:   

   .. code-block:: python

         # copies elements 2, 1, 3 from x to y
         i = |2,1,3|
         y = x[i]
 

.. describe:: number ( any in list )
.. describe:: number ( any not in list )

   Tests whether a value is in a list or not. Returns a 0 (false) or 1 (true)


.. describe:: list ( list & list )

   Concatenate two lists. Note that to add a single element to a list, it must first be converted into a single-element list, for example:

   .. code-block:: python
   
         mylist = mylist & [23]

.. describe:: list abs( list )
.. describe:: list acos( list )
.. describe:: list asin( list )
.. describe:: list atan( list )
.. describe:: list cos( list )
.. describe:: list exp( list )
.. describe:: list int( list )
.. describe:: list log( list )
.. describe:: list log10( list )
.. describe:: list neg( list )
.. describe:: list sgn( list )
.. describe:: list sin( list )
.. describe:: list sqrt( list )
.. describe:: list tan( list )
.. describe:: list div( list,list )
.. describe:: list max( list,list )
.. describe:: list min( list,list )
.. describe:: list max( list,number )
.. describe:: list min( list,number )
.. describe:: list mod( list,list )

   Computational functions – the function is applied to each element in the list; for functions that take two lists as arguments, both lists must have the same number of elements. For example, calling sin on a list of numbers will internally call sin(number) for each element of the input list, putting the results into a new output list. This helps avoid the need to write loops to process data in some circumstances. Note that for large data sets (1000s of values), the vector data type is more efficient for numeric computations.

   To take sin as an example, the following two pieces of code are exactly equivalent:

   .. code-block:: python

         b = [1, 5, 9, geopoints, fieldset]
         a = sin(b)                # version 1

         a = nil                   # version 2
         for i = 1 to count(b) do  # version 2
         a = a & [sin(b[i])]   # version 2
         end for                   # version 2

   This shows that the types of the elements in the input lists are not restricted – a list can contain many different data types (e.g. [number, vector, geopoints]) and as long as the requested function is valid for each type, the correct result will be returned. If the requested operation is illegal for that element (e.g. sin(['hello'])) then it will fail on that element. See the descriptions of these functions for the relevant data types.


.. describe:: number count( list )

   Returns the number of elements in a list.


.. describe:: number or list find( list,any )
.. describe:: number or list find( list,any,string )

   Searches the given list for an item and returns the index of the first occurrence of it. If an optional third argument is given as the string 'all', then a list of the indexes of all occurrences of the item is returned. In both cases, if the item is not contained in the list, nil is returned.


.. describe:: list list( any,any,...)

   Returns a list built from its arguments.


.. describe:: list sort( list )

   Sorts a list in ascending order.


.. describe:: list sort( list,string )

   Sorts a list given a comparison, expressed as a string : Ascending "<", descending ">"; you may specify the sorting criterion in a comparison function:

   .. code-block:: python

      function compare(a,b)
      return a < b
      end compare 

      number s = [1,5,3,9,0,4,6,7,8,2]

      print (sort(numbers, ">"))       # prints in decreasing order
      print (sort(numbers, "compare")) # prints in ascending order

   Note that it is not valid to sort a list which contains more than one type of data element.


.. describe:: list sort_indices( list )
.. describe:: list sort_indices( list,string )

   Sorts a list and returns the sorted indices. The default behaviour is to sort in ascending order unless an alternative comparison function is provided. See example under sort_and_indices() to see how this function works.


.. describe:: list sort_and_indices( list)
.. describe:: list sort_and_indices( list,string )

   Sorts a list and returns a list of pairs of list items and their corresponding indices in the original list. The default behaviour is to sort in ascending order unless an alternative comparison function is provided. The following example illustrates sort_indices() and sort_and_indices():

   .. code-block:: python

      original = [10, 12, 9, 7, 6]
      comparison = "<"

      sorted_list = sort (original, comparison)
      sorted_indices = sort_indices (original, comparison)
      sorted_both = sort_and_indices (original, comparison)

      print ('Original list : ', original)
      print ('Sorted list : ', sorted_list)
      print ('Sorted indices : ', sorted_indices)
      print ('Sort and indices : ', sorted_both)

   Note that in this example it is not necessary to provide a comparison operator, as "<" is the default anyway. The output is as follows:

   .. code-block:: python

      Original list    : [10,12,9,7,6]
      Sorted list      : [6,7,9,10,12]
      Sorted indices   : [5,4,3,1,2]
      Sort and indices : [[6,5],[7,4],[9,3],[10,1],[12,2]]


.. describe:: list unique( list )

   Returns a list of the unique elements in the input list.


.. describe:: vector vector( list )

   Returns a vector containing the numeric elements of the input list. Any nil list elements are converted to vector_missing_value. Any other non-numeric elements will cause an error. If the input list is empty, the function returns nil.
