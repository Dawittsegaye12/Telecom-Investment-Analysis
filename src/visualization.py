import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, columns):
    """
    Plots histograms for specified columns in the DataFrame.
    """
    df[columns].hist(figsize=(12, 8))
    plt.show()

def plot_boxplots(df, columns):
    """
    Plots boxplots for specified columns in the DataFrame.
    """
    sns.boxplot(data=df[columns])
    plt.show()

def plot_scatter(df, x_col, y_col):
    """
    Plots a scatter plot for the specified columns in the DataFrame.
    """
    sns.scatterplot(x=x_col, y=y_col, data=df)
    plt.show()