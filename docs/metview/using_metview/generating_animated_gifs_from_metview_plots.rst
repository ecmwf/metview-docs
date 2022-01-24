.. _generating_animated_gifs_from_metview_plots:

Generating animated GIFs from Metview plots
///////////////////////////////////////////

Metview can generate animated GIF files from the interactive plot
window. Just click on the Export icon or the File → Export menu and
choose **Animated_GIF** as the output format. Make sure that the Frame
Selection is what you want (usually **All**). The spanner icon presents
more options for the output. Note that this feature requires that the
ImageMagick command 'convert' be available on your system.

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image1.png
   :width: 0.3125in
   :height: 0.46875in

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image2.png
   :width: 3.14583in
   :height: 0.95833in

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image3.png
   :width: 3.20833in
   :height: 2.28749in

It is also possible to convert Metview's PostScript output using the
ImageMagick `convert <http://www.imagemagick.org/script/convert.php>`__
command. This is useful when running from a Macro or Python script.
Below are some examples of doing this, along with an example showing how
to incorporate this into a Metview macro.

Please note, if you only try to achieve an animation with a relative
small number of images within *PowerPoint* you might want to consider
the options provided by *PowerPoint*. The *Insert > Photo Album* might
be one of them.

Converting a multi-page PostScript to an animated GIF
=====================================================

To perform this conversion use::

   convert -delay 200 -rotate "90<" input.ps output.gif

Tip: Alter the speed of animation
=================================

To change the animation speed use::

   convert -delay 100 input.gif output.gif

Tip: High-quality larger images
===============================

Simply setting the **-geometry** flag to obtain a larger output file
does not ensure high quality; instead use something like::

   convert -density 150 input.gif output.gif

Tip: Continuous looping
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

Tip: Transparent background
===========================

You can also use convert to replace any white in the image with a
transparent background::

   convert -fuzz 10% -transparent white input.gif output.gif

Example Metview Macro
=====================

The following macro retrieves several time steps of data from MARS,
plots them to a PostScript file and uses the convert command to generate
an animated gif. The result is shown on this page.

.. code-block:: python

    # Metview Macro                                                    
                                                                    
    # ***************************\* LICENSE START ********************************** 
    # 
    # Copyright 2014- ECMWF. This software is distributed under the terms
    # of the Apache License version 2.0. In applying this license, ECMWF does not 
    # waive the privileges and immunities granted to it by virtue of its status as
    # an Intergovernmental Organization or submit itself to any jurisdiction.                                             
    #                            
    # ****************************\* LICENSE END ***********************************                             
                                                              
    # retrieve some data from MARS                                        
    t2m_fc = retrieve(                    
      type : "fc",                                                       
      levtype:"sfc",                                                                                               
      param : "2t",
      time : 00,
      step : [00,"to",72,"by",6],                                        
      grid : [1.5,1.5]                                                   
    )                                                                  
                                         
    # define our plotting attributes                    
    t_shade = mcont(
      legend : "on",
      contour_automatic_setting : "ecchart"              
    )                                                                  
                                                    
    view = geoview(
      map_area_definition : "corners",
      area : [30.62,\ -\ 25.4,70.12,40.36] 
    )                                                                  
                                                       
    # plot the data
    outdir = getenv('SCRATCH')
    outbasename = "t2m_fc"
    ps = ps_output(output_name : outdir & "/" & outbasename)
    setoutput(ps)

    plot(view, t2m_fc, t_shade)                                        
                                                           
    # force Macro to wait for the plot to be generated, then convert
    # to animated gif 

    setoutput(ps) # wait for the plot file to be generated

    shell('convert -delay 100 -rotate "90<" ' & outdir & '/' &         
    outbasename & '.ps ' & outdir & '/' & outbasename & '.gif')        


The resulting image looks like this:

.. image:: /_static/ug/generating_animated_gifs_from_metview_plots/image4.png
   :width: 5.90069in
   :height: 4.17343in