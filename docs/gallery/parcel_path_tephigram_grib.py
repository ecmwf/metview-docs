"""
GRIB - Parcel Path from Surface on Tephigram
"""

# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import metview as mv

# Note: at least Metview version 5.17.0 is required

# read GRIB data
filename = "thermo_profile.grib"
if mv.exist(filename):
    g = mv.read(filename)
else:
    g = mv.gallery.load_dataset(filename)

# extract thermo profile (Lat/Lon)
prof = mv.thermo_grib(coordinates=[5, 0], data=g)

# compute parcel path - start from surface
parcel = mv.thermo_parcel_path(prof, mode="surface")

# create plot object for parcel areas
parcel_area = mv.thermo_parcel_area(parcel)

# create plot object for parcel path
parcel_vis = mv.xy_curve(parcel["t"], parcel["p"], "charcoal", "dash", 6)

# define t and td profile style
prof_vis = mv.mthermo(
    thermo_temperature_line_thickness=5, thermo_dewpoint_line_thickness=5
)

# define the thermodynamic view
view = mv.thermoview(
    type="tephigram",
    minimum_temperature=-110,
    maximum_temperature=30,
    # top_pressure=50,
    subpage_clipping="ON",
)

# get profile info for title
info = mv.thermo_data_info(prof)

# define title
title_txt = "Run: {} {} UTC Step: {} h Lat: {:.2f} Lon: {:.2f}".format(
    int(info["date"]), int(info["time"]), int(info["step"]), info["lat"], info["lon"]
)

title = mv.mtext(text_lines=title_txt, text_font_size=0.5, text_colour="charcoal")

# define text lines for info box
txt = []
txt.append("     Mode: " + parcel["start"]["mode"])
txt.append("  Start p: {:.0f} hPa".format(parcel["start"]["p"]))
txt.append("  Start t: {:.1f} C".format(parcel["start"]["t"]))
txt.append(" Start td: {:.1f} C".format(parcel["start"]["td"]))
txt.append("       LI: {:.1f} K".format(parcel["li"]))
txt.append("     CAPE: {:.3f} J/kg".format(parcel["cape"]))
txt.append("      CIN: {:.3f} J/kg".format(parcel["cin"]))

if parcel["lcl"] is not None:
    txt.append("    LCL p: {:.0f} hPa".format(parcel["lcl"]["p"]))
    txt.append("    LCL t: {:.1f} C".format(parcel["lcl"]["t"]))

if parcel["lfc"] is not None:
    txt.append("    LFC p: {:.0f} hPa".format(parcel["lfc"]["p"]))
    txt.append("    LFC t: {:.1f} C".format(parcel["lfc"]["t"]))

if parcel["el"] is not None:
    txt.append("     EL p: {:.0f} hPa".format(parcel["el"]["p"]))
    txt.append("     EL t: {:.1f} C".format(parcel["el"]["t"]))

if parcel["top"] is not None:
    txt.append("    TOP p: {:.0f} hPa".format(parcel["top"]["p"]))
    txt.append("    TOP t: {:.1f} C".format(parcel["top"]["t"]))

# create info box - make sure font is monospace
info_box = mv.mtext(
    text_lines=txt,
    text_font="courier",
    text_font_size=0.4,
    text_colour="charcoal",
    text_justification="left",
    text_mode="positional",
    text_box_x_position=14.8,
    text_box_y_position=11.4,
    text_box_x_length=5.4,
    text_box_y_length=len(txt) * 0.45 + 0.4,
    text_box_blanking="on",
    text_border="on",
    text_border_colour="charcoal",
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="parcel_path_tephigram_grib"))

# plot the profile, parcel areas, parcel path and info box together
mv.plot(view, parcel_area, prof, prof_vis, parcel_vis, title, info_box)
