# def reduce(num):
#     print(f"Called number,{num}")
#
#     if num:
#         print(f"reducing number,{num}-1")
#         reduce(num-1)
#
# print("[START]: CALLING reduce(3)")
# reduce(5)
#
#
# def reduce(num):
#     print(f"called number,{num}")
#
#     if num:
#         print(f"reducing number,{num}-1")
#         reduce(num-1)
#
#
# print(f"start: calling number(6)")
# reduce(6)

# DECORATORS
def fence(func):

    def add_fence(val):
        print("+"*10)
        func(val)
        print("+"*10)

    return add_fence

@fence
def fence(val):
    print(val)

