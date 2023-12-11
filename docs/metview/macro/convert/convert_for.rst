Adjust for() loops
===========================================

.. note::
   
    The Macro to Python converter is available from Metview version 5.22.0

For loops in Macro are normally converted into Python using a **for** loop with **range()**:

.. list-table:: 
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
   * -
       .. code-block:: python
        
          for i=1 to 11 by 2 do
               print(i)
          end for

     -
       .. code-block:: python
        
          for i in range(1, 12, 2):
               print(i)

However, in Macro the **start**, **stop** or **step** can also be a ``float``, but the Python **range()** only supports ``int``\ s. Therefore, when the converter is able to detect the presence of floats the loop is converted into Python using the numpy **arange()** method:


.. list-table:: 
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
   * -
       .. code-block:: python
        
          for i=1 to 4 by 0.5 do
               print(i)
          end for

     -
       .. code-block:: python
          
          import numpy as np

          for i in np.arange(float(1), float(4+0.5/2), float(0.5)):
               print(i)

Unfortunately, there are cases when **start**, **stop** or **step** hold float values but the converter cannot detect this and the loop is converted into Python using **range()**. In this case manual correction is needed as illustrated in the following example:

.. list-table:: 
   :header-rows: 1
 
   * - Macro code
     - Generated Python code
     - Correct Python code
   * -
       .. code-block:: python
        
          step = 0.5
          for i=2 to 6 by step do
              print(i)
          end for

     -
       .. code-block:: python
        
          step = 0.5
          # wrong
          for i in range(2, 6 + step, step):
              print(i)

     -
       .. code-block:: python
        
          import numpy as np
          
          step = 0.5
          # correct
          for i in np.arange(2, 6 + step/2., step):
              print(i)

