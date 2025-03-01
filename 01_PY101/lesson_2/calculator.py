import json

LANG = "en"

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    messages = json.load(file)

def get_message(message, lang=LANG):
    return messages[lang][message]

def prompt(key):
    message = get_message(key, LANG)
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def perform_calculation():
    prompt("first_num")
    number1 = input()

    while invalid_number(number1):
        prompt("invalid_num")
        number1 = input()

    prompt("second_num")
    number2 = input()

    while invalid_number(number2):
        prompt("invalid_num")
        number2 = input()

    prompt("operation")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("operation_validation")
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    print(f"{messages[LANG]["result"].format(output=output)}")
    perform_another_calculation()

def perform_another_calculation():
    prompt("another_calc")
    another_calc = input()

    while another_calc not in [messages[LANG]["positive"],
                               messages[LANG]["negative"],
                               messages[LANG]["positive"].upper(),
                               messages[LANG]["negative"].upper()]:
        prompt("another_calc")
        another_calc = input()

    if another_calc.casefold() == messages[LANG]["positive"]:
        perform_calculation()

prompt("welcome")
perform_calculation()