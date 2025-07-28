# Input from the user
text = input("Enter a string or number: ")

# Check palindrome by reversing
if text == text[::-1]:
    print(f"{text} is a Palindrome")
else:
    print(f"{text} is Not a Palindrome")
12