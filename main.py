class Employee:
    def __init__(self, fullname, experience):
        self.fullname = fullname
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_exp):
        if 0 <= new_exp <= 40:
            self.__experience = new_exp
        else:
            print("Noto'g'ri tajriba")


e1 = Employee("Rustam", 5)

print(e1.fullname)
print(e1.get_experience())

e1.set_experience(10)
print(e1.get_experience())

e1.set_experience(50)
