def transform(text, shift):
    """Shifts characters based on the provided integer."""
    result = ""
    for char in text:
        result += chr(ord(char) + shift)
    return result

while True:
    print("\n--- Shift Cipher ---")
    choice = input("1. Encrypt\n2. Decrypt\n3. Exit\nChoose: ")

    if choice == '1':
        password = input("Enter password: ")
        code = int(input("Enter shift code: "))
        print(f"Result: {transform(password, code)}")

    elif choice == '2':
        password = input("Enter password: ")
        code = int(input("Enter shift code: "))
        # To decrypt, we just pass the negative version of the code
        print(f"Result: {transform(password, -code)}")

    elif choice == '3':
        break
    else:
        print("Invalid choice, try again.")