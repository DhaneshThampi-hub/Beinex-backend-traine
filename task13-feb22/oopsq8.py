'''show class method, static method and instance method with simple example'''

#instance method
class MyClass:
    def instance_method(self):
        return "Instance method called"

obj = MyClass()
print(obj.instance_method())  

#class method
class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"
print(MyClass.class_method())  


#static method
class MyClass:
    @staticmethod
    def static_method():
        return "Static method called"

print(MyClass.static_method()) 
