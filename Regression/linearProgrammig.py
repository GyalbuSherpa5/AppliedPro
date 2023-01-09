# sample points
X = [0, 1, 2, 3, 4]
Y = [2, 3, 5, 4, 6]

# solve for a and b
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    covariance = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    variance = sum([xi**2 for xi in X]) - n * xbar**2

    b = covariance / variance
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# solution
a, b = best_fit(X, Y)
print(f"m = {b}")
print(f"c = {round(a,2)}")
#best fit line:
#y = 0.80 + 0.92x

# plot points and fit line
# import matplotlib.pyplot as plt
# plt.scatter(X, Y)
# yfit = [a + b * xi for xi in X]
# plt.plot(X, yfit)