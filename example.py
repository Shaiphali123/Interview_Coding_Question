"""Assume you have a string, a = "one two three".
How can you put the items of the string into a list?
Example: l = ['one', 'two', 'three']"""

a = "one two three"
list1 = []

for i in a:
    list1.append(i)

print(list1)

"""Read file ‘firstfile.txt’ and print contents"""

firstfile.r()
print("read the firstfile",firstfile.txt)


"""Create a dictionary ‘car’.
Create three keys.
Make, model and year.
Try to access the color key.
Remember we never created the color key, so it’s going to throw an exception. 
You need to handle the exception using try, except and finally block."""

dict1 = {"make":"renault","model":"KIA","year": 2023}
try:
    dict1 = {"make": "renault", "model": "KIA", "year": 2023}

except:
    if dict1.key == "color":
        print("Color is Not in the Dict1")


""" Define a class Car and inherit from object.
Define methods init, drive, stop.
Create instance of class Car.
Cal methods."""

class Car:
    def __init__(self):
        self.a()

    def drive(self):
        self.drive1()

    def stop(self):
        self.stop1()

class Renault_car(car):
    def __init__(self):
        self.a()

    def drive1(self):
        self.drive2()

    def stop1(self):
        self.stop2()


obj1 = Renault_car()
Renault_car.drive1()
renault_car.stop1()

@pytest.fixture
def startup_teardown():
    # start Browser
    yield
    # close Browser

def sum(startup_teardown):
    return a+b

def sum(a,b):
    return a+b

@pytest.mark.parameterize
def Check_sum("a,b,expected_result",[
(1,2,3), #
(3,5,8),
(7,8,12)])


import request

url = "https://interview.com"

content_type = {
    "name" : "shaiphali"
    "company" : "LGE"
    "role" : "Automation Engineer"
}



try:
if response_code == 200:
    print("This is Valid Status Code")
except
 response_code == 400:
    print("bad Request")



def sum(a,b):
    return a+b

@pytest.mark.parameterize("a,b,expected_result",[
    (2,3,5),
    (1,6,7),
    (5,8,23),
    (0,0,2),
    (5,3,8)])

def test_add_number(a,b,expected_result):
    assert add_number(a,b) == expected_result







