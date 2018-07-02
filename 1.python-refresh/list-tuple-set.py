student_grades_list = [80, 90, 75, 79]  # list, ordered
# print(sum(student_grades_list) / len(student_grades_list))  # get the average

student_grades_tuple = (80, 90, 75, 79)  # tuple, immutable

student_grades_set = {80, 90, 75, 79}  # set, unique, unordered


student_grades_list.append(98)  # add at the end
print(student_grades_list)

# has to have a comma, otherwise it's a number
student_grades_tuple = student_grades_tuple + (98,)  # add element to tuple
print(student_grades_tuple)

student_grades_list[0] = 100
print(student_grades_list)

# student_grades_tuple[0] = 200 # not working, because tuples are immutable

# print(student_grades_set[0]) # won't work, set is unordered

student_grades_set.add(70)  # add to the top
print(student_grades_set)


# advanced set operations
lottery_numbers = {1, 2, 3, 4, 5}
win_numbers = {1, 3, 5, 7, 9, 11}

common = lottery_numbers.intersection(win_numbers)
print(common)
diff = lottery_numbers.difference(win_numbers)
print(diff)
union = lottery_numbers.union(win_numbers)
print(union)
