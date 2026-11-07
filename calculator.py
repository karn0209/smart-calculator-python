def save(text):
    with open("history.txt", "a") as f:
        f.write(text + "\n")
 
 
def add(a, b):
    result = a + b
    save(f"{a} + {b} = {result}")
    return result
 
 
def subtract(a, b):
    result = a - b
    save(f"{a} - {b} = {result}")
    return result
 
 
def multiply(a, b):
    result = a * b
    save(f"{a} * {b} = {result}")
    return result
 
 
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    result = a / b
    save(f"{a} / {b} = {result}")
    return result
 
 
def power(a, b):
    result = a ** b
    save(f"{a} ^ {b} = {result}")
    return result
 
 
def square_root(a):
    if a < 0:
        return "Square root of a negative number is not defined."
    result = a ** 0.5
    save(f"Square root of {a} = {result}")
    return result
 
 
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")
 
 
def view_history():
    try:
        with open("history.txt", "r") as f:
            history = f.read()
        if history:
            print("\nCalculation History:")
            print(history)
        else:
            print("\nNo calculations performed yet.")
    except FileNotFoundError:
        print("\nNo calculations performed yet.")
 
 
def clear_history():
    open("history.txt", "w").close()
    print("\nCalculation history cleared.")
 
 
def search_history():
    term = input("Search for (+, -, *, /, ^, sqrt): ").strip()
 
    if term == "":
        print("Search cannot be empty.")
        return
 
    if term == "sqrt":
        term = "Square root"
    elif term in ("+", "-", "*", "/", "^"):
        term = f" {term} "
 
    try:
        with open("history.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("\nNo calculations performed yet.")
        return
 
    found = False
    for line in lines:
        if term in line:
            print(line, end="")
            found = True
 
    if not found:
        print(f"\nNo calculations found for '{term.strip()}'.")
 
 
def show_menu():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. View History")
    print("8. Clear History")
    print("9. Search History")
    print("10. Exit")
    return input("Enter choice (1-10): ")
 
 
def main():
    print("Welcome to Smart Calculator!")
 
    while True:
        choice = show_menu()
 
        if choice in ("1", "2", "3", "4", "5"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
 
            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
            elif choice == "5":
                print("Result:", power(a, b))
 
        elif choice == "6":
            a = get_number("Enter a number: ")
            print("Result:", square_root(a))
 
        elif choice == "7":
            view_history()
 
        elif choice == "8":
            clear_history()
 
        elif choice == "9":
            search_history()
 
        elif choice == "10":
            print("Thank you for using Smart Calculator!")
            break
 
        else:
            print("Invalid choice")
 
 
if __name__ == "__main__":
    main()

