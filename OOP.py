class EmobilisStudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and im {self.age}years old")
#creating and object
myobj=EmobilisStudent("Erick",30)

myobj.hello_me()

class supermarkets:
    def __init__(self, name, location):
        self.name=name
        self.location=location
    def hello_me(self):
        print(f"{self.name} is located in  {self.location} near Eden ville")
#creating and object
myobj=supermarkets("Quickmart","Thindigua")
myobj.hello_me()
myobj=supermarkets("Tuskys","Nairobi Town")
myobj.hello_me()

#create a class called magari,it should  have model,make,year properties
#create min of three objects
class magari:
    def __init__(self, model, make, year):
        self.model=model
        self.make=make
        self.year=year
    def hello_me(self):
        print(f"This is a {self.model} {self.make} of the year {self.year}")
myobj=magari("BMW","320i", 2016)
myobj.hello_me()
myobj=magari("Range Rover","evoque",2022)
myobj.hello_me()
myobj=magari("Toyota","supra",2011)
myobj.hello_me()