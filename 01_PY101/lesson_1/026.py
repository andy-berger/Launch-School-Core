def print_top_or_bottom(text_length, location):
    top_or_bottom = "+" + (text_length + 2) * "-" + "+"
    second_to_top_or_bottom = "|" + (text_length + 2) * " " + "|"
    if location == "top":
        print(top_or_bottom + "\n" + second_to_top_or_bottom)
    elif location == "bottom":
        print(second_to_top_or_bottom + "\n" + top_or_bottom)
    else:
        print('Error: second parameter must be either "top" or "bottom"')
    
def print_in_box(text):
    text_length = len(text)
    print_top_or_bottom(text_length, "top")
    print("|" + " " + text + " " + "|")
    print_top_or_bottom(text_length, "bottom")

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
