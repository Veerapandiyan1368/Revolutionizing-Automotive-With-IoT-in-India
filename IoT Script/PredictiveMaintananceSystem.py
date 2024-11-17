import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#Sample dataset loading (replace with actual data)
data = pd.read_csv('vehicle_maintenance.csv')
X = data[['temperature', 'fuel_usage', 'engine_hours', 'speed']]
#0 or 1
y = data['maintenance_required']
#Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Model training
model = LogisticRegression()
model.fit(X_train, y_train)
#Predict and evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
#Predicting maintenance for a new data point
#Example values
new_data = [[85, 5.6, 1000, 60]]
maintenance_prediction = model.predict(new_data)
print("Maintenance Required" if maintenance_prediction[0] == 1 else "No Maintenance Needed")