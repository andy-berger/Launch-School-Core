import json

LANG = "en"

# Open the JSON file for reading
with open('loan_calculator_messages.json', 'r') as file:
    messages = json.load(file)

def get_message(message, confirmation=False, lang=LANG):
    if confirmation:
        return f"{messages[lang][message]}"

    return f"==> {messages[lang][message]}"

def is_invalid_input(user_input):
    try:
        if isinstance(user_input, str) and \
        ("$" in user_input or "%" in user_input):
            user_input = user_input.replace("$", "").replace("%", "")
        user_input = float(user_input)
        if user_input <= 0:
            raise ValueError(get_message("error"))
        return False
    except ValueError:
        print(get_message("error"))
        return True

def get_inputs():
    welcome_prompt = get_message("welcome")
    print(f"{welcome_prompt}\n{'-' * len(welcome_prompt)}")
    input_prompts = [get_message("loan_amount"),
                     get_message("annual_percentage_rate"),
                     get_message("loan_duration_in_months")]
    inputs = [0.0, 0.0, 0.0]
    i = 0
    while i < len(inputs):
        while True:
            answer = input(input_prompts[i])
            if not is_invalid_input(answer):
                inputs[i] = float(answer)
                break

        i += 1

    return inputs

def calculate_monthly_payment(loan_amount,
                              annual_percentage_rate,
                              loan_duration_in_months):
    monthly_interest_rate = annual_percentage_rate / 12 / 100
    return f"{get_message('result')} ${loan_amount *
                                    (monthly_interest_rate /
                                    (1 - (1 + monthly_interest_rate)
                                    ** (-loan_duration_in_months))):.2f}"

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