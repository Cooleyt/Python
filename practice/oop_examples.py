class Employee():

    def __init__(self, first_name, last_name, salary, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = int(salary) 
#this is out blueprint of building an employee
    def get_full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

employee1 = Employee('Alice', 'Jones', 87000, middle_name = 'Anne')
employee2 = Employee('Jack', 'Craig', 61000)
employee3 = Employee('Charlie', 'Price', 79000, middle_name = 'Zachary')

# print(employee1.first_name) #this will print Alice Jack Charlie

employees = [employee1, employee2, employee3]

for employee in employees:
        print(f"Full name = {employee.get_full_name()} Salary: {employee.salary}" ) #prints