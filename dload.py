import cdsapi
cds = cdsapi.Client()
import pandas as pd

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
import time

df = pd.DataFrame([])
df['date'] = pd.date_range('2020-01-01 00:00','2020-12-31 23:00',freq='D')
df['mth'] = [str(x).zfill(2) for x in df['date'].dt.month]
df['day'] = [str(x).zfill(2) for x in df['date'].dt.day]

fname = "workflow.py"
with open(fname) as f:
    code = f.read()

for index,row in df.iterrows():
    mth = row['mth']
    day = row['day']
    #hour = row['hour']
    
    fname = '0_dloaded/fdir_' + mth + '_' + day + '.nc'    
    if os.path.isfile(fname):
        continue
    
    code_new = code.replace('MM', mth).replace('DD', day) #.replace('HH', hour)

    r = cds.workflow(code_new)
    link = r[0].get('location')
    
    urllib.request.urlretrieve(link, fname)