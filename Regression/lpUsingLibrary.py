from sklearn.linear_model import LinearRegression
import numpy as np

# sample points
X = [0, 1, 2, 3, 4]
Y = [2, 3, 5, 4, 6]

# reshape the input data to make it suitable for the model
X = np.array(X).reshape(-1, 1)
Y = np.array(Y).reshape(-1, 1)

# create the model and fit it to the data
model = LinearRegression()
model.fit(X, Y)

# get the slope and intercept of the best-fit line
m = model.coef_[0][0]
c = model.intercept_[0]

print(f"m = {round(m,2)}")
print(f"c = {round(c,2)}")