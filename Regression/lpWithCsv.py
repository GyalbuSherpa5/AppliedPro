import csv
import numpy as np
from sklearn.linear_model import LinearRegression

# open the CSV file and read the data
with open('data.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)

# extract the X and Y values from the data
X = []
Y = []
for row in data:
  X.append(row[0])
  Y.append(row[1])

# convert the data to numpy arrays
X = np.array(X).reshape(-1, 1)
Y = np.array(Y).reshape(-1, 1)

# create the model and fit it to the data
model = LinearRegression()
model.fit(X, Y)

# get the slope and intercept of the best-fit line
m = model.coef_[0][0]
c = model.intercept_[0]

print(f"m = {m}")
print(f"c = {c}")
