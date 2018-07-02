my_person = {
    "name": "Foo",
    "age": 10,
    "grades": [
        20, 29, 51
    ]
}

another_dict = {  # key can also be numbers
    1: "foo",
    2: "bar",
    3: "baz"
}

players = {
    "name": "Ralf",
    "numbers": (23, 18, 33, 15)
}

unis = [
    {"name": "UTS", "students": 16000},
    {"name": "USYD", "students": 50000},
    {"name": "UNSW", "students": 56000},
]

players["name"] = "John"

# can dict have any methods?


def say_hello():
    print("Hello")


my_person2 = {
    "name": "Foo",
    "age": 10,
    "grades": [
        20, 29, 51
    ],
    "say_hello": say_hello
}

my_person2["say_hello"]()  # works only for simple methods
