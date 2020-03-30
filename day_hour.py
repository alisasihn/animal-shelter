import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing

data = pd.read_csv('data/shelter_intakes_outcomes_day_hour.csv')

x = data.copy()
X = data['intake_weekday']
Y = data['intake_hour']

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
kmeans = KMeans(3)
kmeans.fit(x)

clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)

plt.scatter(clusters['intake_weekday'], clusters['intake_hour'], c=clusters['cluster_pred'],
            cmap='rainbow')
plt.xlabel('Weekday')
plt.ylabel('Hour')
plt.show()
