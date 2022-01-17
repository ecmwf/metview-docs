ui.slider
=================

.. py:function:: ui.slider(**kwargs)
   
   *New in metview-python version 1.9.0*.
   
   Defines a slider widget to be used in :func:`ui.dialog`.
      
   :param name: parameter name
   :type name: str
   :param default: default value
   :type default: number, default: 0
   :param min: minimum value
   :type min: number, default: 0
   :param max: maximum value
   :type max: number, default: 100
   :param step: value step
   :type step: number, default: 10
   :param direction: slider direction
   :type direction: {"max_on_left", "max_on_right"}, default: "max_on_right"
   :param help: creates a helper button with a given helper action in the widget.
   :type help: {"help_script"}, default: None
   :param help_script_command: defines the shell command to be executed when ``help`` is "help_script"
   :type help_script_command: str
   :rtype: object to be used in :func:`ui.dialog`

   .. note::
      
      See also :func:`ui.dialog`

.. mv-minigallery:: ui.slider