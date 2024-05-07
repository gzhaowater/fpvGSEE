# fpvGSEE

This GitHub repository includes python code for calculating floating photovoltaics (FPV) power output for the global lakes and reservoirs based on the [GSEE algorithm](https://doi.org/10.1016/j.energy.2016.08.060). The generated dataset can be accessed at [Figshare](https://figshare.com/XX). 

**ERA5_data**

Download three variable at a hourly time step from the [ERA5 dataset](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels) including the surface solar radiation downwards, total sky direct solar radiation at surface, and 2m temperature.

**0_divide.ipynb**

Due to the computational cost of GSEE, we divide the globe into latitudinal regions. These code divides the netCDF files of the three variables into latitudinal files.

**1_run_gsee.py**

This code calls the GSEE code and calculate power output for each latitudinal region. 

**2_merge.ipynb**

This code merges all latitudinal regions to create the global FPV power output dataset. Also, it plots an example for the month of August.

![Alt text](images/PV.png?raw=true "Photovoltaics")
