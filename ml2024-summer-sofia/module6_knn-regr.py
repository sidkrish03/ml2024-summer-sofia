import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Ask the user for input N and k
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the number of neighbors (k): "))
    
    # Validate k
    if k > N:
        print("Error: k cannot be greater than N.")
        return
    
    # Initialize lists to store data points
    X = []
    Y = []

    # Read N (x, y) points from the user
    print(f"Enter {N} data points (x, y) one by one:")
    for _ in range(N):
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        X.append(x)
        Y.append(y)
    
    # Convert lists to numpy arrays
    X = np.array(X).reshape(-1, 1)  # Reshape for sklearn
    Y = np.array(Y)
    
    # Create and train the k-NN regression model
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X, Y)
    
    # Ask the user for input X value and predict the corresponding Y value
    x_input = float(input("Enter the x value for prediction: "))
    
    # Predict the Y value using k-NN regression
    y_pred = model.predict([[x_input]])
    
    # Output the result
    print(f"The predicted Y value for X={x_input} is: {y_pred[0]}")

if __name__ == "__main__":
    main()
