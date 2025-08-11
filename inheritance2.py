class user():
    
    def __init__(self,name,email,phone,password,discount):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.discount = discount

    def say_my_name(self):
        print(f"My name {self.name}.")



class Employee(user):
    
    def __init__(self,name,email,phone,password,salary):
        super().__init__(name,email,phone,password,discount)
        self.salary = salary

class Customer(user):

    def __init__(self,name,email,phone,password,discount):
        super().__init__(name,email,phone,password,0)
     