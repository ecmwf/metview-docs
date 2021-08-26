.. _macro_string:

Strings
==================

.. note::

    For a list and details of functions and operators on strings, see :ref:`String functions <macro_string_fn>`. 

Strings are sets of characters. They are unlimited in length. String literals are defined using single or double quotes:

.. code-block:: python

    s = "foo"
    s = 'bar'

You can concatenate strings with numbers, dates and other strings. The result is always a string :

.. code-block:: python

    parameter = "z"
    level = 500
    file_name = parameter & level & ".grib"
    print (file_name)

will print the following string::

    z500.grib

You can retrieve substrings using the substring() command :

.. code-block:: python

    print (substring ("Metview", 4, 7))

will print the following string::

    view

You can split strings into substrings, using the function parse() . This takes two strings as input : the first is the string to split, the second is a string consisting of all the separators; it returns a list whose elements are the individual strings resulting from the split (or tokens):

.. code-block:: python

    n = parse("z500.grib", ".")
    print ("name = ", n[1], " extension = ", n[2])

will print the following string::

    name = z500 extension = grib

Note that the separator character(s) are not part of the output token list.


You can create multi-line strings, using the inline keyword:

.. code-block:: python

    s = string inline
    This is a multiline string, with all sorts of characters such as double quotes (") or single quotes (') which are ignored in the inline context.
    end inline
    

Special characters
++++++++++++++++++++++

Some strings that are not easy to enter via a keyboard are defined as global variables. These are:

* ``newline``:  a new line character
* ``tab``: a tab character

An example of using these is:

.. code-block:: python

    greeting = "Hello" & tab & "world" & newline & "Pleased to see you!"
    print(greeting)