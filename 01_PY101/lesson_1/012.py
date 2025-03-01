def greetings(name, properties):
    return f"Hello, {' '.join(name)}! Nice to have a {properties["title"]} {properties["occupation"]} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)
