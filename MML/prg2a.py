import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv("C:\\Users\\sujan\\Downloads\\HeightWeight.csv")
heights = dataset['Height'].values.reshape(-1, 1)
weights = dataset['Weight'].values
heights_train, heights_test, weights_train, weights_test = train_test_split(
heights, weights, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(heights_train, weights_train)
weights_pred = model.predict(heights_test)
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
user_height = float(input("Enter the height in inches: "))
user_height_reshaped = np.array([[user_height]])
predicted_weight = model.predict(user_height_reshaped)[0]
print(f"Predicted weight for a height of {user_height} inches: {predicted_weight:.2f} pounds")
plt.scatter(heights_test, weights_test, color='black', label='Actual data')
plt.plot(heights_test, weights_pred, color='blue', linewidth=3, label='Regression line')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression: Height vs Weight')
plt.legend()
plt.savefig("ss.jpg")

plt.show()