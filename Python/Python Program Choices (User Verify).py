# Smart Calculator with Input Protection
# Name: Noah Baker
# Period: 3rd

def get_int(prompt):
    while True:
        raw = input(prompt).strip()

        if raw == "":
            print("Error: type a number.")
            continue

        try:
            value = int(raw)
        except ValueError:
            print("Error: enter a whole number.")
            continue

        if value < -1_000_000 or value > 1_000_000:
            print("Error: number is too large.")
            continue

        return value


while True:
    name = input("What is your name? ").strip()
    if name == "":
        print("Error: name cannot be blank.")
    else:
        break


num1 = get_int("Enter a number: ")
num2 = get_int("Enter another number: ")

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

print("\n--- Calculator Results ---")
print("Hello", name)
print("First number:", num1)
print("Second number:", num2)
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
