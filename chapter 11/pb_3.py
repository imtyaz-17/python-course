class Employee:

    def __init__(self, salary, increment=0.0):
        self.salary = salary
        self.increment = increment 

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = (new_salary - self.salary) / self.salary


emp = Employee(50000, 0.1)  
print("Current Salary After Increment:", emp.salaryAfterIncrement)  # 55,000

emp.salaryAfterIncrement = 60000
print("New Increment:", emp.increment)  # 0.2 (20%)
print("New Salary After Increment:", emp.salaryAfterIncrement)  # 60,000
