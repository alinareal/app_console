# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# my solution
def even_or_odd(number):
    if number % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return result


# users solution
def even_or_odd_1(number):
    return 'Odd' if number % 2 else 'Even'


# need to explain
def even_or_odd_2(number):
    return ["Even", "Odd"][number % 2]
