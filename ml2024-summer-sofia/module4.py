def find_number_index(numbers, X):
    """Returns the 1-based index of X if found in numbers, otherwise -1."""
    if X in numbers:
        return numbers.index(X) + 1
    else:
        return -1

def main():
    # Ask the user for input N
    N = int(input("Enter the number of elements (N): "))

    # Initialize an empty list to store the N numbers
    numbers = []

    # Read N numbers from the user
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Ask the user for input X
    X = int(input("Enter the number to find (X): "))

    # Get the result and print it
    result = find_number_index(numbers, X)
    print(result)

if __name__ == "__main__":
    main()