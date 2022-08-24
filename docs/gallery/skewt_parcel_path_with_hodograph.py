"""
BUFR - Skew-T with Parcel Path and Hodograph
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
import numpy as np

# Note: at least Metview version 5.17.0 is required


def build_title_text(prof):
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


def build_box_text(p):
    """
    Utility function to generate text for parcel info box
    """

    def _add_row(label, val, units=""):
        t = "{:>7} ".format(label + ":")
        if val is None:
            t += "-"
        elif isinstance(val, str):
            t += "{:<}".format(val)
        else:
            t += "{:.0f} {}".format(val, units)
        return t

    def _add_row_pt(label, val):
        t = "{:>7} ".format(label + ":")
        if val is None or not isinstance(val, dict):
            t += "-"
        else:
            t += "{:.0f}/{:.1f}".format(val["p"], val["t"])
        return t

    t = []
    t.append("{:>7} {:<10}".format("mode:", p["start"]["mode"]))
    t.append(_add_row("cape", p.get("cape"), "J/kg"))
    t.append(_add_row("cin", p.get("cin"), "J/kg"))
    t.append(_add_row("li", p.get("li"), ""))
    t.append(_add_row_pt("lcl", p.get("lcl")))
    t.append(_add_row_pt("lfc", p.get("lfc")))
    t.append(_add_row_pt("el", p.get("el")))
    t.append(_add_row_pt("start", p.get("start")))

    return t


def build_layout(thermo_view, hodo_incr=5, hodo_max_val=35):
    """
    Utility function to build a layout with thermo view on the left
    and hodograph on the right
    """

    # --------------------------------
    # define page for the thermo view
    # --------------------------------

    th_page = mv.plot_page(
        top=0,
        bottom=100,
        left=0,
        right=75,
        view=thermo_view,
    )

    # ----------------------------
    # define the hodograph view
    # ----------------------------

    # the maximum radial size of the coordinate system
    hodo_max_val = np.ceil(hodo_max_val / hodo_incr) * hodo_incr

    # define horizontal and vertical  axes
    h_axis = mv.maxis(axis_position="left", axis_tick="off", axis_tick_label="off")
    v_axis = mv.maxis(axis_position="bottom", axis_tick="off", axis_tick_label="off")

    # the view
    view = mv.cartesianview(
        x_automatic="off",
        x_min=-hodo_max_val,
        x_max=hodo_max_val,
        y_automatic="off",
        y_min=-hodo_max_val,
        y_max=hodo_max_val,
        horizontal_axis=h_axis,
        vertical_axis=v_axis,
        subpage_frame="on",
        subpage_frame_thickness=1,
        subpage_x_position=5,
        subpage_y_position=5,
        subpage_x_length=90,
        subpage_y_length=90,
    )

    # define the hodograph plot page.
    # NOTE: In order to correctly render the hodograph (we want
    # concentric circles instead of ellipses) we have to ensure
    # that the physical width and height of the plot are the same.
    # Please note that while the page size is defined in % the
    # superpage size is defined in cm! See also subpage size in the view.

    # physical size of the whole plot (A4 landscape)
    sp_width = 29.7
    sp_height = 21

    hodo_width = 7  # cm
    hodo_height = 7  # cm
    page_width = 100 * hodo_width / sp_width
    page_height = 100 * hodo_height / sp_height
    page_top = 10
    page_left = 100 - page_width - 5

    hodo_page = mv.plot_page(
        top=page_top,
        bottom=page_top + page_height,
        left=page_left,
        right=page_left + page_width,
        view=view,
    )

    # ---------------------------------------
    # define the superpage (A4 landscape)
    # ---------------------------------------

    dw = mv.plot_superpage(pages=[th_page, hodo_page])
    return dw


def build_hodo_bg(
    hodo_incr=5,
    hodo_max_val=35,
    hodo_highlight=[10, 20, 30],
    hodo_label=[10, 20, 30],
    hodo_label_size=0.3,
    hodo_colour="black",
):
    """
    Utility function to generate plot objects making up
    the hodograph background
    """

    # the maximum radial size of the coordinate system
    hodo_max_val = np.ceil(hodo_max_val / hodo_incr) * hodo_incr

    gr_lst = []

    # build the concentric circles
    sp = hodo_incr
    angle_incr = 2 * np.pi / 180
    while sp <= hodo_max_val:
        xp = [np.cos(i * angle_incr) * sp for i in range(1, 182)]
        yp = [np.sin(i * angle_incr) * sp for i in range(1, 182)]
        gr = mv.xy_curve(xp, yp, hodo_colour, "solid", 1 if sp in hodo_highlight else 1)
        gr_lst.append(gr)
        sp += hodo_incr

    # build horizontal and vertical lines going
    # through the centre
    gr_lst.append(
        mv.xy_curve([-hodo_max_val, hodo_max_val], [0, 0], hodo_colour, "solid", 1)
    )
    gr_lst.append(
        mv.xy_curve([0, 0], [-hodo_max_val, hodo_max_val], hodo_colour, "solid", 1)
    )

    # add labels to the horizontal line
    vis = mv.input_visualiser(
        input_plot_type="xy_point",
        input_x_values=[-v for v in hodo_label] + hodo_label,
        input_y_values=[0] * 2 * len(hodo_label),
        input_values=hodo_label + hodo_label,
    )

    sym = mv.msymb(
        symbol_colour=hodo_colour,
        symbol_text_font_size=hodo_label_size,
        symbol_text_font_style="normal",
        symbol_text_position="bottom",
    )

    gr_lst.extend([vis, sym])

    return gr_lst


def build_hodo_wind(prof, pres_bins, pres_colours):
    """
    Utility function to generate plot objects for the hodograph
    wind data (per bin)
    """

    # get individual profiles as vectors. Values are sorted by descending
    # pressure, no missing values includes.
    info = mv.thermo_data_values(prof, 0)
    p = info["p_wind"]
    u = info["u"]
    v = info["v"]

    gr_wind = []
    for i in range(len(pres_bins) - 1):

        # collect wind data in bin
        u_val = []
        v_val = []
        for k in range(len(p)):
            if (
                not np.isnan(p[k])
                and not np.isnan(u[k])
                and not np.isnan(v[k])
                and p[k] <= pres_bins[i]
                and p[k] >= pres_bins[i + 1]
            ):
                u_val.append(u[k])
                v_val.append(v[k])

        # build graph object
        if u_val and v_val:
            vis = mv.input_visualiser(input_x_values=u_val, input_y_values=v_val)

            gr = mv.mgraph(
                legend="on",
                graph_line_colour=pres_colours[i],
                graph_line_style="solid",
                graph_line_thickness=5,
            )
            gr_wind.extend([vis, gr])

    return gr_wind


# read BUFR data
filename = "temp.bufr"
if mv.exist(filename):
    b = mv.read(filename)
else:
    b = mv.gallery.load_dataset(filename)

# define station id
statid = "78583"

# extract thermo profile
prof = mv.thermo_bufr(data=b, station=mv.stations(search_key="ident", ident=statid))

# -----------------------------
# profile and parcel path
# -----------------------------

# compute parcel path
parcel = mv.thermo_parcel_path(prof, mode="mucape", layer_depth=300)

# create plot object for parcel areas
parcel_area = mv.thermo_parcel_area(parcel)

# create plot object for parcel path
parcel_vis = mv.xy_curve(parcel["t"], parcel["p"], "charcoal", "dash", 6)

# define t and td profile style
prof_vis = mv.mthermo(
    thermo_temperature_line_thickness=5,
    thermo_temperature_missing_data_thickness=5,
    thermo_dewpoint_line_thickness=5,
    thermo_dewpoint_missing_data_thickness=5,
)

# define wind plotting style
prof_wind_style = mv.mwind(
    wind_thinning_factor=1,
    wind_field_type="flags",
    wind_flag_colour="magenta",
    wind_flag_length=0.8,
    wind_flag_origin_marker="dot",
    wind_flag_origin_marker_size=0.2,
)

# define thermo grid
thermo_grid = mv.mthermogrid(
    thermo_isotherm_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_isotherm_reference_colour="blue",
    thermo_dry_adiabatic_colour="grey",
    thermo_dry_adiabatic_label_frequency=2,
    thermo_mixing_ratio_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_colour="RGB(0.2577,0.6364,0.5039)",
    thermo_mixing_ratio_label_font_size=0.4,
)

# define thermodynamic view
thermo_view = mv.thermoview(
    type="skewt",
    minimum_temperature=-140,
    maximum_temperature=40,
    top_pressure=100,
    thermo_grid=thermo_grid,
    subpage_clipping="on",
    subpage_x_position=8,
    subpage_y_position=15,
    subpage_x_length=82,
    subpage_y_length=82,
)

# define profile title
prof_title_txt = build_title_text(prof)
prof_title = mv.mtext(
    text_lines=prof_title_txt, text_font_size=0.5, text_colour="charcoal"
)

# -----------------------------
# hodograph
# -----------------------------

# hodograph options
hodo_incr = 5
hodo_highlight = [10, 20, 30]
hodo_label = [10, 20, 30]
hodo_max_val = 35
hodo_colour = "RGB(0.4,0.4,0.4)"

# define the wind speed bins and their associated colours
pres_bins = [1050, 700, 500, 300, 200, 100]
pres_colours = ["red", "kelly_green", "sky", "blue", "magenta"]

# generate the graphical objects for the hodograph background
gr_hodo_bg = build_hodo_bg(
    hodo_incr=hodo_incr,
    hodo_highlight=hodo_highlight,
    hodo_label=hodo_label,
    hodo_max_val=hodo_max_val,
    hodo_colour=hodo_colour,
)

# generate the graphical objects for wind data on the hodograph
gr_hodo_wind = build_hodo_wind(prof, pres_bins, pres_colours)

# define hodograph legend with custom labels
legend_text = []
for i in range(len(pres_bins) - 1):
    legend_text.append(str(pres_bins[i]) + "-" + str(pres_bins[i + 1]))

hodo_legend = mv.mlegend(
    legend_display_type="disjoint",
    legend_box_mode="positional",
    legend_text_font_size=0.3,
    legend_text_composition="user_text_only",
    legend_user_lines=legend_text,
    legend_column_count=3,
    legend_box_y_position=6.5,
    legend_box_y_length=1.5,
    legend_entry_text_width=80,
)

# -----------------------------
# layout
# -----------------------------

# generate the layout and build the view for the hodograph
dw = build_layout(thermo_view, hodo_incr=hodo_incr, hodo_max_val=hodo_max_val)

# -------------------------------
# info box
# -------------------------------

txt = build_box_text(parcel)

# create info box - ensure font is monospace
info_box = mv.mtext(
    text_lines=txt,
    text_font="courier",
    text_font_size=0.45,
    text_colour="charcoal",
    text_justification="left",
    text_mode="positional",
    text_box_x_position=22.1,
    text_box_y_position=6.8,
    text_box_x_length=4.8,
    text_box_y_length=len(txt) * 0.5 + 0.5,
    text_box_blanking="on",
    text_border="on",
    text_border_colour="charcoal",
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="skewt_parcel_path_with_hodograph"))

# generate the plot
mv.plot(
    dw[0],
    parcel_area,
    prof,
    prof_vis,
    prof_wind_style,
    parcel_vis,
    prof_title,
    info_box,
    dw[1],
    gr_hodo_bg,
    gr_hodo_wind,
    hodo_legend,
)
