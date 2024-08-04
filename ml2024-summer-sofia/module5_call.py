from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    # Input number of elements
    N = int(input("Enter the number of elements (N): "))
    processor.initialize(N)

    # Input N numbers
    for i in range(1, N + 1):
        number = int(input(f"Enter number {i}: "))
        processor.insert(i, number)

    # Input the number to find
    X = int(input("Enter the number to find (X): "))
    
    # Find and output the index or -1
    result = processor.find_index(X)
    print(result)

if __name__ == "__main__":
    main()
