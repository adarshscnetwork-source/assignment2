def check_even_odd():
    try:
        number = int(input("Enter an integer: "))

        if number % 2 == 0:
            result = "even"
        else:
            result = "odd"

        print(f"\nThe number {number} is {result}.")

    except ValueError:
        print("\nInvalid input. Please enter a whole number (integer) only.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    check_even_odd()