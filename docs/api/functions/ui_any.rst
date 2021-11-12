ui_any
=================

.. py:function:: ui_any(**kwargs)
   
   *New in metview-python version 1.9.0*.
   
   Defines a value input widget component to be used in :func:`dialog`.
      
   :param name: parameter name
   :type name: str
   :param values: value or list of values 
   :param default: default value
   :param help: creates a helper button with a given helper action in the widget.
   :type help: {"help_input", "help_script", "help_multiple_selection", "help_file_box"}, default: None
   :param input_type: define the input type popup editor when ``help`` is "help_input". 
   :type input_type: {point, line, area}, default "line"
   :param help_script_command: define the shell command to be executed when ``help`` is "help_script"
   :type help_script_command: str

   .. note::
      
      See also :func:`dialog`

.. mv-minigallery:: ui_any