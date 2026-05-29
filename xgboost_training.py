import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)



from xgboost import XGBClassifier

# load dataset
df = pd.read_csv(
    "data/processed/labeled_dataset.csv"
)

print(df.shape)

df.head()


# features and labels

X = df.drop(
    columns=["quality_score", "label"]
)

y = df["label"]



# Encode labels
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

print(encoder.classes_)



# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

print(len(X_train))
print(len(X_test))



# Model
model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    n_jobs=-1
)


# Train model
print("Training XGBoost...")

model.fit(X_train, y_train)

print("Training Completed!")



# predict
preds = model.predict(X_test)


# Evaluation
accuracy = accuracy_score(
    y_test,
    preds
)

print("Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        preds
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        preds
    )
)


# save model
joblib.dump(
    model,
    "models/xgboost.pkl"
)

print("Model Saved!")
