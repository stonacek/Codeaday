# cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
# returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
# cons returns a function object 'pair' with arguments set for 
# variables 'a' and 'b', that expects a function as input. When 
# trying to retrieve a, b we need to feed the higher-order 
# 'pair' function a function that unpacks 'a' or 'b'. 


#________________Given Solution____________________
# This is a really cool example of using closures to store data.
# We must look at the signature type of cons to retrieve its 
# first and last elements. cons takes in a and b, and returns a 
# new anonymous function, which itself takes in f, and calls f 
# with a and b. So the input to car and cdr is that anonymous 
# function, which is pair. To get a and b back, we must feed it 
# yet another function, one that takes in two parameters and 
# returns the first (if car) or last (if cdr) one.
x = cons(1,2)
y = []
def car(pair):
    def unpair(a,b):
        return a
    return pair(unpair)
#   the above is same as --> return pair(lambda a, b: a)


def cdr(pair):  # Fun fact: cdr is pronounced "cudder"!
    return pair(lambda a, b: b)


# Lambda examples
lambda x: x
# In the example above, the expression is composed of:
#    The keyword: lambda
#    A bound variable: x  
#    A body: x
# The bound variable is determined by the argument to a lambda
# function. In contract, the free variables are referenced in 
# the body of the expression

# The above lambda construciton is equivalent to:
def identity(x):
    return x

# More advanced Lambda function, adds 1 to the arg.
lambda x: x + 1
# To use the function, where 2 is the argument that fills in 
# the bounded variable x
(lambda x: x + 1)(2)

