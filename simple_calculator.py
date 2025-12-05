# Simple script to calculate total and average

# Taking input from the user
numbers = input("Enter numbers separated by spaces: ")

# Converting the input string to a list of integers
num_list = [float(num) for num in numbers.split()]

# Processing
total = sum(num_list)
average = total / len(num_list)

# Output
print("\n--- Results ---")
print(f"Total: {total}")
print(f"Average: {average}")
