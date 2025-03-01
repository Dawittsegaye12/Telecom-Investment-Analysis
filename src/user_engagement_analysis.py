import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

#Aggregate engagement metrics per customer
def aggregate_engagement_metrics(data):
    engagement_metrics = data.groupby('Bearer Id').agg({
        'Bearer Id': 'count',
        'Dur. (ms)': 'sum',
        'Total UL (Bytes)': 'sum',
        'Total DL (Bytes)': 'sum',
    }).rename(columns={'Bearer Id':'sessions frequency',
                       'Dur. (ms)':'session duration',})
    engagement_metrics["total_traffic"]=engagement_metrics["Total DL (Bytes)"] + engagement_metrics["Total UL (Bytes)"]
    return engagement_metrics

#Normalize engagement metrics
def normalize_metrics(engagement_metrics):
    scaler = StandardScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(engagement_metrics[['sessions frequency', 'session duration', 'total_traffic']]), 
                                   columns=['sessions frequency', 'session duration', 'total_traffic'])
    return normalized_data

#Apply K-Means clustering
def apply_kmeans(normalized_data, k=3):
    kmeans = KMeans(n_clusters=k, random_state=0)
    normalized_data['Cluster'] = kmeans.fit_predict(normalized_data)
    return normalized_data, kmeans

#Calculate cluster statistics
def compute_cluster_stats(normalized_data, original_data):
    cluster_stats = original_data.groupby(normalized_data['Cluster']).agg({
        'sessions frequency': ['min', 'max', 'mean', 'sum'],
        'session duration': ['min', 'max', 'mean', 'sum'],
        'total_traffic': ['min', 'max', 'mean', 'sum']
    }).reset_index()
    return cluster_stats

#Plot engagement results
def plot_engagement_clusters(normalized_data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sessions frequency', y='total_traffic', hue='Cluster', data=normalized_data, palette='Set1')
    plt.title('Engagement Clusters')
    plt.show()

#Determine optimal K value using elbow method
def elbow_method(normalized_data):
    distortions = []
    K = range(1, 10)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(normalized_data)
        distortions.append(kmeans.inertia_)
    
    plt.figure(figsize=(8, 5))
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()