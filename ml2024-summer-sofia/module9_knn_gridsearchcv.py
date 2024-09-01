import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def main():
    # Read the number of training examples
    N = int(input("Enter the number of training examples (N): "))
    TrainS = []
    
    # Read training examples
    print("Enter the training pairs (x, y) one by one:")
    for _ in range(N):
        x = float(input("Enter x value: "))
        y = int(input("Enter y value: "))
        TrainS.append((x, y))
    
    TrainS = np.array(TrainS)
    X_train = TrainS[:, 0].reshape(-1, 1)  # Feature matrix
    y_train = TrainS[:, 1]  # Labels
    
    # Read the number of test examples
    M = int(input("Enter the number of test examples (M): "))
    TestS = []
    
    # Read test examples
    print("Enter the test pairs (x, y) one by one:")
    for _ in range(M):
        x = float(input("Enter x value: "))
        y = int(input("Enter y value: "))
        TestS.append((x, y))
    
    TestS = np.array(TestS)
    X_test = TestS[:, 0].reshape(-1, 1)  # Feature matrix
    y_test = TestS[:, 1]  # Labels
    
    # Initialize the kNN classifier
    knn = KNeighborsClassifier()
    
    # Define the range of k values to test
    param_grid = {'n_neighbors': list(range(1, 11))}
    
    # Initialize GridSearchCV with kNN classifier and the parameter grid
    grid_search = GridSearchCV(knn, param_grid, cv=3, scoring='accuracy')
    
    # Fit the GridSearchCV to the training data
    grid_search.fit(X_train, y_train)
    
    # Get the best k value from the GridSearchCV
    best_k = grid_search.best_params_['n_neighbors']
    
    # Use the best k value to predict on the test set
    best_knn = grid_search.best_estimator_
    y_pred = best_knn.predict(X_test)
    
    # Calculate the test accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Output the results
    print(f"The best k for the kNN Classification method is: {best_k}")
    print(f"The corresponding test accuracy is: {accuracy:.2f}")

if __name__ == "__main__":
    main()
