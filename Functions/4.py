# passing argument to the function means some data to the function 
# means to be able to this we need to declare parameters to be accepted by the function 

def hello_func(greeting):
    return '{} Function'.format(greeting)
# now , this greeting variable will not be affected by anything outside hello_func()  bcz its scope is local to the hello_func() function

print (hello_func('Hi')) # o/p Hi function 

#hello_func() #will give Type error bcz required argument is not passed 

# in this case greeting parameter is a required parameter so in upcoming function we will give a default value to the parameter so the it can fall back to the default value when the function does'nt get any argument for it 

def hello_function( greeting, name = "You"):
    return '{}, {}'.format(greeting, name)

print(hello_function('Hi'))
#o/p : Hi, you
# also this will not give an error 

print(hello_function('Hi', name='Corey'))
#o/p : Hi, Corey    