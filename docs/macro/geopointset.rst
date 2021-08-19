Geopointset Functions
========================
   
For an overview, please see Geopointset.

.. describe:: geopoints et ( geopointset  op geopointset )

   Operation between two geopointsets. op is one of the following:

   * \+ Addition
   * \- Subtraction
   * \* Multiplication
   * \/ Division
   * \^ Power
	
   The geopoints in the geopointsets returned by these boolean operators contain boolean values (containing only 1 where result is true, 0 where it is false):

   * \> Larger Than
   * \< Smaller Than
   * \>= Larger or Equal
   * \<= Smaller or Equal
   * \= Equal
   * \<> Not Equal


.. describe:: geopoints et ( geopointset  op number )
.. describe:: geopoints et ( number op geopointset )

   Operations between geopointsets and numbers. op is any of the operations defined above. See Geopointset for details of how the operations are performed 


.. describe:: geopoints et ( geopointset  op fieldset )
.. describe:: geopoints et ( fieldset op geopointset )

   Operations between geopointsets and fieldsets. op is any of the operations defined above. See Geopointset for details of how the operations are performed.


.. describe:: geopoints et ( geopointset  and geopointset )
.. describe:: geopoints et ( geopointset  or geopointset )
.. describe:: geopoints et ( not geopointset)

   Conjunction, Disjunction and Negation. See Geopointset for details of how the operations are performed.


.. describe:: geopoints et ( geopointset & geopointset & ... )
.. describe:: geopoints et ( nil & geopointset & ... )
.. describe:: geopoints et ( geopointset & nil )
.. describe:: geopoints et ( geopointset & geopoints )
.. describe:: geopoints et  merge ( geopointset,geopointset,... )

   Merge several geopointsets. The output is the concatenation of each geopointset. Merging with the value nil does nothing, and can be used to initialise when building a geopointset in a loop. A geopoints variable can also be merged into a geopointset.


.. describe:: geopoints geopointset[ number ]

   Returns the geopoints variable with the given index (first index is 1 in Macro, but 0 in Python).


.. describe:: geopoints et abs ( geopointset )
.. describe:: geopoints et asin ( geopointset )
.. describe:: geopoints et acos ( geopointset )
.. describe:: geopoints et atan ( geopointset )
.. describe:: geopoints et cos ( geopointset )
.. describe:: geopoints et exp ( geopointset )
.. describe:: geopoints et int ( geopointset )
.. describe:: number intbits ( geopointset,number )
.. describe:: number intbits ( geopointset,number,number )
.. describe:: geopoints et  log ( geopointset )
.. describe:: geopoints et log10 ( geopointset )
.. describe:: geopoints et neg ( geopointset )
.. describe:: geopoints et sgn ( geopointset )
.. describe:: geopoints et sin ( geopointset )
.. describe:: geopoints et sqrt ( geopointset )
.. describe:: geopoints et tan ( geopointset )

   Performs the given function on each component geopoints variable of the geopointset.


.. describe:: number count ( geopointset )

   Returns the number of geopoints variables in the given geopointset.


.. describe:: geopoints create_geo_set ( )

   Creates a new empty geopointset variable.


.. describe:: geopoints et filter ( geopointset, definition)

   From the given geopointset, this function extracts the set of geopoints variables whose metadata matches that given in the definition. See Geopoints for a description of how metadata is set and stored.
   As an example:

   .. code-block:: python

      gfilt = filter(gptset, (level:500, step:[6, 12, 18]))

   This will return a geopointset containing the geopoints variables whose metadata contains the key 'level' with a value of 500, AND the key 'step' with a value of 6 OR 12 OR 18.
   If the filter definition is empty, the original geopointset is returned. If it is non-empty and no geopoints matches its conditions, the filter function will return nil.