import datetime as dt
import numpy as np
import pandas as pd
import pdb

def make_predictors(df, date, hoodname, category):
    """ Create predictor variables.

    Parameters:
        df (DataFrame): crime data
        dates (datetime.date): datetime.date obj; date to predict
        hoodname (str): value for df['NEIGHBORHOOD_ID']

    Returns:
        (DataFrame): Rows are indexed by predictions, columns are features (counts for different intervals)
    """
    hood = df[
        (df['REPORTED_DATE'] < date) & 
        (df['NEIGHBORHOOD_ID'] == hoodname) & 
        (df['OFFENSE_CATEGORY_ID'] == category)
    ]
    nonhood = df[
        (df['REPORTED_DATE'] < date) & 
        (df['NEIGHBORHOOD_ID'] != hoodname) & 
        (df['OFFENSE_CATEGORY_ID'] == category)
    ]

    yesterday_hood = hood[
        hood['REPORTED_DATE'] > (date - dt.timedelta(days=1))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']
    
    last3days_hood = hood[
        hood['REPORTED_DATE'] > (date - dt.timedelta(days=3))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    lastweek_hood = hood[
        hood['REPORTED_DATE'] > (date - dt.timedelta(days=7))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    lastmonth_hood = hood[
        hood['REPORTED_DATE'] > (date - dt.timedelta(days=30))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    lastyear_hood = hood[
        hood['REPORTED_DATE'] > (date - dt.timedelta(days=365))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']
    
    weekago_hood = hood[
        hood['REPORTED_DATE'] == (date - dt.timedelta(days=7))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']
    
    yesterday_nonhood = nonhood[
        nonhood['REPORTED_DATE'] > (date - dt.timedelta(days=1))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']
    
    last3days_nonhood = nonhood[
        nonhood['REPORTED_DATE'] > (date - dt.timedelta(days=3))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    lastweek_nonhood = nonhood[
        nonhood['REPORTED_DATE'] > (date - dt.timedelta(days=7))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    lastmonth_nonhood = nonhood[
        nonhood['REPORTED_DATE'] > (date - dt.timedelta(days=30))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    lastyear_nonhood = nonhood[
        nonhood['REPORTED_DATE'] > (date - dt.timedelta(days=365))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']
    
    weekago_nonhood = nonhood[
        nonhood['REPORTED_DATE'] == (date - dt.timedelta(days=7))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']
    
    #months = [0] * 12
    #months[date.month-1] = 1
    #weekdays = [0] * 7
    #weekdays[date.weekday()] = 1
    #mwd = pd.DataFrame(data=[months+weekdays], index=[category])
    mwd = pd.Series(months+weekdays, index=[category]*19)
    print(type(mwd))

    import pdb; pdb.set_trace()

    return pd.concat(
        [yesterday_hood, last3days_hood, 
        lastweek_hood, lastmonth_hood, 
        lastyear_hood, weekago_hood, 
        yesterday_nonhood, last3days_nonhood, 
        lastweek_nonhood, lastmonth_nonhood, 
        lastyear_nonhood, weekago_nonhood, 
        keys=['yesterday_hood', 'last3days_hood', 
              'lastweek_hood', 'lastmonth_hood',
              'lastyear_hood', 'weekago_hood',
              'yesterday_nonhood', 'last3days_nonhood', 
              'lastweek_nonhood', 'lastmonth_nonhood', 
              'lastyear_nonhood', 'weekago_nonhood'],
              #'Jan', 'Feb'], 
              #'Mar', 'Apr', 'May', 'Jun', 'Jul', 
              #'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Mon', 'Tue', 
              #'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        axis=1,
        sort=False
    ).fillna(0)

def make_responses(df, dates, hood, category):
    """ Create response variables.

    Parameters:
        df (DataFrame): crime data
        dates (list): list of datetime.date objs
        hood (str): value for df['NEIGHBORHOOD_ID']
        category (str): value for df['OFFENSE_CATEGORY_ID']

    Returns:
        (Series): Counts of each offense category for this date and neighborhood
    """
    sub = df[
        (df['NEIGHBORHOOD_ID'] == hood) &
        (df['REPORTED_DATE'].isin(dates)) &
        (df['OFFENSE_CATEGORY_ID'] == category)
    ]
    return sub.groupby('REPORTED_DATE').count()

def main():
    """ Entry point.
    For testing purposes only.
    """
    crime = pd.read_csv('data/raw/crime.csv', parse_dates=True)
    crime['REPORTED_DATE'] = pd.to_datetime(crime['REPORTED_DATE']).dt.normalize()
    crime.to_pickle('data/processed/crime.pkl')
    crime = pd.read_pickle('data/processed/crime.pkl')
    test = make_predictors(
        crime,
        dt.datetime.strptime('2018-04-22', '%Y-%m-%d'),
        'stapleton',
        'burglary'
    )
    print(test.T)
    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
