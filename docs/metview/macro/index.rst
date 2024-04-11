.. _macro_lang:

Macro language
====================================

.. note::
   These pages describe the Metview Macro language. Macro was developed before Python became popular,
   but has similar principles and syntax. As the Python language and ecosystem has become so
   well-featured, you may wish to consider using Metview's :ref:`Python API <python_api>` instead of the Macro language.

A macro language was part of the first design specification of Metview. It is designed to perform data manipulation and plotting from within the Metview system environment. A language is the best "user interface" to describe very complex sequences of actions, particularly if the flow of action is conditional. It also provides a common means to express the mathematical formulae used when performing data manipulations.

The Metview Macro language was designed to be as easy to get started with as a script language (e.g. UNIX shell) and as powerful as a modern computer language. To be as simple as a shell language implies that no variable declarations or program units should be required. This feature is achieved through the implementation of typeless variables, a benefit of object-oriented languages. To be as complex as a computer language implies support for variables, flow control, functions and procedures, I/O and error control.

The Metview Macro language provides an easy, powerful and comprehensive way for a researcher to manipulate and display meteorological data. It extends the use of Metview into an operational environment as it enables a user to write complex scripts that may be run with any desired periodicity. 

.. toctree::
   :maxdepth: 1
   
   syntax
   data_types/index
   functions/index 
   macro_animated_gif
   convert_to_python
