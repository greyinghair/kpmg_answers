def is_prime(prime):
    count = 0
    for p in range(2,(prime)): # loop from 2 through to index 1 less than the number itself, i.e. won't include the
        # number itself nor 1 but divide by everything else, if any of then can be divided by a whole number then not
        # a Prime number
        if prime % p == 0: # If the number is divisible (entirely by the number in range, then:
            print(str(prime) + " is divisible by " + str(p))
            count += 1
    if count == 0:
        print("\nPRIME" + " (count: " + str(count) + ")")
    else:
        print("\nNOT PRIME" + " (divisible by " + str(count) + " number(s) other than 1 and itself)")


is_prime(int(input("What number would you like to know whether is a prime number or not? ")))