## Very very powerful

## You can combine arguments and keyword arguments un the same function
# such as the below example such as an order system in a bookstore.
# anything without a keyword (the first 3 items) will be put into
# the args list and anything with keywords defined (last 2 items)
# will be put into the kwargs dictionary.

# Single function to reuse for different things, don;t have to have same number of fields

def add_item(*args, **kwargs):
    print(args)
    print(kwargs)

add_item(
    "146", # Order Number
    "A guide to golden retrievers", # Item name
    "book", # Item type
    author = "Dan Stacey", # Author
    isbn = "123456789"
    )

add_item(
    "147", # Order number
    "Stacey Family Holiday Vid", # Item name
    "video", # Blueray documentary
    creator = "Dan Stacery",
    length = "2:15:00",
    created = "2018"
)