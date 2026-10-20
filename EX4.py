# Simple Linear Regression for House Price Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create Dataset (Area vs Price)
data = {
    'Area': [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2700, 3000],
    'Price': [150000, 200000, 240000, 300000, 360000, 400000, 440000, 500000, 540000, 600000]
}

df = pd.DataFrame(data)

# Step 2: Define X (feature) and y (target)
X = df[['Area']]
y = df['Price']

# Step 3: Train the Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict house price
area = np.array([[1900]])  # new house area
predicted_price = model.predict(area)

print("Predicted Price for 1900 sq ft house:", predicted_price[0])

# Step 5: Plot the regression line
plt.scatter(X, y)
plt.plot(X, model.predict(X))

plt.title("Simple Linear Regression - House Price Prediction")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.show()