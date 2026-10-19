# Interactive Calculator & Unit Converter

def calculator():
    print("\n--- Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers.")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation: ")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation!")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose a conversion: ")

    try:
        value = float(input("Enter the value: "))

        if choice == "1":
            print("Miles:", value * 0.621371)
        elif choice == "2":
            print("Fahrenheit:", (value * 9 / 5) + 32)
        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input! Please enter a number.")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = input("Choose a conversion: ")

    try:
        amount = float(input("Enter the amount: "))

        # Example rates only; update with a current exchange rate.
        inr_to_usd = 0.012
        usd_to_inr = 1 / inr_to_usd

        if amount < 0:
            print("Amount cannot be negative.")
        elif choice == "1":
            print("USD:", round(amount * inr_to_usd, 2))
        elif choice == "2":
            print("INR:", round(amount * usd_to_inr, 2))
        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input! Please enter a number.")


while True:
    print("\n===== INTERACTIVE CALCULATOR =====")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Currency Converter")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        unit_converter()
    elif choice == "3":
        currency_converter()
    elif choice == "4":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice! Please try again.")

