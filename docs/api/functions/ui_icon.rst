ui.icon
=================

.. py:function:: ui.icon(**kwargs)
   
   *New in metview-python version 1.9.0*.
   
   Defines an Metview icon drop area widget to be used in :func:`ui.dialog`.
      
   :param name: parameter name
   :type name: str
   :param class\_: the accepted Metview icon type(s)
   :type class\_: str or list
   :param default: default icon(s)
   :type default: an icon object or a list of these
   :param help: creates a helper button with a given helper action in the widget.
   :type help: {"help_script"}, default: None
   :param help_script_command: defines the shell command to be executed when ``help`` is "help_script"
   :type help_script_command: str
   :rtype: object to be used in :func:`ui.dialog`

   .. note::
      
      See also :func:`ui.dialog`

.. mv-minigallery:: ui.icon