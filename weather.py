import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Read training data from csv file
train_data = pd.read_csv("train.csv").dropna()

# Encode categorical label 'weather'
label_encoder = LabelEncoder()
train_data["weather"] = label_encoder.fit_transform(train_data["weather"])

# Split training data into features and labels
X_train = train_data.drop(columns=["date", "weather"])
y_train = train_data["weather"]

# Create and train a Random Forest classifier model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Read new data from csv file
new_data = pd.read_csv("final_test.csv")

# Make predictions on the new data
y_pred = model.predict(new_data.drop(columns="date"))

# Create a new DataFrame with the predicted 'weather' column
predicted_data = pd.DataFrame(
    {'weather': label_encoder.inverse_transform(y_pred)})

# Concatenate the predicted 'weather' column with the original new_data
new_data_predicted = pd.concat([new_data, predicted_data], axis=1)

# Save the complete predicted data to a new file
new_data_predicted.to_csv("syntax50_weather.csv", index=False)

# Evaluate model accuracy using cross-validation
mean_accuracy = model.score(X_train, y_train)
print("Mean Accuracy:", mean_accuracy)
