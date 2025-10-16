while True:
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '5':
        print("GOODBYE")
        break

    # Check if choice is valid
    if choice not in ['1', '2', '3', '4']:
        print("INVALID: CHOOSE 1-4")
        continue

    # Get numbers safely
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("ERROR: VALID NUM ONLY")
        continue  # Go back to the top of the loop

    # Perform operation
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("ERROR: DIV BY 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
