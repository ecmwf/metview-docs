Adjust concatenations
=============================

In Macro the generic **concatenation** operator is **& (ampersand)**, which can be used for strings, lists, fieldsets and many other built-in types in the same way. Conversion of these operator calls to Python would require run-time information, which the converter does not posses since it does not actually runs the Macro. To overcome this difficulty the converter adds a local function called ``_concat`` to the top of the generated Python script and all the calls to & are replaced by calling ``_concat``. You would see something like this: 

.. list-table:: Replacing & with _concat() calls in the generated Python code
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
          c = _concat(a, "my_text")

          # list
          a = []
          a = _concat(a, 12)

          # numpy array
          v = _concat(a, np.array([1,2,3]))

          # fieldset, geopoints, bufr
          f = _concat(g1, g2)

While this solution results in a correctly working code it must be only regarded as a **temporary solution**. Ideally you should check your code and **replace** all ``_concat()`` calls with the proper concatenation used for a given type in Python, and finally remove the ``_concat()`` function from your script.

The following table can serve you as a guide to properly convert the & operator calls in Macro to Python:  

.. list-table:: Resolving the Macro & operator calls in Python
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

