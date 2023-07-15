************************************************************
`c4p`: a Python package for paleoclimate research using CESM
************************************************************

`c4p` stands for `cesm4paleo`, or "CESM for paleoclimate research".
It aims to provide a user-friendly toolkit for paleoclimate research using CESM.
Specifically, it provides Pythonic workflows for

+ the setup of boundary conditions for paleoclimate simulations
+ the submission of the CESM cases

Note: the current version of `c4p` assumes the runtime environment is the NCAR machine "Derecho".

|

.. grid:: 1 1 2 2
    :gutter: 2

    .. grid-item-card::  Installation
        :class-title: custom-title
        :class-body: custom-body
        :img-top: _static/installation.png
        :link: ug-installation
        :link-type: doc

        Installation instructions.

    .. grid-item-card::  Boundary Condition Setup
        :class-title: custom-title
        :class-body: custom-body
        :img-top: _static/bc_setup.png
        :link: ug-bc_setup
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
   ug-api