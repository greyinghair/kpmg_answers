### Class (which is part of object oriented programming) is a blueprint.

## syntax is as below, IMPORTANT 1st letter of class name SHOULD be UPPERCASE:

#   class Name_of_class:
#       <code>

## If you use a "FUNCTION" within a class then the function is called a "METHOD":

# class Name_of_class:
#     wheels = 4
#
#     def drive():
#         # code that makes the car drive

## An OBJECT is a an instance of that class.  it uses the blueprint of the class to create it's own object
# e.g.

class Car:
    wheels = 4


volvo = Car()
print (volvo.wheels) # 4