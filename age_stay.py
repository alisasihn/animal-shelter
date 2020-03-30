import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing

data = pd.read_csv('data/shelter_intakes_outcomes_age_stay.csv')

x = data.copy()
X = data['age_upon_intake_(years)']
Y = data['time_in_shelter_days']

x_scaled = preprocessing.scale(x)

# elbow curve
score = []
for i in range(1, 20):
    kmeans = KMeans(i)
    kmeans.fit(x_scaled)
    score.append(kmeans.inertia_)

plt.plot(range(1, 20), score)
plt.xlabel('# Clusters')
plt.ylabel('Score')
plt.show()

# plot
kmeans = KMeans(5)
kmeans.fit(x)

clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)

plt.scatter(clusters['age_upon_intake_(years)'], clusters['time_in_shelter_days'], c=clusters['cluster_pred'],
            cmap='rainbow')
plt.xlabel('Age (Years)')
plt.ylabel('Length of Stay (Days)')
plt.show()
