# Function 1: Add two numbers
def add(a, b):
    return a + b

# Function 2: Subtract two numbers
def subtract(a, b):
    return a - b

# Function 3: Multiply two numbers
def multiply(a, b):
    return a * b

# Function 4: Divide two numbers (with error handling for division by zero)
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Function 5: Find the maximum of two numbers
def find_max(a, b):
    return max(a, b)

# Function 6: Find the minimum of two numbers
def find_min(a, b):
    return min(a, b)

# Function 7: Check if a number is even
def is_even(number):
    return number % 2 == 0

# Function 8: Check if a number is odd
def is_odd(number):
    return number % 2 != 0

# Function 9: Calculate the square of a number
def square(number):
    return number ** 2

# Function 10: Calculate the cube of a number
def cube(number):
    return number ** 3

# Function 11: Check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

# Function 12: Calculate the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

# Function 13: Find the square root of a number
def square_root(number):
    return math.sqrt(number)

# Function 14: Count the number of vowels in a string
def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Function 15: Count the number of words in a string
def count_words(string):
    words = string.split()
    return len(words)

# Function 16: Reverse a string
def reverse_string(string):
    return string[::-1]

# Function 17: Check if a string is a palindrome
def is_palindrome(string):
    string = string.lower()
    string = re.sub(r'[^a-z0-9]', '', string)
    return string == string[::-1]

# Function 18: Generate a list of prime numbers within a given range
def generate_primes_in_range(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Function 19: Sort a list of numbers
def sort_list(numbers):
    return sorted(numbers)

# Function 20: Calculate the mean (average) of a list of numbers
def calculate_mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

# Function 21: Find the median of a list of numbers
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        middle1 = sorted_numbers[(n - 1) // 2]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2

# Function 22: Count the occurrences of a specific element in a list
def count_occurrences(element, lst):
    return lst.count(element)

# Function 23: Find the factorial of a number using recursion
# (Already defined as "factorial")

# Function 24: Check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Function 25: Convert a string to lowercase
def convert_to_lowercase(string):
    return string.lower()

# Function 26: Convert a string to uppercase
def convert_to_uppercase(string):
    return string.upper()

# Function 27: Calculate the power of a number
def power(base, exponent):
    return base ** exponent

# Function 28: Generate Fibonacci numbers up to a specified term
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Function 29: Check if a string contains only digits
def is_all_digits(string):
    return string.isdigit()

# Function 30: Convert temperature between Celsius and Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function 31: Calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function 32: Calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * radius**2

# Function 33: Calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Function 34: Generate a random number within a specified range
import random

def generate_random_number(start, end):
    return random.randint(start, end)

# Function 35: Check if a list is sorted in ascending order
def is_sorted(lst):
    return lst == sorted(lst)

# Function 36: Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 37: Find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Function 38: Calculate the natural logarithm of a number
def natural_logarithm(number):
    return math.log(number)

# Function 39: Calculate the absolute value of a number
def absolute_value(number):
    return abs(number)

# Function 40: Round a floating-point number to a specified decimal place
def round_to_decimal(number, decimal_places):
    return round(number, decimal_places)

# Function 41: Convert binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# Function 42: Convert decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Function 43: Convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    return hex(decimal)

# Function 44: Convert decimal to octal
def decimal_to_octal(decimal):
    return oct(decimal)

# Function 45: Calculate the absolute difference between two numbers
def absolute_difference(a, b):
    return abs(a - b)

# Function 46: Calculate the perimeter of a rectangle
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function 47: Calculate the perimeter of a circle
def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

# Function 48: Calculate the perimeter of a triangle
def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Function 49: Convert a list to a set (remove duplicates)
def list_to_set(lst):
    return set(lst)

# Function 50: Calculate the n-th term of the Fibonacci sequence using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)