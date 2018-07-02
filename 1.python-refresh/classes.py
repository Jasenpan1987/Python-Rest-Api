class LotteryPlayer():
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


# lottery_player = LotteryPlayer("Rolf", (23, 9, 18, 7, 1, 52, 13))
# print(lottery_player.total())

# # ========= student class ==========
# class Student():
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []

#     def get_avg(self):
#         return sum(self.marks) / len(self.marks)


# anna = Student("Anna", "UTS")
# anna.marks.append(89)
# anna.marks.append(74)
# anna.marks.append(82)
# print(anna.get_avg())


# ========= stock class ==========
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        # return sum(map(lambda item: item["price"], self.items))
        return sum([item["price"] for item in self.items])


# s = Store("mystore")
# s.add_item("foo", 120)
# s.add_item("bar", 100)

# print(s.stock_price())


# ========= student class ==========
class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def get_avg(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print(f"Im going to {self.school}")

    # Class Method
    @classmethod
    def say_hello(cls):
        print("Hello there")

    @staticmethod
    def say_goodbye(name):
        print(f"Bye {name}")


anna = Student("Anna", "UTS")
anna.go_to_school()
Student.say_hello()  # call a Class method with class also works
Student.say_goodbye("John")  # call a static method
anna.say_goodbye("billy")
