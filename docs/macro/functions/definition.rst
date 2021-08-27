.. _macro_definition_fn:

Definition Macro functions
=============================

.. note::

   A definition is a list of named items (which may be numbers, strings, lists,...).


.. describe:: definition definition(any,...)

   Builds a definition with the specified elements. Note that the keyword definition is not in fact required:

   .. code-block:: python
   
      my_field = (param : "z", level : 500, grid : [2, 2])


.. describe::   any definition[string]

   Returns the value named by the input string from a definition.

   .. code-block:: python

      level = my_field["level"]

   Note the shorthand form of this, the dot operator:

   .. code-block:: python
      
      level = my_field.level


.. describe:: list keywords( definition )

   Returns the list of keys (member names) in the given definition.