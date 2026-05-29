import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# Load Dataset

df = pd.read_csv(
    "data/processed/labeled_dataset.csv"
)

print("Dataset Loaded!")
print(df.shape)


# Features and Labels

X = df.drop(
    columns=["quality_score", "label"]
)

y = df["label"]

# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# Create Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# Train Model
print("Training model...")

model.fit(X_train, y_train)

print("Training completed!")


# Predictions
preds = model.predict(X_test)


# Evaluation

accuracy = accuracy_score(y_test, preds)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, preds))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, preds))


# Save Model

os.makedirs(
    "models",
    exist_ok=True
)

joblib.dump(
    model,
    "models/random_forest.pkl"
)

print("\nModel saved successfully!")