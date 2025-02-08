def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Improved Solution
def calculate_average_improved(numbers):
    if not numbers:
        return 0  # Handle empty list explicitly
    return sum(numbers) / len(numbers)

my_numbers = [1,2,3,4,5]
print(f"The average is: {calculate_average_improved(my_numbers)}")

my_empty_list = []
print(f"The average of the empty list is: {calculate_average_improved(my_empty_list)}") 