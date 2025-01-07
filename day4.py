# Taking input for the positive integer n
n = int(input("Enter a positive integer n: "))

# Initialize the sum to 0
sum_even_numbers = 0

# Loop through the numbers from 1 to n
for i in range(1, n+1):
    # Check if the number is even
    if i % 2 == 0:
        sum_even_numbers += i  # Add the even number to the sum

# Print the sum of all even numbers
print(f"The sum of all even numbers between 1 and {n} is: {sum_even_numbers}")
