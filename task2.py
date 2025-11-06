def calculate_sum():
    total_sum = 0

    for number in range(1, 51):
        total_sum += number

    print(f"The sum of all integers from 1 to 50 is: {total_sum}")

if __name__ == "__main__":
    calculate_sum()