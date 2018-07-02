class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name):
        return cls(friend_name, origin.school)


class WorkingStudent(Student):
    def __init__(self, name, school, sallary):
        super().__init__(name, school)
        self.sallary = sallary

    @classmethod
    def friend(cls, origin, friend_name, sallary):
        return cls(friend_name, origin.school, sallary)

# anna = Student("Anna", "USYD")
# greg = anna.friend("Greg")

# print(greg.name, greg.school)


bill = WorkingStudent("Bill", "QUT", 40000)
jill = WorkingStudent.friend(bill, "Jill", 6000)
print(bill.sallary)
print(jill.school, jill.sallary)
