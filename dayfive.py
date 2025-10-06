class Person:
    def __init__(self,name,age):
        self .name = name
        self .age = age
        
    def __str__(self):
        return f"{self.name},{self.age} years old"

person= Person("AKHIL",23)
print(person)

class Dog:
    def __init__(self,name,age):
        self .name = name
        self .age = age
        
    def __str__(self):
        return f"{self.name},{self.age} years old"

dog= Dog("MINTOO",5)
print(dog)
