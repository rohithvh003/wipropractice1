# 1d reduce use the import reduce
from functools import reduce

sq_num = [4,9]
total_sum = reduce(lambda x, y: x + y, sq_num)
print(total_sum)


# 1e enumerate
for index, value in enumerate(sq_num):
    print(index, value)