import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare your data (reshape is required by scikit-learn)
X = np.array([2020, 2021, 2022, 2023, 2024]).reshape(-1, 1)
y = np.array([10000, 10800, 11900, 13200, 14800])

# 2. Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# 3. Predict for 2025
prediction = model.predict([[2025]])
print(f"Predicted population for 2025: {prediction[0]}")