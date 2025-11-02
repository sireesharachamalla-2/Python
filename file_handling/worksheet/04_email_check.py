import re

def extract_emails(text):
    """
    Extracts all valid email addresses from a block of text.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)
def run_tests():
    test_cases = [
        {
            "text": "Contact us at support@example.com or sales@example.org.",
            "expected": ["support@example.com", "sales@example.org"]
        },
        {
            "text": "No emails here!",
            "expected": []
        },
        {
            "text": "Invalid: test@com, also @example.com, and test@.com",
            "expected": []
        },
        {
            "text": "Mixed: admin@example.com, user.name@domain.co.in, and test_user+123@service.io",
            "expected": ["admin@example.com", "user.name@domain.co.in", "test_user+123@service.io"]
        },
        {
            "text": "Emails with numbers: user123@abc.net, 456john.doe@mail-server.org",
            "expected": ["user123@abc.net", "456john.doe@mail-server.org"]
        }
    ]

    all_passed = True
    for i, case in enumerate(test_cases):
        result = extract_emails(case["text"])
        if result == case["expected"]:
            print(f"Test case {i+1} passed.")
        else:
            print(f"Test case {i+1} failed.")
            print(f"Expected: {case['expected']}")
            print(f"Got     : {result}")
            all_passed = False

    if all_passed:
        print("\nAll test cases passed!")
    else:
        print("\nSome test cases failed.")

if __name__ == "__main__":
    run_tests()