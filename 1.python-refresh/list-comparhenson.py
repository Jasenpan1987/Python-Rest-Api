# list comparehenson is a way to build list

list1 = [x for x in range(5)]
print(list1)

list2 = [x**2 for x in range(5)]
print(list2)

list3 = [x for x in range(1, 10) if x % 2 == 0]
print(list3)

name_input = ["Anna ", "Bill", "  Josh", "steve"]
normalized_people = [p.lower().strip() for p in name_input]
print(normalized_people)
