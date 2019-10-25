
#Lesson 1 
#Creating and instantiating classes and instances of those classes. 

#Example of a class in Python. 
class Employee:

	# This is the constructor method __init__ which initializes all attributes of a object. 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
		self.email = first + '.' + last + '@email.com'


	# Creating the emp_1 and emp_2 objects and passing attributes into them. 
	emp_1 = Employee('Corey', 'Schafer', 50000)
	emp_2 = Employee('Test', 'Employee', 60000)


# Each method by default recieves the instance as the first arg. (self)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

print(emp_1.email)
print(emp_2.email)  
print(emp_1.fullname())  #dont forget to use the () after every method


"""
Both of the below lines do the same thing. They invoke the fullname() method. 
One simply uses the classname . dot notation to the fullname() method. 
"""
emp_1.fullname()
Employee.fullname(emp_1) 


# Lesson 2 
# Instance variables and class variables. 
# Class variables should be the same for every instance of a class. 
class Employee: 

	 raise_amount = 1.04
	 num_of_emps = 0 
	
	def __init__(self, first, last, pay) 
		self.first = first
		self.last= last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay
		
		Employee.num_of_emps += 1
		
	def fullname(self): 
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
		
# Instances can overide the class variable with their own variable values. 
 emp_1.raise_ammount = 1.05


# Below the class variable of num_of_emps gets auto incremented by the construtor after we create the objects that are passed in. 	
print(Employee.num_of_emps) 	

emp_1 = Employee('Dean', 'Chiri', 50000) 
emp_2 = Employee('test', 'user', 60000)

print(Employee.num_of_emps) 

print(emp_1.pay) 
emp_1.apply_raise()
print(emp_1.pay) 

#What if we could do the following? the raise_amount variable needs to exist. 
#emp_1.raise_ammount
#.raise_amount

