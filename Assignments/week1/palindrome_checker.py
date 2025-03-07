def clean_string(input_string: str) -> str:
    """Helper function to clean the input string by removing non-alphanumeric characters
    and converting to lowercase."""
    return ''.join(char.lower() for char in input_string if char.isalnum())

def is_palindrome_while(input_string: str) -> bool:
    """Check if a string is a palindrome using a while loop."""
    # Clean the input string first
    cleaned = clean_string(input_string)
    if not cleaned:  # Handle empty string case
        return True
    
    # Use two pointers: one from start, one from end
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_for(input_string: str) -> bool:
    """Check if a string is a palindrome using a for loop."""
    # Clean the input string first
    cleaned = clean_string(input_string)
    if not cleaned:  # Handle empty string case
        return True
    
    # Use for loop to compare characters from both ends
    length = len(cleaned)
    for i in range(length // 2):  # Only need to check half the string
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
    
    return True

# Test cases
def test_palindromes():
    test_cases = [
        "A man, a plan, a canal, Panama",  # True
        "race a car",                      # False
        "Was it a car or a cat I saw?",    # True
        "hello",                           # False
        "",                                # True (empty string)
        "A",                               # True (single character)
        "12321",                           # True (numbers)
        "A,b.C,d,e",                      # False
    ]
    
    print("Testing palindrome functions:")
    print("-" * 50)
    
    for test in test_cases:
        result_while = is_palindrome_while(test)
        result_for = is_palindrome_for(test)
        print(f"Input: '{test}'")
        print(f"While loop result: {result_while}")
        print(f"For loop result: {result_for}")
        print(f"Match: {result_while == result_for}")
        print("-" * 50)

# Run the tests
if __name__ == "__main__":
    test_palindromes()