import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

import matplotlib.pyplot as plt
import seaborn as sns

# ============================================
# step 1  load dataset
# ===========================================
df = pd.read_csv("dataset.csv",sep=";")
print(df)


# ==========================================================
#  STEP 2: UNDERSTAND DATA
#  ==========================================================

print("\n================ STEP 2: DATA UNDERSTANDING ================\n")

print("\nFirst 5 records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Information:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# ==========================================================
# STEP 4: REMOVE MISSING VALUES
# ==========================================================

# print("\n================ STEP 4: HANDLE MISSING VALUES ================\n")
#
# df = df.dropna()
#
# print("Dataset Shape After Removing Missing Values:")
# print(df.shape)

# ================= STEP 4: HANDLE MISSING VALUES =================

df = df.dropna()

# IMPORTANT: Remove leading/trailing spaces
df["label"] = df["label"].str.strip()

print("Dataset Shape After Removing Missing Values:")
print(df.shape)


# Check labels
print("\nCleaned Labels:")
print(df["label"].unique())

print("\nClass Distribution:")
print(df["label"].value_counts())
# ==========================================================
# STEP 5: CHECK TARGET DISTRIBUTION
# ==========================================================

print("\n================ STEP 5: CLASS DISTRIBUTION ================\n")

print(df["label"].value_counts())

print("\n================ STEP 6: FEATURES AND TARGET ================\n")

X = df["message"]
y = df["label"]

print("X sample:")
print(X.head())

print("\ny sample:")
print(y.head())

# ==========================================================
# STEP 7: TRAIN TEST SPLIT
# ==========================================================

print("\n================ STEP 7: TRAIN TEST SPLIT ================\n")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================================
# STEP 8: TF-IDF VECTORIZATION
# ==========================================================

print("\n================ STEP 8: TF-IDF ================\n")

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)

print("TF-IDF Training Shape:")
print(X_train_tfidf.shape)

print("\nTF-IDF Testing Shape:")
print(X_test_tfidf.shape)


# ==========================================================
# STEP 9: CREATE LOGISTIC REGRESSION MODEL
# ==========================================================

print("\n================ STEP 9: LOGISTIC REGRESSION ================\n")

model = LogisticRegression(
    max_iter=1000
)

print("Model created successfully.")

# ==========================================================
# STEP 10: TRAIN MODEL
# ==========================================================

print("\n================ STEP 10: MODEL TRAINING ================\n")

model.fit(
    X_train_tfidf,
    y_train
)

print("Model training completed successfully.")

# ==========================================================
# STEP 11: PREDICTION
# ==========================================================

print("\n================ STEP 11: PREDICTION ================\n")

y_pred = model.predict(X_test_tfidf)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

# ==========================================================
# STEP 12: PROBABILITY
# ==========================================================

print("\n================ STEP 12: PREDICTION PROBABILITY ================\n")

y_probability = model.predict_proba(X_test_tfidf)

print(y_probability)

# ==========================================================
# STEP 13: ACCURACY
# ==========================================================

print("\n================ STEP 13: ACCURACY ================\n")

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

# ==========================================================
# STEP 14: PRECISION
# ==========================================================

print("\n================ STEP 14: PRECISION ================\n")

precision = precision_score(
    y_test,
    y_pred,
    pos_label="spam",
    zero_division=0
)

print("Precision:", precision)

# ==========================================================
# STEP 15: RECALL
# ==========================================================

print("\n================ STEP 15: RECALL ================\n")

recall = recall_score(
    y_test,
    y_pred,
    pos_label="spam",
    zero_division=0
)

print("Recall:", recall)

# ==========================================================
# STEP 16: F1 SCORE
# ==========================================================

print("\n================ STEP 16: F1 SCORE ================\n")

f1 = f1_score(
    y_test,
    y_pred,
    pos_label="spam",
    zero_division=0
)

print("F1 Score:", f1)

# ==========================================================
# STEP 17: CLASSIFICATION REPORT
# ==========================================================

print("\n================ STEP 17: CLASSIFICATION REPORT ================\n")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

# ==========================================================
# STEP 18: CONFUSION MATRIX
# ==========================================================

print("\n================ STEP 18: CONFUSION MATRIX ================\n")

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=["ham", "spam"]
)

print(cm)

# ==========================================================
# STEP 19: CONFUSION MATRIX VISUALIZATION
# ==========================================================

print("\n================ STEP 19: CONFUSION MATRIX GRAPH ================\n")

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=["Ham", "Spam"],
    yticklabels=["Ham", "Spam"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Spam Detection - Confusion Matrix")

plt.show()

# ==========================================================
# STEP 20: TEST NEW EMAILS
# ==========================================================

print("\n================ STEP 20: TEST NEW EMAILS ================\n")

new_emails = [
    "Congratulations! You won a free cash prize. Click now",
    "Please send me the project report tomorrow",
    "URGENT! Claim your free reward now",
    "Can we meet tomorrow for the project discussion?"
]

new_emails_tfidf = vectorizer.transform(new_emails)

new_predictions = model.predict(new_emails_tfidf)

new_probabilities = model.predict_proba(new_emails_tfidf)


for email, prediction, probability in zip(
    new_emails,
    new_predictions,
    new_probabilities
):

    print("\nEmail:")
    print(email)

    print("Prediction:")
    print(prediction)

    # Find probability of SPAM
    spam_index = list(model.classes_).index("spam")

    spam_probability = probability[spam_index]

    print(
        "Spam Probability:",
        round(spam_probability * 100, 2),
        "%"
    )

# ==========================================================
# STEP 21: SAVE MODEL
# ==========================================================

print("\n================ STEP 21: SAVE MODEL ================\n")

model_data = {
    "model": model,
    "vectorizer": vectorizer
}

with open("spam_model.pkl", "wb") as file:

    pickle.dump(
        model_data,
        file
    )

print("Model saved successfully!")

print("\nFile created:")
print("spam_model.pkl")


# ==========================================================
# PROJECT COMPLETED
# ==========================================================

print("\n==========================================================")
print("       SPAM EMAIL DETECTION PROJECT COMPLETED")
print("==========================================================")


