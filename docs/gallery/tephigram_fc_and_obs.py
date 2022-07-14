"""
GRIB, BUFR - Forecast and Observation on Tephigram
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


def build_title_text(prof_obs, prof_fc):
    """
    Utility function to generate text for plot title
    """

    # obs
    info = mv.thermo_data_info(prof_obs)
    t1 = "{} UTC WMO Id: {} Lat: {:.2f} Lon: {:.2f}".format(
        info["base_date"].strftime("%Y-%m-%d %H"),
        int(info["station"]),
        info["lat"],
        info["lon"],
    )

    # fc or an
    info = mv.thermo_data_info(prof_fc)
    t2 = "Run: {} UTC +{}h Valid: {} UTC".format(
        info["base_date"].strftime("%Y-%m-%d %H"),
        int(info["step"]),
        info["valid_date"].strftime("%Y-%m-%d %H"),
    )

    return [t1, t2]


filename_obs = "temp_18.bufr"
filename_fc = "fc_prof_18.grib"

# getting data
use_mars = False

# getting forecast data from MARS
if use_mars:
    # retrieve data from MARS
    ret_core = {
        "date": 20180801,
        "time": 0,
        "step": 12,
        "type": "fc",
        "levtype": "ml",
        "area": [50, 10, 40, 25],
        "grid": [0.1, 0.1],
    }

    # forecast fields on model levels 60-137 (bottom is ML=137)
    fs_ml = mv.retrieve(
        **ret_core,
        levelist=[60, "TO", 137],
        param=["t", "q", "u", "v"],
    )

    # log surface pressure (lnsp) is defined on ML-1!
    lnsp = mv.retrieve(**ret_core, levelist=1, param=["lnsp"])

    mv.write(filename_fc, mv.merge(fs_ml, lnsp))
    g = mv.read(filename_fc)

    # get bufr
    bf = mv.retrieve(type="ob", repres="bu", obstype="t", date=20180801)
    mv.write(filename_obs, bf)

# read data from file or fetch from data server
else:
    # obs
    if mv.exist(filename_obs):
        bf = mv.read(filename_obs)
    else:
        bf = mv.gallery.load_dataset(filename_obs)
    # fc
    if mv.exist(filename_fc):
        g = mv.read(filename_fc)
    else:
        g = mv.gallery.load_dataset(filename_fc)


# extract thermo profile for a given station
station = 12982
prof_obs = mv.thermo_bufr(
    data=bf, station=mv.stations(search_key="ident", ident=station)
)

# extract thermo profile from the forecast for the station location
info_obs = mv.thermo_data_info(prof_obs)
location = [info_obs["lat"], info_obs["lon"]]
prof_fc = mv.thermo_grib(
    data=g, coordinates=location, dew_point_formulation="saturation_over_water"
)

# obs: define t and td profile style
prof_vis_obs = mv.mthermo(
    legend="on",
    legend_user_text="OBS",
    thermo_temperature_line_thickness=5,
    thermo_temperature_missing_data_thickness=5,
    thermo_temperature_line_colour="red",
    thermo_dewpoint_line_thickness=5,
    thermo_dewpoint_missing_data_thickness=5,
    thermo_dewpoint_line_colour="red",
)

# obs: define wind plotting style
prof_wind_style_obs = mv.mwind(
    wind_thinning_factor=1,
    wind_field_type="flags",
    wind_flag_colour="red",
    wind_flag_length=0.8,
    wind_flag_origin_marker="dot",
    wind_flag_origin_marker_size=0.2,
)

# fc: define t and td profile style
prof_vis_fc = mv.mthermo(
    legend="on",
    legend_user_text="FC",
    thermo_temperature_line_colour="charcoal",
    thermo_temperature_line_thickness=5,
    thermo_dewpoint_line_colour="charcoal",
    thermo_dewpoint_line_thickness=5,
)

# fc: define wind plotting style
prof_wind_style_fc = mv.mwind(
    wind_thinning_factor=2,
    wind_field_type="flags",
    wind_flag_colour="charcoal",
    wind_flag_length=0.8,
    wind_flag_origin_marker="dot",
    wind_flag_origin_marker_size=0.2,
)

# define thermo grid
thermo_grid = mv.mthermogrid(
    thermo_isotherm_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_isotherm_reference_colour="blue",
    thermo_isotherm_label_font_size=0.4,
    thermo_isobar_label_font_size=0.4,
    thermo_dry_adiabatic_colour="grey",
    thermo_dry_adiabatic_label_frequency=2,
    thermo_mixing_ratio_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_font_size=0.4,
)

# define the thermodynamic view
view = mv.thermoview(
    type="tephigram",
    minimum_temperature=-100,
    maximum_temperature=40,
    top_pressure=100,
    thermo_grid=thermo_grid,
    subpage_clipping="on",
)

# define title
title_txt = build_title_text(prof_obs, prof_fc)
title = mv.mtext(text_lines=title_txt, text_font_size=0.5, text_colour="charcoal")

# define positional legend
legend = mv.mlegend(
    legend_text_colour="black",
    legend_box_mode="positional",
    legend_display_type="disjoint",
    legend_text_font_size=0.4,
    legend_entry_plot_direction="column",
    legend_box_x_position=26,
    legend_box_y_position=12,
    legend_box_x_length=1,
    legend_box_y_length=7,
    legend_entry_text_width=2,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="tephigram_fc_and_obs"))

# generate the plot
mv.plot(
    view,
    prof_obs,
    prof_vis_obs,
    prof_wind_style_obs,
    prof_fc,
    prof_vis_fc,
    prof_wind_style_fc,
    title,
    legend,
)
