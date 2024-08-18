import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def main():
    # Read input N
    N = int(input("Enter the number of points N: "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Read input k
    k = int(input("Enter the value of k: "))
    if k <= 0:
        print("Error: k must be a positive integer.")
        return

    # Initialize lists for data points
    X_train = []
    y_train = []

    # Read N points
    print("Enter the points (x y) one by one:")
    for _ in range(N):
        x = float(input("x: "))
        y = float(input("y: "))
        X_train.append([x])
        y_train.append(y)

    # Convert lists to numpy arrays
    X_train = np.array(X_train)
    y_train = np.array(y_train)

    # Compute and print variance of labels in the training dataset
    variance = np.var(y_train)
    print(f"Variance of labels in the training dataset: {variance}")

    # Read input X for prediction
    X_pred = float(input("Enter the value of X for prediction: "))
    X_pred = np.array([[X_pred]])

    if k > N:
        print("Error: k must be less than or equal to N.")
        return

    # Create and train the k-NN regressor
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)

    # Predict the value for the given X
    y_pred = knn_regressor.predict(X_pred)
    print(f"Predicted value for X = {X_pred[0][0]}: {y_pred[0]}")

if __name__ == "__main__":
    main()
