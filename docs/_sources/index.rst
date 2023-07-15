******************************
CESM for Paleoclimate Research
******************************

This website introduces how to setup and run CESM for paleoclimate research.
It comes with a Python package named `c4p` that stands for `cesm4paleo`, which aims to provide a user-friendly toolkit for paleoclimate research using CESM.
Specifically, it provides Pythonic workflows for

+ the setup of boundary conditions for paleoclimate simulations
+ the submission of the CESM cases

Note: the current version of `c4p` assumes the runtime environment is the NCAR machine "Derecho".

|

.. grid:: 1 1 2 2
    :gutter: 2

    .. grid-item-card::  Installation of `c4p`
        :class-title: custom-title
        :class-body: custom-body
        :img-top: _static/installation.png
        :link: ug-installation
        :link-type: doc

        Installation instructions.

    .. grid-item-card::  Boundary Condition Setup
        :class-title: custom-title
        :class-body: custom-body
        :img-top: _static/setup.png
        :link: ug-setup
        :link-type: doc

        Instructions on boundary condition setup.

    .. grid-item-card::  Run the Simulations
        :class-title: custom-title
        :class-body: custom-body
        :img-top: _static/run.png
        :link: ug-run
        :link-type: doc

        Instructions on how to run CESM cases.

    .. grid-item-card::  API
        :class-title: custom-title
        :class-body: custom-body
        :img-top: _static/api.png
        :link: ug-api
        :link-type: doc

        The essential API.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: User Guide

   ug-installation
   ug-bc_setup
   ug-run
   ug-api