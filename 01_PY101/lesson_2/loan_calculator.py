import os
import json

LANG = "en"
MONTHS_PER_YEAR = 12

# Open the JSON file for reading
with open('loan_calculator_messages.json', 'r') as file:
    messages = json.load(file)

def get_message(message, confirmation=False, lang=LANG):
    if confirmation:
        return f"{messages[lang][message]}"

    return f"==> {messages[lang][message]}"

def strip_unwanted_chars(user_input):
    if "$" in user_input or "%" in user_input:
        user_input = user_input.replace("$", "").replace("%", "")

    return user_input

def is_invalid_input(user_input, question_number):
    try:
        if "." in user_input:
            if len(user_input.split(".")[1]) > 2:
                raise ValueError(get_message("error"))

        user_input = float(user_input)

        if (question_number == 1 and user_input < 0) or \
           (question_number != 1 and user_input <= 0):
            raise ValueError(get_message("error"))
        return False
    except ValueError:
        print(get_message("error"))
        return True

def get_inputs():
    os.system("clear")
    welcome_prompt = get_message("welcome")
    print(f"{welcome_prompt}\n{'-' * len(welcome_prompt)}")
    input_prompts = [get_message("loan_amount"),
                     get_message("annual_percentage_rate"),
                     get_message("loan_duration_in_months")]
    inputs = [0.0, 0.0, 0.0]
    i = 0
    while i < len(inputs):
        while True:
            answer = strip_unwanted_chars(input(input_prompts[i]))
            if not is_invalid_input(answer, i):
                inputs[i] = float(answer)
                break

        i += 1

    return inputs

def calculate_monthly_payment(loan_amount,
                              annual_percentage_rate,
                              loan_duration_in_months):
    monthly_interest_rate = 0 if annual_percentage_rate == 0 else \
        annual_percentage_rate / MONTHS_PER_YEAR / 100

    if annual_percentage_rate == 0:
        monthly_payment = loan_amount / loan_duration_in_months
    else:
        monthly_payment = (loan_amount * monthly_interest_rate /
                          (1 - (1 + monthly_interest_rate) **
                          (-loan_duration_in_months)))

    return f"{get_message('result')} ${monthly_payment:.2f}"

def perform_another_calculation():
    another_calc = ""
    positive_confirmation = get_message("positive", confirmation=True)
    negative_confirmation = get_message("negative", confirmation=True)

    while not another_calc.casefold().startswith(
        (positive_confirmation, negative_confirmation)):
        another_calc = input(f"\n{get_message('another_calc')}")

    if another_calc.casefold().startswith(positive_confirmation):
        get_result()

def get_result():
    loan_amount, annual_percentage_rate, loan_duration_in_months = get_inputs()
    print(calculate_monthly_payment(loan_amount,
                                    annual_percentage_rate,
                                    loan_duration_in_months))
    perform_another_calculation()

get_result()