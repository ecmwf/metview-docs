Dataset
**********************

A dataset is a collection of data and a set of predefined styles to visualise the data. It was created for studying openifs use cases.

Dataset structure
+++++++++++++++++++++

A dataset is a directory with the following structure:

    .. code-block:: shell

        data.yaml
        data/
            data_dir_1 ...
        index/
        conf/
            areas.yaml
            map_styles.yaml
            params.yaml
            param_styles.yaml

data.yaml
-------------------------

This is the main data configuration file describing all the dataset components (aka experiments).

    .. code-block:: yaml

        mars_params: &mars_params
            "93.128": tdyn
            "95.128": trad
            "98.128": tvdiff
            "105.128": tcon
            "109.128": tcl
            "94.128": qdyn
            "99.128": qvdiff
            "106.128": qcon
            "110.128": qcl
        # use __ROOTDIR__ as a placeholder for the actual root data path
        experiments:
            - an:
                label: "an"
                dir: __ROOTDIR__/an
                fname : re"an_[A-Za-z0-9]+_[A-z]+\.grib"
            - oper:
                label: "oper"
                dir: __ROOTDIR__/oper
                fname : re"oper_[A-Za-z0-9]+_[A-z]+_\d+_\d+\.grib"
            - control:
                label: "control"
                dir: __ROOTDIR__/control_hhe4
                fname : re"hhe4_[A-Za-z0-9]+_[A-z]+_\d+_\d+\.grib"
                mars_params: *mars_params

It contains the paths to the data files. The  __ROOTDIR__ placeholder is resolved to the full path of the data directory.

data
--------------------

This is the directory containing the data files. There is one sub-directory in it for each experiment.

index
---------------

The is the directory containing the data indexing information. It contains one directory for each experiment. The contents is typically pre-generated and if it is missing or incomplete automatically re-generated.

conf
---------------

The is the directory containing the map and style configurations. It can be empty, however if we place files in it they will extend the system based default configurations.

conf/areas.yaml
-------------------
-------------------

This file contains the definition of the map areas. 
    
    .. code-block:: yaml

        - base:
            map_area_definition: "corners"
            area: [15,-70,80,40]
        - atl:
            map_area_definition: "corners"
            area: [30,-60,70,0]

Areas defined here can be used like this:

    .. code-block:: python

        view = mv.make_geoview(area="atl")
        mv.plot_maps(v, view=view)


conf/map_styles.yaml
-------------------
-------------------

This file contains the definition of the map plotting styles (:func:`mcoast`). E.g.:

    .. code-block:: yaml

        grey_light_base:
                map_coastline_resolution: "low"
                map_coastline_land_shade: "on"
                map_coastline_land_shade_colour: "grey"
                map_coastline_sea_shade: "on"
                map_coastline_sea_shade_colour: "RGB(0.86,0.94,1)"
                map_boundaries: "on"
                map_boundaries_colour: "RGB(0.21,0.21,0.21)"
                map_disputed_boundaries: "off"
                map_administrative_boundaries: "off"
                map_grid_latitude_increment: 10
                map_grid_longitude_increment: 10
                map_grid_colour: "RGB(0.294,0.294,0.2941)"
                map_label_colour: "RGB(0.294,0.294,0.2941)"

Styles defined here can be used like this:

    .. code-block:: python

        view = mv.make_geoview(area="atl", style="grey_light_base")
        mv.plot_maps(v, view=view)

conf/params.yaml
--------------------
--------------------

This file defines the data parameters and assigns the plotting styles to them.


conf/param_styles.yaml
---------------------------
---------------------------

This file defines the plotting styles for data.
