"""
Git & GitHub Practice Application
----------------------------------
Use this script to practice basic Git commands, branching, and pull requests.
"""

def greet_user(name="Developer"):
    """Returns a simple greeting message."""
    return f"Hello, {name}! Welcome to your Git & GitHub practice repository."


def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b


# TODO (Practice Exercise 1): Create a function that calculates the product of two numbers.
# Example: def multiply(a, b): return a * b


def main():
    print(greet_user())
    
    num1, num2 = 5, 10
    print(f"The sum of {num1} and {num2} is: {calculate_sum(num1, num2)}")

    # TODO (Practice Exercise 2): Print your name and favorite programming language below.
    # print("Developer: <Your Name> | Favorite Language: Python")


if __name__ == "__main__":
    main()