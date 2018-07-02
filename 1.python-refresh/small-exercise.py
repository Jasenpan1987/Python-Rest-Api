known_people = []


def who_do_you_know():
    try:
        input_list = input("give me some names, separated by comma")
        input_without_comma = input_list.replace(" ", "").lower()
        global known_people
        known_people = input_without_comma.split(",")
    except:
        print("input is not valid")
        who_do_you_know()
    finally:
        return known_people


def ask_a_user():
    input_name = input("give me a name")
    if input_name.lower() in known_people:
        print("You know {}".format(input_name))
    else:
        print("You don't know {}".format(input_name))


who_do_you_know()
ask_a_user()
