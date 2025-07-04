def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return "❌ Cannot divide by zero"
    return x / y
while True:
    print("\n🧮 Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    user_choice = input("Enter choice (1-5): ")
    if user_choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numbers!!!.")
            continue
        if user_choice == '1':
            print(f"Result: {addition(num1, num2)}")
        elif user_choice == '2':
            print(f"Result: {subtraction(num1, num2)}")
        elif user_choice == '3':
            print(f"Result: {multiplication(num1, num2)}")
        elif user_choice == '4':
            print(f"Result: {division(num1, num2)}")
    elif user_choice == '5':
        print("👋 Exiting Calculator.Byeeee!")
        break
    else:
        print("❌ Invalid input. Please choose only from 1 to 5!!!.")
