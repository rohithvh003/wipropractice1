try:
    a =10
    b =0
    print(a/b)
except ZeroDivisionError:
    print("cant divide by zero")


try:
    x = int(input("enter a number\n"))
    print(10/x)
except ValueError:
    print("invalid entery")

except ZeroDivisionError:
    print("cant divide by zero")
else:
    print("Execution is Successful")

# user defined exception
