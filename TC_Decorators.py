# Modifies the behaviour but does not change the previous function is
# known as Decorators

def mydecorators(func):
    def wrapper():
        print("Before function call")
        func()
        print("After Functional call")
    return wrapper

@mydecorators
def sayhello():
    print("hello")
sayhello()

@mydecorators
def saybye():
    print("Bye")
saybye()