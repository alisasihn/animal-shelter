import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing

tis_data = pd.read_csv('data/time_in_shelter.csv')


def convert_days(x):
    x = x / 30
    return float(x)


tis_data['time_in_shelter_days'] = tis_data['time_in_shelter_days'].apply(convert_days)
tis_data['age_upon_outcome_(days)'] = tis_data['age_upon_outcome_(days)'].apply(convert_days)

processed_data = preprocessing.scale(tis_data)

kmeans = KMeans(n_clusters=1)
kmeans.fit(processed_data)

cluster = tis_data.copy()
cluster['cluster_pred'] = kmeans.fit_predict(processed_data)

# x and y axis data for graph in main.py
x_scatter = cluster['age_upon_outcome_(days)']
y_scatter = cluster['time_in_shelter_days']

# find number of clusters with elbow graph
# score = []
# for i in range(1, 20):
#     kmeans = KMeans(i)
#     kmeans.fit(processed_data)
#     score.append(kmeans.inertia_)
#
# plt.plot(range(1, 20), score)
# plt.xlabel('# Clusters')
# plt.ylabel('Score')
# plt.show()

# plt.scatter(cluster['age_upon_outcome_(days)'], cluster['time_in_shelter_days'], c=cluster['cluster_pred'])
# plt.xlabel('Age (months)')
# plt.ylabel('Time in Shelter (months)')
# plt.show()
