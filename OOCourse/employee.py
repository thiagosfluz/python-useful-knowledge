class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee('Thiago', 'Luz', 90000)
emp_2 = Employee('Teste', 'User', '100000')

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))


print(emp_1.__dict__)
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)








