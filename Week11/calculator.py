def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def power(a, b):
    if b == 0:
        return 1
    if b < 1:
        return 1 / power(a, -b)
    return a * power(a, b - 1)


if __name__ == "__main__":
    f = input(
        """Choose a function:\n1: Check your number is prime\n2: Power your numbers\n"""
    )
    if f == "1":
        n = input("Input your number: ")
        print("Is the number prime: ", prime(int(n)))
    elif f == "2":
        first = input("Input first number: ")
        second = input("Input second number: ")
        print("The power result is: ", power(int(first), int(second)))
    else:
        print("Invalid input, try again.")
