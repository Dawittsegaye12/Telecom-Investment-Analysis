import pandas as pd

def aggregate_user_data(df):
    """
    Aggregates user data including number of xDR sessions, session duration,
    total download (DL) and upload (UL) data, and total data volume for each user.
    """
    user_aggregates = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',  # Number of xDR sessions
        'Dur. (ms)': 'sum',  # Total Duration of the xDR in milliseconds
        'HTTP DL (Bytes)': 'sum',  # Total download data (HTTP)
        'HTTP UL (Bytes)': 'sum',  # Total upload data (HTTP)
        'Social Media DL (Bytes)': 'sum',  # Total download data (Social Media)
        'Social Media UL (Bytes)': 'sum',  # Total upload data (Social Media)
        'Youtube DL (Bytes)': 'sum',  # Total download data (YouTube)
        'Youtube UL (Bytes)': 'sum',  # Total upload data (YouTube)
        'Netflix DL (Bytes)': 'sum',  # Total download data (Netflix)
        'Netflix UL (Bytes)': 'sum',  # Total upload data (Netflix)
        'Google DL (Bytes)': 'sum',  # Total download data (Google)
        'Google UL (Bytes)': 'sum',  # Total upload data (Google)
        'Email DL (Bytes)': 'sum',  # Total download data (Email)
        'Email UL (Bytes)': 'sum',  # Total upload data (Email)
        'Gaming DL (Bytes)': 'sum',  # Total download data (Gaming)
        'Gaming UL (Bytes)': 'sum',  # Total upload data (Gaming)
        'Other DL (Bytes)': 'sum',  # Total download data (Other)
        'Other UL (Bytes)': 'sum',  # Total upload data (Other)
        'Total DL (Bytes)': 'sum',  # Total download data (All)
        'Total UL (Bytes)': 'sum'   # Total upload data (All)
    }).rename(columns={
        'Bearer Id': 'number_of_sessions',
        'Dur. (ms)': 'total_duration',
        'HTTP DL (Bytes)': 'total_http_dl',
        'HTTP UL (Bytes)': 'total_http_ul',
        'Social Media DL (Bytes)': 'total_social_media_dl',
        'Social Media UL (Bytes)': 'total_social_media_ul',
        'Youtube DL (Bytes)': 'total_youtube_dl',
        'Youtube UL (Bytes)': 'total_youtube_ul',
        'Netflix DL (Bytes)': 'total_netflix_dl',
        'Netflix UL (Bytes)': 'total_netflix_ul',
        'Google DL (Bytes)': 'total_google_dl',
        'Google UL (Bytes)': 'total_google_ul',
        'Email DL (Bytes)': 'total_email_dl',
        'Email UL (Bytes)': 'total_email_ul',
        'Gaming DL (Bytes)': 'total_gaming_dl',
        'Gaming UL (Bytes)': 'total_gaming_ul',
        'Other DL (Bytes)': 'total_other_dl',
        'Other UL (Bytes)': 'total_other_ul',
        'Total DL (Bytes)': 'total_dl',
        'Total UL (Bytes)': 'total_ul',
    })
    
    # Calculate total data volume
    user_aggregates['total_data_volume'] = user_aggregates['total_dl'] + user_aggregates['total_ul']
    
    return user_aggregates