ui_option_menu
=================

.. py:function:: ui_option_menu(**kwargs)
   
   *New in metview-python version 1.9.0*.
   
   Defines an option menu (combobox) widget to be used in :func:`dialog`.
      
   :param name: parameter name
   :type name: str
   :param values: list of values
   :type values: list, default: ["a", "b", "c"] 
   :param default: default value
   :type default: default: "a"
   :param beautify: beautifies values appearing in the widget
   :type beautify: bool, default: True
   :param help: creates a helper button with a given helper action in the widget.
   :type help: {"help_script"}, default: None
   :param help_script_command: defines the shell command to be executed when ``help`` is "help_script"
   :type help_script_command: str

   .. note::
      
      See also :func:`dialog`

.. mv-minigallery:: ui_option_menu