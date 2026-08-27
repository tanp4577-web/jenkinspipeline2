import sys

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Missing required arguments.")
        print("Usage: python add.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be integers.")
        sys.exit(1)

    result = add_numbers(num1, num2)
    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum          : {result}")