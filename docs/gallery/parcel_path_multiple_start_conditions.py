"""
GRIB - Multiple Parcel Path Start Conditions on Skew-T
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


def make_title_text(prof):
    """
    Utility function to generate text for plot title
    """

    # get profile info for title
    info = mv.thermo_data_info(prof)

    # obs
    if "station" in info:
        t1 = "{} {} UTC WMO Id: {}".format(
            int(info["date"]), int(info["time"]), int(info["station"])
        )
    # fc or an
    else:
        t1 = "Run: {} UTC +{}h Valid: {} UTC".format(
            info["base_date"].strftime("%Y-%m-%d %H"),
            int(info["step"]),
            info["valid_date"].strftime("%Y-%m-%d %H"),
        )

    t2 = "Lat: {:.2f} Lon: {:.2f}".format(info["lat"], info["lon"])
    return [t1, t2]


def make_box_text(parcels, has_top=False):
    """
    Utility function to generate text for parcel info box
    """

    t = " <b>{:<9}{:>5}{:>5}{:>4}{:>5}{:>5}{:>5}</b>".format(
        "PARCEL", "CAPE", "CIN", "LI", "LCL", "LFC", "EL"
    )

    if has_top:
        t += "<b>{:>5}</b>".format("TOP")

    t += "<b>{:^13}</b>".format("START")

    txt = [t.replace(" ", "&nbsp;")]
    for p in parcels:
        if p is None:
            continue

        t = " {:<9}{:5.0f}{:5.0f}".format(p["start"]["mode"], p["cape"], p["cin"])

        v = p.get("li", None)
        if v is not None:
            t += "{:4.0f}".format(v)
        else:
            t += "{:>4}".format("-")

        v = p.get("lcl", None)
        if v is not None:
            t += "{:5.0f}".format(v["p"])
        else:
            t += "{:>5}".format("-")

        v = p.get("lfc", None)
        if v is not None:
            t += "{:5.0f}".format(v["p"])
        else:
            t += "{:>5}".format("-")

        v = p.get("el", None)
        if v is not None:
            t += "{:5.0f}".format(v["p"])
        else:
            t += "{:>5}".format("-")

        if has_top:
            v = p.get("top", None)
            if v is not None:
                t += "{:5.0f}".format(v["p"])
            else:
                t += "{:>5}".format("-")

        t += "{:6.0f}".format(p["start"]["p"])
        t += "{:5.1f}".format(p["start"]["t"])

        txt.append(t.replace(" ", "&nbsp;"))

    return txt


filename = "thermo_global_5.grib"

# getting data
use_mars = False

# getting forecast data from MARS
if use_mars:
    # retrieve data from MARS
    # low res global data
    ret_core = {
        "date": 20220604,
        "time": 12,
        "step": 12,
        "type": "fc",
        "levtype": "ml",
        "area": [90, -180, -90, 180],
        "grid": [5, 5],
    }

    # forecast fields on model levels 60-137 (bottom is ML=137)
    fs_ml = mv.retrieve(
        **ret_core,
        levelist=[60, "TO", 137],
        param=["t", "q", "u", "v"],
    )

    # log surface pressure (lnsp) is defined on ML-1!
    lnsp = mv.retrieve(**ret_core, levelist=1, param=["lnsp"])

    mv.write(filename, mv.merge(fs_ml, lnsp))
    g = mv.read(filename)
# read data from file
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)


# extract thermo profile
location = [-5, -60]  # lat, lon
prof = mv.thermo_grib(coordinates=location, data=g)

# compute parcels paths with various options
options = [
    {"mode": "surface"},
    {"mode": "ml50"},
    {"mode": "ml100"},
    {"mode": "mucape", "layer_depth": 300},
]

parcels = []
for opt in options:
    parcels.append(mv.thermo_parcel_path(prof, **opt))

# plot the mucape parcel path only
parcel = parcels[-1]

# create plot object for parcel areas
parcel_area = mv.thermo_parcel_area(parcel)

# create plot object for parcel path
parcel_vis = mv.xy_curve(parcel["t"], parcel["p"], "charcoal", "dash", 6)

# define t and td profile style
prof_vis = mv.mthermo(
    thermo_temperature_line_thickness=5, thermo_dewpoint_line_thickness=5
)

# define wind plotting style
prof_wind_style = mv.mwind(
    wind_thinning_factor=2,
    wind_field_type="flags",
    wind_flag_colour="magenta",
    wind_flag_length=0.8,
    wind_flag_origin_marker="dot",
    wind_flag_origin_marker_size=0.2,
)

# define thermodynamic grid
grid = mv.mthermogrid(
    thermo_isotherm_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_isotherm_reference_colour="blue",
    thermo_dry_adiabatic_colour="grey",
    thermo_dry_adiabatic_label_frequency=2,
    thermo_mixing_ratio_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_font_size=0.4,
)

# define the thermodynamic view
view = mv.thermoview(
    type="skewt",
    minimum_temperature=-120,
    maximum_temperature=40,
    top_pressure=100,
    subpage_clipping="on",
    subpage_y_position=20,
    subpage_y_lenght=70,
)

# define title
txt = make_title_text(prof)
title = mv.mtext(text_lines=txt, text_font_size=0.5, text_colour="charcoal")

# create info box - make sure font is monospace
txt = make_box_text(parcels)
info_box = mv.mtext(
    text_lines=txt,
    text_font="courier",
    text_font_size=0.4,
    text_colour="charcoal",
    text_justification="left",
    text_mode="positional",
    text_box_x_position=3.5,
    text_box_y_position=0.9,
    text_box_x_length=12,
    text_box_y_length=len(txt) * 0.45 + 0.4,
    text_box_blanking="on",
    text_border="on",
    text_border_colour="charcoal",
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="parcel_path_multiple_start_conditions"))

# plot the profile, parcel areas, parcel path and info box together
mv.plot(
    view,
    parcel_area,
    prof,
    prof_vis,
    prof_wind_style,
    parcel_vis,
    grid,
    title,
    info_box,
)
