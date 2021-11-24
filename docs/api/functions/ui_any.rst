ui.any
=================

.. py:function:: ui.any(**kwargs)
   
   *New in metview-python version 1.9.0*.
   
   Defines a value input widget to be used in :func:`ui.dialog`.
      
   :param name: parameter name
   :type name: str
   :param values: value or list of values 
   :param default: default value
   :param help: creates a helper button with a given helper action in the widget.
   :type help: {"help_input", "help_script", "help_multiple_selection"}, default: None
   :param input_type: define the input type popup editor when ``help`` is "help_input". 
   :type input_type: {point, line, area}, default "line"
   :param help_script_command: defines the shell command to be executed when ``help`` is "help_script"
   :type help_script_command: str
   :rtype: object to be used in :func:`ui.dialog`

   .. note::
      
      See also :func:`ui.dialog`

.. mv-minigallery:: ui.any