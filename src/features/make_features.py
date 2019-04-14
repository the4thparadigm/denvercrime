import numpy as np
import pandas as pd

def make_predictors(df, date, hood):
    """ Create predictor variables.
    TODO: this function should resolve issue #27
    https://github.com/the4thparadigm/denvercrime/issues/27
    TODO: write a docstring explaining your approach
    TODO: submit a PR with your changes to this file

    Parameters:
        df (DataFrame): crime data
        date (datetime.date): value for df['REPORTED_DATE']
        hood (str): value for df['NEIGHBORHOOD_ID']

    Returns:
        (Series): Counts of different combinations of date, offense type, and location

    """
    return None

def make_responses(df, date, hood):
    """ Create response variables.
    TODO: this function should resolve issue #28
    https://github.com/the4thparadigm/denvercrime/issues/28
    TODO: write a docstring explaining your approach
    TODO: submit a PR with your changes to this file

    Parameters:
        df (DataFrame): crime data
        date (datetime.date): value for df['REPORTED_DATE']
        hood (str): value for df['NEIGHBORHOOD_ID']

    Returns:
        (Series): Counts of each offense category for this date and neighborhood
    """
    return None

def main():
    """ Entry point.
    Calls predictors() and responses() and saves the
    result in data/processed/features.csv
    """
    crime = pd.read_csv('data/raw/crime.csv')
    # make_predictors(crime).to_csv('data/processed/predictors.csv', index=False)
    # make_responses(crime).to_csv('data/processed/responses.csv', index=False)

if __name__ == '__main__':
    main()
