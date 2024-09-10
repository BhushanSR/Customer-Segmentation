income = int(input("Enter the Annual Income(k$):"))
spend = int(input("Enter the Spend Score: "))

import joblib

model = joblib.load("KMeans_Cluster")
cluster = model.predict([[income,spend]])

print(f"Customer belongs to => Cluster{cluster}")