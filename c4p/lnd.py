import os, glob
import numpy as np
from IPython.display import display, Image, IFrame
from datetime import date
import xarray as xr

from . import utils

cwd = os.path.dirname(__file__)

class LND:
    def __init__(self, grids_dirpath=None, path_create_ESMF_map_sh=None, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

        self.grids_dirpath='/glade/p/cesmdata/inputdata/share/scripgrids' if grids_dirpath is None else grids_dirpath
        self.path_create_ESMF_map_sh=os.path.join(cwd, './src/rof/create_ESMF_map.sh') if path_create_ESMF_map_sh is None else path_create_ESMF_map_sh
        self.configs = {}

        for k, v in self.__dict__.items():
            utils.p_success(f'>>> LND.{k}: {v}')

    def gen_surfdata(self):
        utils.p_header('>>> Generate land surface data ...')
        # TODO

    def interpinic(self, template, input_field, exe_path=os.path.join(cwd, './src/interpinic/interpinic')):
        utils.p_header('>>> Interpolate the input land surface data based on the given template ...')
        fpath_exe = utils.copy(exe_path, 'interpinic')
        fpath_template = utils.copy(template)
        utils.exec_script(fpath_exe, args=f'-i {input_field} -o {fpath_template}')

        