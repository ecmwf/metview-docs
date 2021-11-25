Macro syntax
===================

Reserved keywords
++++++++++++++++++++++

The following words are reserved and cannot be used as identifiers::

    and by case do else end export extern for function global if import in include inline loop nil not object of on or otherwise repeat return task tell then to until when while

Comments
+++++++++++++++

To write comments, use the character #. Any text from this character to the end of the line is ignored. Each line to be commented must be preceded by the # character, i.e. C-like multi-line comments are not allowed.

.. code-block:: python
    
    # Now plot the field
    plot (Z500) # using default contours 

Variables and scope
+++++++++++++++++++++++++

Variables declared in the program scope are not visible to functions unless they are declared global. This is usually discouraged, but an example is here:

.. code-block:: python

    global my_var = 5
    
    function modify_my_var()
        my_var = 6
    end modify_my_var
    
    print(my_var)    # 5
    modify_my_var()
    print(my_var)    # 6

If the word global had not been present, the last line would have printed 5, because the function would have simply set the value of a local variable and not touched the one declared outside.

Loops
+++++++++++++

.. code-block:: python

    # basic for loop
    for i = 1 to 4 do
        print (i)
    end for

    # for loop with a list
    for i = 1 to count(thisList) do
        print (i, " : ", thisList[i])
    end for

    # for loop using dates with a step
    for day = 2003-01-24 to 2003-02-14 by 3 do
        print (day)
    end for

    # basic while loop
    n = 1
    while n <= 10 do
        print(n)
        n = n + 1
    end while

    # basic repeat loop
    n = 1
    repeat
        print(n)
        n = n + 1
    until n > 10

    # loop - can be used on lists, fieldsets and geopoints
    loop element in thisList
        print(element)
    end loop


Tests
++++++++++

.. code-block:: python

    # basic if test
    if a = b then
        print("a and b are equal")
    end if
    
    # if test with an else condition
    if a = b then
        print("a and b are equal")
    else print("a and b are different")
    end if
    
    # if test with an else if and an else condition
    if a > 0 then
        print("a is positive")
    else if a < 0 then
        print("a is negative")
    else print("a is null")
    end if
    
    # when statement. The code following the first true expression is
    # executed.
    when
        a > 0 :
            print("a is positive")
            end
        a < 0 :
            print("a is negative")
            end
        a = 0 :
            print("a is null")
            end
    end when
    
    # case statement
    case type(x) of
        "number" :
            print("x is a number")
            end
        "date" :
            print("x is a date")
            end
        otherwise :
            stop("Unsupported type")
            end
    end case


Functions
++++++++++++++

You can define your own functions  in Macro. Functions can take any number of input arguments and can optionally enforce type-checking on them. A function does not need to have a return value. Only one value can be returned - to return multiple values, return a structure such as a list, vector or definition containing the values.

The following examples show how to write functions in Macro.

.. code-block:: python

    # function that takes no arguments
    function always_return_5 ()
        return 5
    end always_return_5
    
    five = always_return_5()  # 5
 
.. code-block:: python

    # function that takes an argument and does no type-checking
    function add_10_untyped (a)
        return a+10
    end add_10_untyped
    
    b = add_10_untyped(4) # 14
    
.. code-block:: python 

    # function that takes two arguments
    function add_two_untyped (a, b)
        return a+b
    end add_two_untyped
    
    b = add_two_untyped(9, 11) # 20
 
.. code-block:: python

    # function that takes an argument that must be a number
    function add_10_to_number (a:number)
        return a+10
    end add_10_to_number
    
    b = add_10_to_number(6) # 16
    b = add_10_to_number('Hello')  # Run-time error
 
.. code-block:: python

    # function that returns a list of four values
    function return_4_values_as_list(a)
        return [a+4, a+3, a+2, a+1]
    end return_4_values
    
    b = return_4_values_as_list(10) # [14,13,12,11]
    
.. code-block:: python

    # return four values as named elements of a structure
    function return_4_values_as_definition(a)
        return (w: a+1, x: a+2, y:a+3, z:a+20)
    end return_4_values_as_definition
    
    b = return_4_values_as_definition(10) # (w:11,x:12,y:13,z:30)
 
.. code-block:: python

    # function that takes any number of arguments
    function print_all_params
        loop arg in arguments()
            print(arg)
        end loop
    end print_all_params
    
    print_all_params(5, 6, 7, 'Hello')


Macro tutorial
+++++++++++++++++++++

To learn more about the Macro syntax, please follow the Metview Tutorials.
