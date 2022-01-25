.. _animation_frames_in_the_display_window:

Animation frames in the Display Window
//////////////////////////////////////


The sidebar in the **Display Window** contains two tabs. The first of
these presents the animation frames of the currently loaded data, and
works best with GRIB data.

.. image:: /_static/ug/animation_frames_in_the_display_window/image1.png
   :width: 5.90069in
   :height: 2.79949in

A selection of metadata from the GRIB fields is shown. The
currently-selected frame is highlighted, and the frames that have
already been rendered and cached are shaded - these will be displayed
more quickly the next time they are selected.

The columns are sortable. By default, the sorting is done on the order
in which a field occurs in the GRIB file. Click on a column heading to
sort the frames by that column, e.g. **Name**.

.. image:: /_static/ug/animation_frames_in_the_display_window/image2.png
   :width: 4.53125in
   :height: 2.15625in

The selection of keys used to populate these columns is configurable.
The **Key profile** button allows you to choose a different set of keys
stored in a *profile*.

.. image:: /_static/ug/animation_frames_in_the_display_window/image3.png
   :width: 4.45833in
   :height: 0.94792in

Here's one we prepared earlier (not supplied with Metview), displaying
some statistics of the field values. Note that this particular selection
could result in a slow startup, owing to the fact that it needs to scan
every value in every field. Most keys do not need to do this, as they
are just metadata.

.. image:: /_static/ug/animation_frames_in_the_display_window/image4.png
   :width: 4.58333in
   :height: 3.09996in

To the left of the profile selection button is the **Manage key profiles
button**. This brings up a dialogue that allows management of key
profiles (click the **Profiles** button at the top).

.. image:: /_static/ug/animation_frames_in_the_display_window/image5.png
   :width: 4.375in
   :height: 3.24774in

Once you have a new key profile, you can change the keys that it uses.
Click the **Keys** button at the top and you will see an interface that
allows you to add and delete keys, as well as change the order in which
they appear. Different categories of keys are available to help you find
what you want.

.. image:: /_static/ug/animation_frames_in_the_display_window/image6.png
   :width: 5in
   :height: 3.6875in

Finally, the key profile management dialogue allows you to import key
profiles from the **GRIB Examiner**. Click the Import button at the top
to do this.

.. image:: /_static/ug/animation_frames_in_the_display_window/image7.png
   :width: 4.375in
   :height: 3.24774in

With all this flexibility, you really can customise the Frames panel of
the **Display Window** as you wish!
