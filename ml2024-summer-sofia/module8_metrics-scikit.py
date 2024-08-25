import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask the user for input N (positive integer)
    try:
        N = int(input("Enter the number of points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Initialize lists to hold the true labels (X) and predicted labels (Y)
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    print("Enter the points (x, y) one by one:")

    # Read N points from the user
    for i in range(N):
        try:
            x = int(input(f"Point {i+1} - Enter x value (0 or 1): "))
            y = int(input(f"Point {i+1} - Enter y value (0 or 1): "))
            
            if x not in (0, 1) or y not in (0, 1):
                raise ValueError("x and y values must be either 0 or 1.")
            
            X[i] = x
            Y[i] = y
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

    # Calculate Precision and Recall using scikit-learn
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    # Output the results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
