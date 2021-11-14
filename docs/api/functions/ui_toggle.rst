ui_toggle
=================

.. py:function:: ui_toggle(**kwargs)
   
   *New in metview-python version 1.9.0*.
   
   Defines a widget with two exclusive toggle buttons labelled as "on" and "off". To be used in :func:`dialog`.
      
   :param name: parameter name
   :type name: str
   :param default: default value
   :type default: {"on", "off"} default: "on"
   :param help: creates a helper button with a given helper action in the widget.
   :type help: {"help_script"}, default: None
   :param help_script_command: defines the shell command to be executed when ``help`` is "help_script"
   :type help_script_command: str
   :rtype: object to be used in :func:`dialog`

   .. note::
      
      See also :func:`dialog`

.. mv-minigallery:: ui_toggle