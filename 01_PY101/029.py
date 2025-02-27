def create_story():
    answers = []
    for question in ["noun", "verb", "adjective", "adverb"]:
        answer = input(f"Enter a {question}: ")
        answers += [answer]

    print(f"Do you {answers[1]} your {answers[2]} {answers[0]} {answers[3]}? That's hilarious!")
    print(f"The {answers[2]} {answers[0]} {answers[1]}s over the lazy {answers[0]}.")
    print(f"The {answers[0]} {answers[3]} {answers[1]}s up to Joe's {answers[2]} turtle.")

create_story()
