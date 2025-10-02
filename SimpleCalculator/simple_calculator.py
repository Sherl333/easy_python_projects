calc_history = []

def add(x, y):
    result = x + y
    calc_history.append(f"{x}+{y}={result}")
    return result

def sub(x, y):
    result = x - y
    calc_history.append(f"{x}-{y}={result}")
    return result

def mul(x, y):
    result = x * y
    calc_history.append(f"{x}*{y}={result}")
    return result

def div(x, y):
    if y == 0:
        print("Cannot be divided by 0")
        return None
    result = x / y
    calc_history.append(f"{x}/{y}={result}")
    return result

def chainedOperation(chained_exp):
    try:
        result = eval(chained_exp)
        calc_history.append(f"{chained_exp}={result}")
        return result
    except Exception as e:
        print(f"Invalid chained expression: {e}")
        return None

def show_history():
    if not calc_history:
        print("No previous calculations")
    else:
        print("\nCalculation History:")
        for cal in calc_history:
            print(cal)

def userInput():
    while True:
        his = input("Do you want to see past calculations? (Y/N): ")
        if his.upper() == "Y":
            show_history()

        try:
            number1 = int(input("Enter a number: "))
            number2 = int(input("Enter a second number: "))
        except ValueError:
            print("Please input integer values only")
            continue

        operator = input("Choose the operator (+,-,*,/): ")

        if operator == '+':
            print(f"The answer is: {add(number1, number2)}")
        elif operator == '-':
            print(f"The answer is: {sub(number1, number2)}")
        elif operator == '*':
            print(f"The answer is: {mul(number1, number2)}")
        elif operator == '/':
            ans = div(number1, number2)
            if ans is not None:
                print(f"The answer is: {ans}")
        else:
            print("Invalid operator")

        replay_option = input("Do you want to continue? (Y/N): ")
        if replay_option.upper() != 'Y':
            print("Thank you for using the calculator!")
            break

        chained_op = input("Do you want to perform a chained operation? (Y/N): ")
        if chained_op.upper() == 'Y':
            chained_exp = input("Enter your chained expression: ")
            ans = chainedOperation(chained_exp)
            if ans is not None:
                print(f"The answer is: {ans}")
userInput()