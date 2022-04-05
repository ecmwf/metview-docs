remove_duplicates
===================

.. py:function:: remove_duplicates(gpt)

    Returns a new :class:`Geopoints` that contains just one instance of any duplicate
    geopoint in ``gpt``. Two geopoints are considered to be duplicates of each other if
    the files have the same format and the points have the same coordinates, height,
    date, time and values.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: :class:`Geopoints`

.. mv-minigallery:: remove_duplicates
