import datetime
import numpy as np
import pandas as pd


def no_nonsense(df):
    """
    TODO: this function should resolve issue #9
    NOTE: It is possible that this function is not necessary.
        if that is the case, your PR should be to remove this function
        and the call to this function from this script.
    https://github.com/the4thparadigm/denvercrime/issues/9
    TODO: write a docstring explaining your approach
    NOTE: Do not hesitate to add other functions if you find it appropriate.
        Be sure to add calls to any additional functions either here or in 
        main().
    TODO: submit a PR with your changes to this file

    Preconditions:
        no_incomplete() has already been called on df.

    Parameters:
        df (DataFrame): crime data

    Returns:
        (DataFrame): crime data without nonsensical events
    """
    return df

def no_incomplete(df):
    """
    TODO: this function should resolve issue #8
    https://github.com/the4thparadigm/denvercrime/issues/8
    TODO: write a docstring explaining your approach
    NOTE: Do not hesitate to add other functions if you find it appropriate.
        Be sure to add calls to any additional functions either here or in 
        main().
    TODO: submit a PR with your changes to this file

    Parameters:
        df (DataFrame): crime data

    Returns:
        (DataFrame): crime data without incomplete events
    """
    return df


def main():
    """ Entry point.
    Calls no_nonsense() and no_incomplete() and saves the
    result in data/processed/cleaned.csv
    """
    crime = pd.read_csv('data/raw/crime.csv')
    crime = no_incomplete(crime)
    crime = no_nonsense(crime)
    crime.to_csv('data/processed/cleaned.csv', index=False)

if __name__ == '__main__':
    main()
    