# Utility functions for processing NIPS reviews.
import datetime as dt
import pandas as pd
from datetime import timedelta
import numpy as np
import os

from cmtutils.config import *

# Date of different review events.
events = {}
# Time stamps from CMT are on separate time? If so add here
offset = dt.timedelta(hours=0)
events['reviews'] = dt.datetime(2014, 7, 21, 23, 59) + offset
events['rebuttal_start'] = dt.datetime(2014, 8, 3, 23, 59) + offset
events['rebuttal_ends'] = dt.datetime(2014, 8, 11, 23, 59) + offset
events['start_teleconference'] = dt.datetime(2014, 8, 19, 23, 59) +offset
events['decisions_despatched'] = dt.datetime(2014, 9, 5, 23, 59) + offset

# Date range across which we have review information.
review_date_range = pd.date_range('2014/07/01', periods=72, freq='D')
review_store = os.path.expandvars(config.get('review data', 'directory'))
review_file = os.path.expandvars(config.get('review data', 'file'))

def load_review_history():
    """Load in the history of the NIPS reviews."""

    # return load of pickled reviews.
    return pd.io.pickle.read_pickle(os.path.join(review_store, review_file))

def reviews_before(reviews, date):
    "Give a review snapshot of reviews before a certain date."
    indices = (((reviews.LastUpdated<=date) & (reviews.LastSeen>date))
               | ((reviews.LastUpdated<=date) & (reviews.LastSeen.isnull())))
    return reviews[indices].sort_values(by='LastUpdated').drop_duplicates(subset=['Email', 'ID'], keep='last')

def reviews_status(reviews, datetime, column=None):
    """Give a snapshot of the reviews at any given time. Use multi-index across ID
    and Email"""

    if column is not None:
        return reviews_before(reviews, datetime).set_index(['ID', 'Email'])[column].sort_index()
    else:
        return reviews_before(reviews, datetime).set_index(['ID', 'Email']).sort_index()





def late_early_values(reviews, column):
    "Compute a statistic for late reviews and a statistic for early reviews"
    first_entered = reviews.sort_values(by='LastUpdated', ascending=False).drop_duplicates(subset=['ID', 'Email'],keep='last').sort_values(by='LastUpdated')
    cat1 = first_entered[column][first_entered.LastUpdated<events['reviews']]
    cat2 = first_entered[column][(first_entered.LastUpdated>events['reviews'])& (first_entered.LastUpdated < events['rebuttal_start'])]

    return cat1, cat2


# def top_papers(reviews):
#     """Compute the top review levels."""
#     for date in review_date_range:
        
