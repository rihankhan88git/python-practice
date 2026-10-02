import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("dataset.csv")
print(df)
# Understand data
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# check missing values
print(df.isnull().sum())

# Check Duplicate records
# print(df.duplicated().sum())
df = df.drop_duplicates()

print(df)
print(df.duplicated().sum())

# Create EDA (understanding relationships between our features and house price.)

plt.figure(figsize=(8,5))
plt.scatter(df["area"], df["price"])

plt.xlabel("area")
plt.ylabel("price")
plt.title("Area vs House Price")

plt.show()

# Split DataSet (80-20 formula)
# Define independent and dependent variables
# x = input and y = output

x = df[["area", "bedrooms", "bathrooms", "age"]]
y = df["price"]


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42
                                                )

# check train and test data frame shapes
print("X_Train:", x_train.shape)
print("X_Test:", x_test.shape)

print("Y_Train:", y_train.shape)
print("Y_Test:", y_test.shape)

# Create model
model = LinearRegression()

# Model Training
model.fit(x_train, y_train)

# Make Predications
y_predict = model.predict(x_test)
print(y_predict)
df = pd.DataFrame({
    "Actual Price": y_test,
    "Predicted Price": y_predict
})

print(df)


# Test with new data
new_house = pd.DataFrame({
    "area": [1770],
    "bedrooms": [3],
    "bathrooms": [3],
    "age": [5]
})

predicted_price = model.predict(new_house)
print("Predicated House Price : ", predicted_price)

## save model

with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("*********** Model Saved to Pickle file ************")



