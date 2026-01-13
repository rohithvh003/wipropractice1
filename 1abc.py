# 1a
for num in range(1,21):
    print(num)

# 1b
num = [1,2,3,4,5,6,7,8,9,10]
even_numbers = filter(lambda x: x % 2 == 0, num)
print(list(even_numbers))


# 1c
num = [1,2,3,4,5]
squared_num = list(map(lambda x: x ** 2, num))
print(list(squared_num))

