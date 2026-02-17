# Polynomial Features vs Simple Linear Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# -------------------- Create Non-Linear Dataset --------------------
np.random.seed(0)
X = np.linspace(-10, 10, 200).reshape(-1, 1)
y = 3 * X.flatten()**2 + 2 * X.flatten() + 5 + np.random.normal(0, 20, 200)

# -------------------- Linear Regression (Original Feature) --------------------
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)

# -------------------- Polynomial Features (Degree 2) --------------------
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

# -------------------- Plot 1: Linear Fit --------------------
plt.figure()
plt.suptitle("Linear Vs Polynomial Regression")

plt.subplot(1,2,1)
plt.scatter(X, y)
plt.plot(X, y_pred_linear)
plt.title("Linear Regression Fit")
plt.xlabel("Feature")
plt.ylabel("Target")

# -------------------- Plot 2: Polynomial Fit --------------------
plt.subplot(1,2,2)
plt.scatter(X, y)
plt.plot(X, y_pred_poly)
plt.title("Polynomial Regression Fit (Degree=2)")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()

# -------------------- Print R2 Scores --------------------
print("R² Score using Original Linear Feature:", round(r2_linear, 4))
print("R² Score using Polynomial Features (degree=2):", round(r2_poly, 4))

if r2_poly > r2_linear:
    print("\nPolynomial features improved the model by capturing the curve in the data.")
else:
    print("\nPolynomial features did not improve the model.")