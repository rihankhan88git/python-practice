import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
df = pd.read_csv("loan_dataset.csv")

print(df)

# Understand data
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

print(df)
print(df.duplicated().sum())


# EDA
plt.figure(figsize=(10, 6))

plt.scatter(df["income"], df["loan_amount"])

plt.xlabel("Income")
plt.ylabel("Loan Amount")
plt.title("Income vs Loan Amount")

plt.show()

# Features
X = df[
    [
        "age",

        "income",
        "loan_amount",
        "credit_score",
        "employment_years",
        "existing_loans",
        "debt_to_income"
    ]
]

# Target
y = df["loan_status"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create ML model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)


# Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save trained model
with open("loan_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully as loan_model.pkl")