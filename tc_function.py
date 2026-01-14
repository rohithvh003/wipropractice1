#syntax of function
# def methodname(parameters):
#     print()
# methodname(parameters)

def add(a,b):
    print(a+b)

def sub(a,b):
    return a-b

add(10,20)
print(sub(100,20))


def hello(greeting = "Hello",name="world"):
    print('%s,%s'%(greeting,name))

hello()
hello('Greeting','rohit')

# n number of parameters
def print_params(*params):
    print(params)

print_params('testing')
print_params(10)


# named parametrs we use **
def print_parameters(**params):
    print(params)

print_parameters(x=1,y=2,z=3)


