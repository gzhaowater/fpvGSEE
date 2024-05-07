import cdstoolbox as ct

@ct.application(title='Download data')
@ct.output.download()

def application():
    data = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'variable': 'total_sky_direct_solar_radiation_at_surface',
            'year': [
                '1991', '1992', '1993', '1994', 
                '1995', '1996', '1997', '1998', 
                '1999', '2000', '2001', '2002', 
                '2003', '2004', '2005', '2006', 
                '2007', '2008', '2009', '2010', 
                '2011', '2012', '2013', '2014', 
                '2015', '2016', '2017', '2018', 
                '2019', '2020',
            ],
            'month': 'MM',
            'day': 'DD',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        }
    )
    data_daily = ct.cube.groupby_reduce(data, group='time.hour', how='mean', dim='time')
    return data_daily

