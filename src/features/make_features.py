import os
import numpy as np
import pandas as pd
import datetime as dt

def make_predictors(df, dates, hoodname, category):
    """ Create predictor variables.

    Parameters:
        df (DataFrame): crime data
        dates (list): list of datetime.date obj's; dates to predict
        hoodname (str): value for df['NEIGHBORHOOD_ID']

    Returns:
        (DataFrame): Rows are indexed by predictions, columns are features (counts for different intervals)
    """
    hood_all = df[
        (df['NEIGHBORHOOD_ID'] == hoodname) & 
        (df['OFFENSE_CATEGORY_ID'] == category)
    ]
    nonhood_all = df[
        (df['NEIGHBORHOOD_ID'] != hoodname) & 
        (df['OFFENSE_CATEGORY_ID'] == category)
    ]
    feat_cols = ['yesterday_hood', 'last3days_hood', 
                'lastweek_hood', 'lastmonth_hood',
                'lastyear_hood', 'weekago_hood',
                'yesterday_nonhood', 'last3days_nonhood', 
                'lastweek_nonhood', 'lastmonth_nonhood', 
                'lastyear_nonhood', 'weekago_nonhood',
                'Jan', 'Feb', 
                'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Mon', 'Tue', 
                'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    feats = pd.DataFrame(columns = feat_cols)
    for date in dates:
        hood = hood_all[(hood_all['REPORTED_DATE'] < date)]
        nonhood = nonhood_all[(nonhood_all['REPORTED_DATE'] < date)]

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
        
        months = [0] * 12
        months[date.month-1] = 1
        weekdays = [0] * 7
        weekdays[date.weekday()] = 1
        mwd = pd.DataFrame(data=[months+weekdays], index=[category])

        feat =  pd.concat(
            [yesterday_hood, last3days_hood, 
            lastweek_hood, lastmonth_hood, 
            lastyear_hood, weekago_hood, 
            yesterday_nonhood, last3days_nonhood, 
            lastweek_nonhood, lastmonth_nonhood, 
            lastyear_nonhood, weekago_nonhood, mwd],
            axis=1,
            sort=False
        ).fillna(0)
        feat.columns =  feat_cols
        feat.index = [date]
        feats = feats.append(feat, sort=False)
    return(feats)

def make_responses(df, dates, hoodname, category):
    """ Create response variables.

    Parameters:
        df (DataFrame): crime data
        dates (list): list of datetime.date objs
        hoodname (str): value for df['NEIGHBORHOOD_ID']
        category (str): value for df['OFFENSE_CATEGORY_ID']

    Returns:
        (Series): Counts of each offense category for this date and neighborhood
    """
    sub = df[
        (df['NEIGHBORHOOD_ID'] == hoodname) &
        (df['OFFENSE_CATEGORY_ID'] == category)
    ]
    resps = pd.DataFrame(columns=[category])
    for date in dates:
        subdate = sub[sub['REPORTED_DATE'] == date]
        resp = subdate.groupby('REPORTED_DATE').count().fillna(0)['INCIDENT_ID']
        if resp.shape[0] == 0:
            resp = pd.DataFrame({category: [0]}, index=[date])
        else:
            resp.name = date
            resp.index = [category]
        resps = resps.append(resp, sort=False)
    return(resps)

def main():
    """ Entry point.
    For testing purposes only.
    """
    if os.path.exists('data/processed/crime.pkl'):
        crime = pd.read_pickle('data/processed/crime.pkl')
    else:
        crime = pd.read_csv('data/raw/crime.csv', parse_dates=True)
        crime['REPORTED_DATE'] = pd.to_datetime(crime['REPORTED_DATE']).dt.normalize()
        crime.to_pickle('data/processed/crime.pkl')
    pred = make_predictors(
        crime,
        [dt.datetime.strptime('2018-04-22', '%Y-%m-%d'), 
         dt.datetime.strptime('2018-04-21', '%Y-%m-%d')],
        'stapleton',
        'burglary'
    )
    dates = pd.date_range(
            dt.datetime.strptime('2015-01-02', '%Y-%m-%d'),
            dt.datetime.strptime('2019-02-07', '%Y-%m-%d'), periods=500).normalize().tolist()
    resp = make_responses(
        crime, 
        dates,
        'stapleton',
        'burglary'
    )
    print(pred)
    print(resp)
    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()
