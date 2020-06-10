import timeit

code_to_test = """

## Insert code to test length of time to run in here ##

"""

# Run 100 times, divide it by 100 to get average runtime and round to 2 decimal places
elapsed_time = round( (timeit.timeit( code_to_test, number=100 ) / 100), 2 )
print( "Runtime: " + str( elapsed_time ) + " secs" )