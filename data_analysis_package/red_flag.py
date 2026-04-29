from data_download import data_download

def identify_red_flag_days(df, start_date, end_date):

    """
    identifies red flag days, as defined by certain thresholds:
    wind gusts > 24 mph 
    relative humidity < 15%
    
    """
    
    rf_days_list = []

    df = df[(df.index >= start_date) & (df.index <= end_date)]

    wind_col = "MaxWS"
    rh_col = "MinRH"

    #ONLY LOOKING AT CERTAIN CONDITIONS 
    conditions = (df[wind_col] > 24) & (df[rh_col] < 15)

    rf_days_list = list(df[conditions].index.date)

    return sorted(set(rf_days_list))


if __name__ == "__main__":
    url = "https://sundowner.colorado.edu/weather/atoc1/wxobs20211230.txt" #currently your data downloader only accepts 'text' files, so can not go through entire daily data since it is a 'grf' file
    df = data_download(url)
    rf_days = identify_red_flag_days(df, "2021-12-01", "2024-12-31")
    print(rf_days)
  

    


