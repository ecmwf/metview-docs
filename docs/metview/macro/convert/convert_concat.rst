Adjust concatenations
=============================

.. note::
   
    The Macro to Python converter is available from Metview version 5.22.0

In Macro the generic **concatenation** operator is ``&`` (ampersand), which can be used for strings, lists, fieldsets and many other built-in types in the same way. Conversion of these operator calls to Python would require run-time information, which the converter does not posses since it does not actually runs the Macro. To overcome this difficulty the calls to ``&`` are replaced by calls to Metview's built in :func:`mv.compat.concat` method in the resulting Python script. 

.. note::
   
   :func:`mv.compat.concat` is available from Metview Python version 1.16.0

The following table contains some concatenation examples.


.. list-table:: Replacing ``&`` with :func:`mv.compat.concat` calls in the generated Python code
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
   * -
       .. code-block:: python
        
          # string
          c = a & "my_text"

          # list
          a = nil
          a = a & [12]

          # vector
          v = a & |1,2,3|

          # fieldset, geopoints, bufr
          f = g1 & g2
     -
       .. code-block:: python
        
          # string
          c = mv.compat.concat(a, "my_text")

          # list
          a = []
          a = mv.compat.concat(a, 12)

          # numpy array
          v = mv.compat.concat(a, np.array([1,2,3]))

          # fieldset, geopoints, bufr
          f = mv.compat.concat(g1, g2)

While this results in a correctly working code it must be only regarded as a **temporary solution**. Ideally you should check your code and **replace** all :func:`mv.compat.concat` calls with the proper concatenation used for a given type in Python.

The following table can serve you as a guide to properly convert the ``&`` operator calls in Macro to Python:  

.. list-table:: Resolving the Macro ``&`` operator calls in Python
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
   * -
       .. code-block:: python
        
          # string
          c = a & "my_text"

          # list
          a = nil
          a = a & [12]

          # vector
          v = a & |1,2,3|

          # fieldset, geopoints, bufr
          f = g1 & g2
     -
       .. code-block:: python
        
          # string
          c = a + "my_text"

          # list
          a = []
          a.append(12)

          # numpy array
          v = np.concatenate(a, np.array([1,2,3]))

          # fieldset, geopoints, bufr
          f = mv.merge(g1, g2)

