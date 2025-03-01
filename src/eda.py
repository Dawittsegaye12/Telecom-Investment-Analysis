import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def describe_variables(df):
    """
    Returns a description of variables and their data types.
    """
    return df.info()

def segment_users_by_duration(df, user_aggregates):
    """
    Segments users into decile classes based on session duration
    and computes total data per decile class.
    """
    df['decile'] = pd.qcut(user_aggregates['total_duration'], 10, labels=False) + 1
    total_data_per_decile = df.groupby('decile').agg({
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum',
    }).rename(columns={'Total DL (Bytes)': 'total_dl', 'Total UL (Bytes)': 'total_ul'})
    
    return total_data_per_decile

def compute_basic_metrics(df):
    """
    Computes basic metrics such as mean, median, etc., for the dataset.
    """
    return df.describe()

def compute_dispersion_parameters(df):
    """
    Computes dispersion parameters like variance and standard deviation.
    """
    return df[['total_duration', 'total_dl', 'total_ul']].agg(['mean', 'std', 'var'])

def plot_univariate_analysis(df):
    """
    Plots histograms and boxplots for univariate analysis.
    """
    # Histograms
    df[['session_duration', 'download_data', 'upload_data']].hist(figsize=(12, 8))
    plt.show()

    # Boxplots
    sns.boxplot(data=df[['session_duration', 'download_data', 'upload_data']])
    plt.show()

def plot_bivariate_analysis(df):
    """
    Plots scatter plots for bivariate analysis.
    """
    sns.scatterplot(x='total_data_volume', y='application', data=df)
    plt.show()

def compute_correlation_matrix(df):
    """
    Computes and returns the correlation matrix for selected variables.
    """
    return df[['total_social_media_dl', 'total_google_dl', 'total_email_dl', 'total_youtube_dl', 'total_netflix_dl', 'total_gaming_dl', 'total_other_dl']].corr()

def perform_pca(df):
    """
    Performs Principal Component Analysis (PCA) and returns the PCA result and explained variance.
    """
    pca = PCA(n_components=2)  # Reducing to 2 components for visualization
    data_for_pca = df[['total_social_media_dl', 'total_google_dl', 'total_email_dl', 'total_youtube_dl', 'total_netflix_dl', 'total_gaming_dl', 'total_other_dl']]
    pca_result = pca.fit_transform(data_for_pca)

    # Create a DataFrame for PCA results
    pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
    return pca_df, pca.explained_variance_ratio_, pca.components_