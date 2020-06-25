## Q3
# Create a Employee class and initialise it with name and staff number.
# i. Make methods to:
    # display_info - It should display all the information of the employee.
    # set_department - It should assign the department to employee.
    # set_bonus - It should assign a bonus amount to the employee.

# ii. Create the instance attributes first name and last name instead of name.
    # Create two methods full_name and email_address in the Employee class.
    # Given a person's first and last names:
    # Form the full_name method by simply joining the first and last name together, separated by a space.
    # Form the email_address by joining the first and last name together
        # with a . in between, and follow it with @company.com at the end. Make sure everything is in lowercase.

class Employee:

    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

    def fullname(self):
        return self.fname + " " + self.lname

    def email(self):
        self.email = (self.fname + "." + self.lname + "@stacey.im").lower()
        return self.email

    def set_department(self,team):
        self.team = team

    def set_bonus(self,bonus):
        self.bonus = bonus

    def info(self): # Method with all above variables printed out
        print("Name: " + self.fullname())
        print("E-Mail: " + self.email())
        print("Staff No: " + self.number)
        print("Team+ " + self.team)
        print("Bonus: £" + str(self.bonus))


dan = Employee("Dan", "Stacey", "000123") # set variable of dan to pass parameters to Employee class
dan.set_department("Network Operations") # call set department and pass a string
dan.set_bonus(4000) # pass value of bonus as a string

dan.info() # List all info