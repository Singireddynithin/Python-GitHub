
# SETTER AND GETTER EXAMPLE 
# Encapsulation Example: combination of variables and methods
# setter method: passing of arguments and getter method is the data from setter method we take the data

# class school:
#     def set1(self,s_name):
#         self.name = s_name
#     def get1(self):
#         return self.name
#     def set2(self,pin):
#         self.pin = pin
#     def get2(self):
#         return self.pin
#     def set3(self,city):
#         self.city = city
#     def get3(self):
#         return self.city
    
# obj = school()
# obj.set1('Nithin')
# obj.set2(123456)
# obj.set3('Bangalore')

# print('======')
# print(obj.get1())
# print(obj.get2())
# print(obj.get3())   

class employee:
    def set1(self, emp_name):
        self.name = emp_name
    def get1(self):
        return self.name
    def set2(self, emp_pin):
        self.pin = emp_pin
    def get2(self):
        return self.pin
    def set3(self, emp_salary):
        self.salary = emp_salary
    def get3(self):
        return self.salary
    
obj=employee()
obj.set1('Nithin')
obj.set2(123456)
obj.set3(50000)
print('======EMPLOYEE DETAILS======')

print(obj.get1())
print(obj.get2())
print(obj.get3())

# print("Encapsulation example completed successfully.")
# print(obj.get1(), obj.get2(), obj.get3())
# print("This is an example of encapsulation in Python.")
# print("Encapsulation allows bundling of data and methods that operate on that data within a single unit.")
# print("This example demonstrates how to use setter and getter methods to access and modify private data.")
# print("Encapsulation is a fundamental concept in object-oriented programming that helps in data hiding and abstraction.")
# # This code demonstrates encapsulation in Python using a class with setter and getter methods.
# # This code demonstrates encapsulation in Python using a class with setter and getter methods.

