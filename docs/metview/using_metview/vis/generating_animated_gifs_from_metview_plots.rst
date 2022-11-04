.. _generating_animated_gifs_from_metview_plots:

Generating animated GIFs from Metview plots
///////////////////////////////////////////

Interactive usage
-------------------------

Metview can generate animated GIF files from the interactive plot
window. Just click on the Export icon or the File → Export menu and
choose **Animated_GIF** as the output format. Make sure that the Frame
Selection is what you want (usually **All**). The spanner icon presents
more options for the output. Note that this feature requires that the
ImageMagick command  `convert <http://www.imagemagick.org/script/convert.php>`__ be available on your system.

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image1.png
   :width: 0.3125in
   :height: 0.46875in

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image2.png
   :width: 3.14583in
   :height: 0.95833in

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image3.png
   :width: 3.20833in
   :height: 2.28749in

Script usage
---------------

It is also possible to convert Metview's output to animated gif from Python or Macro scripts. This also relies on using the ImageMagick `convert <http://www.imagemagick.org/script/convert.php>`__ command (so it has to be installed).

The Gallery contains a couple of Python examples showcasing this technique:

- :ref:`gallery_t2_animation`: this generates PostScript output containing one page for each forecast timestep. It is then converted into animated gif in one go.

   .. image:: /_static/gallery/t2_animation.gif
      :width: 350px
      :target: ../../../gen_files/gallery/t2_animation.html

- :ref:`gallery_rotating_geos_globe_animation`: in this example the map projection changes in each animation frame. In Python we cannot generate a single PostScript/PDF output for this. Therefore a separate output file (PDF in this example, but could also be PNG) is produced for each frame. In the end these files are converted to animated gif in a single command.

   .. image:: /_static/gallery/rotating_geos_globe_animation.gif
      :width: 350px
      :target: ../../../gen_files/gallery/rotating_geos_globe_animation.html

A Metview Macro example can be found here: :ref:`generating_animated_gif_macro`.


ImageMagick options
---------------------

This chapter describes some of the `convert <http://www.imagemagick.org/script/convert.php>`__ options you may want to use when generating animated gifs.

.. note::
      
   If you only try to achieve an animation with a relative
   small number of images within *PowerPoint* you might want to consider
   the options provided by *PowerPoint*. The *Insert > Photo Album* might
   be one of them.

Converting a multi-page PostScript to an animated GIF
=====================================================

To perform this conversion use::

   convert -delay 200 -rotate "90<" input.ps output.gif

Alter the speed of animation
=================================

To change the animation speed use::

   convert -delay 100 input.gif output.gif

High-quality larger images
===============================

Simply setting the **-geometry** flag to obtain a larger output file
does not ensure high quality; instead use something like::

   convert -density 150 input.gif output.gif

Continuous looping
=======================

Some viewers, especially some versions of MS PowerPoint, only play a
single animation cycle. To make it continuous you can use the option
*-loop* with convert::

   convert -loop 999 input.gif output.gif

.. note:: 
   
   In Microsoft *PowerPoint* in most cases it should work to
   import the GIF as an 'Image'. If the GIF is imported as a 'Video file',
   *PowerPoint* requires extra settings for continuous looping of GIFs. Go
   to the "video tools" menu, which contains "format" and "playback". Under
   the playback menu, there is a button "Loop until stopped". Click on it,
   to allow continuous loops!

Transparent background
===========================

You can also use convert to replace any white in the image with a
transparent background::

   convert -fuzz 10% -transparent white input.gif output.gif

