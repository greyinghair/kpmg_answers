## Keyword arguments allow you to pass parameters to function in any order
# such as below example
# This is because we define the keyword name with the parameter itself rather than just the value
# up to now we have just passed values, if just values defined then have to be passed in order expected
# in the function, but when we pass keyword AND their value in the parameters it can be in ANY order.

def add_result(player_name, player_score):
    #
    # Do something with the data passed in
    return (player_name, player_score) # Just entered so code doesn't error, IGNORE this line

# Pass in any order as explicitly defined the keyword ALONG with the value
print(add_result(player_name = "Dan", player_score= 99)) # Matches order so could just do "Dan", 99.
print(add_result(player_score= 12, player_name="Wendy")) # Order doesn't match function but defined keyword so doesn't matter

## Example using default arg as well as keywords

def send_message(to, sender = "Alice", message = "Hi"): # expected params in order if not defining keyword in paramater
    #
    # Code to send the message
    #
    return (to, sender, message)

# Both the same and both valid as "to" is first in the parameters
send_message("Dan")
send_message(to = "Dan")

# All of the below function calls are the same
send_message("Dan", "Wendy", "Where are you?") # just values but in right order for passing: (to ,sender, message)
send_message("Dan", message = "Where are you?", sender = "Wendy") # 1st param in order so no keyword needed, 2nd 2 out of order so needs keyword defining with the values so is processed by correct params in the function.
send_message(message = "Where are you?", to = "Dan", sender = "Wendy") # all out of order so need to supply keyword along with value so passed to function and processed by keyword as required.

## You can also use **kwargs (keyword arguments) as per below example, ie using double * (**<var)
# you must define a keyword with a value which when passed to a function will be treated as a dictionary

def my_func(**kwargs):
    print(kwargs)

my_func(name = "Dan", dob = "04021980") # when called will pass each keyword and variable pair as a dictionary to my_func