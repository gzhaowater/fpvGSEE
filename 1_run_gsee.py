from gsee.climatedata_interface.interface import run_interface
import xarray as xr
from datetime import datetime, timedelta
import glob
import numpy as np
import pandas as pd
import os

def tilt2(lat):
    if np.abs(lat)<=15:
        mtilt = lat
    else:
        mtilt = 15*np.abs(lat)/lat
    return mtilt

for ssrd_fname in sorted(glob.glob('tmp_data/era5_ssrd_*.nc')):
    
    t2m_fname = ssrd_fname.replace('ssrd', 't2m')
    dfrac_fname = ssrd_fname.replace('ssrd', 'dfrac')
    pv_fname = ssrd_fname.replace('ssrd', 'pv')
    
    mlat = np.float64(ssrd_fname.split('_')[-1].replace('.nc', ''))
    
    mtilt = tilt2(mlat)
    
    print(mlat, mtilt, datetime.now())
    
    run_interface(
        (ssrd_fname, 'ssrd'),
        pv_fname,
        params=dict(tilt=mtilt, azim=180, tracking=0, capacity=1000),
        frequency='detect',
        diffuse_data=(dfrac_fname, 'dfrac'),
        temp_data=(t2m_fname, 't2m'),
        timeformat=None,
        pdfs_file=None,
        num_cores=15
    )
