# Palindrome Number Checker

def is_palindrome_number(num: int) -> bool:
    # Convert number to string
    num_str = str(num)
    # Compare with its reverse
    return num_str == num_str[::-1]

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_palindrome_number(number):
        print(f"{number} is a palindrome number!")
    else:
        print(f"{number} is not a palindrome number.")
