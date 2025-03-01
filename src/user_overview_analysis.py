def get_top_10_handsets(df):
    """
    This function returns the top 10 most used handsets in the dataset.
    """
    top_10_handsets = df['Handset Type'].value_counts().head(10)
    return top_10_handsets

def get_top_3_manufacturers(df):
    """
    This function returns the top 3 handset manufacturers in the dataset.
    """
    top_3_manufacturers = df['Handset Manufacturer'].value_counts().head(3)
    return top_3_manufacturers

def get_top_5_handsets_per_manufacturer(df, top_3_manufacturers):
    """
    This function returns the top 5 handsets for each of the top 3 manufacturers.
    """
    top_5_handsets_per_manufacturer = {}
    
    for manufacturer in top_3_manufacturers.index:
        top_5_handsets = df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        top_5_handsets_per_manufacturer[manufacturer] = top_5_handsets
    
    return top_5_handsets_per_manufacturer