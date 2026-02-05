#!/usr/bin/env python3
# Simple calculator with input checks


def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Please type something.")
            continue
        try:
            n = int(s)
        except ValueError:
            print("Enter a whole number like -5, 0, or 12.")
            continue
        if abs(n) > 1000000:
            print("Number too big. Keep it between -1000000 and 1000000.")
            continue
        return n


def main():
    name = ""
    while not name:
        name = input("What is your name? ").strip()
        if not name:
            print("Name cannot be blank.")

    while True:
        num1 = get_number("Enter a number: ")
        num2 = get_number("Enter another number: ")

        print("\n--- Results ---")
        print("Hello", name)
        print("First number:", num1)
        print("Second number:", num2)
        print("Sum:", num1 + num2)
        print("Difference:", num1 - num2)
        print("Product:", num1 * num2)
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Quotient:", num1 / num2)
            print("Remainder:", num1 % num2)


if __name__ == "__main__":
    main()
