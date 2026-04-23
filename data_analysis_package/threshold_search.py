# This script searches through a dataframe for values in a given df column that exceed a specified threshold

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import data_download as dd
import download_iterator as di
import datetime
import run_analysis as ra

def threshold_search(column_name, threshold, url, start_date, end_date):
    """
    Searches through a dataframe for values in a given df column that exceed a specified threshold
    inputs:
    column_name (string): the column name of the variable you are filtering
    threshold (float): the value of the variable above which you want to filter for
    url: The url of the data website
    start_date: the start date, in the format yyyy,m,dd
    end_date: the end date, in the format yyyy,m,dd
    outputs: a df containing only rows with records above the threshold value
    """
    url = url
    dd.data_download(url)

    start_date = datetime.date(start_date)
    end_date = datetime.date(end_date)

    df = ra.combined_df(start_date, end_date)
    # print(df.columns)

    # Below is the code Will wrote to help me out. We're analyzing the Humidity column, and it looks like some values are entered as strings and others as floats.
    # Note: This would be good to add to the data download function

    count=0
    count_int=0
    for ii,vv in enumerate(df[column_name]):
        if type(vv)==int:
            count_int+=1
            continue
        else:
            print(vv, type(vv),ii)
            count+=1
    print(count, count_int)    

    
    for x in df[column_name]:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        print(df[column_name])

    # This is the threshold filter - should return a df containing all the rows in which the value exceeds the threshold in the given column.

    HS_df = []
    x = column_name
    thresh_mask = df[column_name] > threshold
    df[thresh_mask]

    # for x in df:
        # print(x)
        # if x["Hi_Speed"] > threshold:
        #     HS_df.append(x)
    print(HS_df)

if __name__ == '__main__':
print("Running tests...")
threshold = 60
column_name = "Hi_Speed"
url = "https://sundowner.colorado.edu/weather/atoc1/wxobs20211230.txt"
start_date = datetime.date(2021,12,1)
end_date = datetime.date(2021,12,31)
HS_df = threshold_search(column_name, threshold, url, start_date, end_date)
print(f"Days exceeding 60mph winds: {HS_df}")