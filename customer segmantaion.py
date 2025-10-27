# customer_segmentation.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("customers.csv")
print("Loaded", len(df), "rows")
print(df.head())

# 2. Select features
X = df[['Age','Income','SpendingScore']]

# 3. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Create and fit KMeans
k = 4
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. Plot Income vs SpendingScore colored by cluster
plt.figure(figsize=(8,6))
plt.scatter(df['Income'], df['SpendingScore'], c=df['Cluster'], cmap='tab10', s=60)
plt.xlabel('Income')
plt.ylabel('SpendingScore')
plt.title('Customer Clusters')
plt.show()

# 6. Print summary
print("\nCluster counts:")
print(df['Cluster'].value_counts())
print("\nCluster means:")
print(df.groupby('Cluster')[['Age','Income','SpendingScore']].mean().round(2))
