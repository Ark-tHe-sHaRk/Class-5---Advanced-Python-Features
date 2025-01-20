# Task 1: Create a list with all the odd numbers under the input value
input_value = int(input("Enter a number: "))
odd_numbers = [num for num in range(input_value) if num % 2 != 0]
print("Odd numbers under the input value:", odd_numbers)

# Task 2: Create a list of fruits and capitalize the first letter of each fruit
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "pear", "plum", "strawberry"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)