Inline C and Fortran code
=============================

.. note::
   
    The Macro to Python converter is available from Metview version 5.20.0

Macro supports embedded C and Fortran code via the **inline** keyword. In Metview Python this is **unsupported**. The converter simply puts the C or Fortran code inside a triple quoted string resulting in a correctly formatted but non-functional Python script.
