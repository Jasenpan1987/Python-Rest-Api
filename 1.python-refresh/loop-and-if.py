# ========== loop ===========
my_var = "hello"  # iterable
for l in my_var:
    print(l)

my_list = [1, 2, 3, 4]
for num in my_list:
    print(num ** 2)

user_wants = True
while user_wants:
    try:
        inp = int(input("give a number"))
        if inp == 2:
            user_wants = False
    except:
        print("not a number")

# ========== if ===========
should_continue = False
if(should_continue):
    print("hello")
else:
    print("bye")

known_people = ["Anna", "Bill", "John"]
input_person = input("enter a person")
if input_person in known_people:
    print("you know {}".format(input_person))
else:
    print("you don't know {}".format(input_person))
