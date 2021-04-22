# class Employee:

#     add_salary = 10

#     def __init__(self, salary, hours_of_work):
#         self.salary = salary
#         self.hours_of_work = hours_of_work

#     def getInfo(self):
#         pass

#     def addSal(self):
#         if employee.salary < 500:
#             self.salary = int(self.salary + 10)
#         else:
#             print('employee salary is higher than 300$')

#     def addWork(self):
#         if employee.hours_of_work > 6 :
#             self.salary = int(self.salary + 5)
#         else:
#             print('work harder bro')
# employee = Employee(300, 9)


# class Employee:
#     def _init_(self, salary, number_of_hours):
#         self.salary = salary
#         self.number_of_hours = number_of_hours

#     def getinfo(self):
#         return '{} {}'.format(self.salary, self.number_of_hours)

#     def addsal(self):
#         if self.salary < 500:
#             self.salary += 10
#             return self.salary
#         else:
#             print("The employee is  more than $500")

#     def addWork(self):
#         if self.number_of_hours > 6:
#             self.salary += 5
#             return self.salary
#         else:
#             print("Employee number of work hours is less than 6 hours")


# emp = Employee(300, 5)
# print(emp.getinfo())git 
# print(emp.addsal())


class Employee:
    def _init_(self, user_salary, work_of_hrs):
        self.user_salary = user_salary
        self.work_of_hrs = work_of_hrs

    def getinfo(self):
        return f'Salary: {self.user_salary} \nWorking hours: {self.work_of_hrs}'

    def addsal(self):
        if self.user_salary < 500:
            return self.user_salary + 10
        else:
            return self.user_salary

    def addwork(self):
        if self.work_of_hrs > 6:
            return f'Working hours: {self.user_salary + 5}'
        else:
            return f'Working hours: {self.user_salary}'


employee1 = Employee(30, 8)
print(employee1.addwork())


# these are what i've tried out and yet they are still not working
