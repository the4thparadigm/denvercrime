import datetime as dt
import numpy as np
import pandas as pd
import pdb

def make_predictors(df, date, hood):
    """ Create predictor variables.

    Parameters:
        df (DataFrame): crime data
        dates (datetime.date): datetime.date obj; date to predict
        hood (str): value for df['NEIGHBORHOOD_ID']

    Returns:
        (DataFrame): Rows are indexed by predictions, columns are features (counts for different intervals)
    """
    sub = df[
        (df['REPORTED_DATE'] < date) & 
        (df['NEIGHBORHOOD_ID'] == hood)
    ]

    day = sub[
        sub['REPORTED_DATE'] > (date - dt.timedelta(days=1))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    week = sub[
        sub['REPORTED_DATE'] > (date - dt.timedelta(days=7))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    month = sub[
        sub['REPORTED_DATE'] > (date - dt.timedelta(days=30))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    year = sub[
        sub['REPORTED_DATE'] > (date - dt.timedelta(days=365))
    ].groupby('OFFENSE_CATEGORY_ID').count()['INCIDENT_ID']

    return pd.concat(
        [day,week,month,year],
        keys=['day', 'week', 'month', 'year'],
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
        (df['OFFENSE_TYPE_ID'] == type)
    ]
    return sub.groupby('REPORTED_DATE').count()

def main():
    """ Entry point.
    For testing purposes only.
    """
    crime = pd.read_csv('data/raw/crime.csv', parse_dates=True)
    crime['REPORTED_DATE'] = pd.to_datetime(crime['REPORTED_DATE']).dt.normalize()
    test = make_predictors(
        crime,
        dt.datetime.strptime('2018-04-22', '%Y-%m-%d'),
        'stapleton'
    )
    print(test)

if __name__ == '__main__':
    main()
