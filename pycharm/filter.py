def IS_four_bytes(num):
    return num % 4
temp = filter(IS_four_bytes, range(100))
print(type(temp))
print(list(temp))
print(temp)
print(list(filter(IS_four_bytes, range(100))))
