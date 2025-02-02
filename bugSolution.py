def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [10,0,20,30,40,50]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average is: {average_with_zero}")

my_list_with_string = [10, 20, 'a', 30, 40, 50]
average_with_string = calculate_average(my_list_with_string)
print(f"The average with a string is: {average_with_string}") #this will print the average of numbers in the list