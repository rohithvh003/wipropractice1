from logging import raiseExceptions


class myerror(Exception):
    pass
# raise myerror("this is a user defined exception")


class invalidage(Exception):
    pass

try:
    age = int(input("enter your age"))
    if age <18:
        raise invalidage("age must be 18 or above")
    else:
        print("eligibility to vote")

except invalidage as e:
    print("error:",e)