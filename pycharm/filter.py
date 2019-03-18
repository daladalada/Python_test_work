def IS_four_bytes(num):
    return num % 4
#filter : 返回使得函数返回值为真的参数
temp = filter(IS_four_bytes, range(100))
print(type(temp))
print(list(temp))
print(temp)
print(list(filter(IS_four_bytes, range(100))))
#map : 使用所给参数依次执行函数所得到的函数返回值
temp = map(IS_four_bytes, range(0,100))
print(type(temp))
print(list(temp))
print(temp)
print(list(map(IS_four_bytes, range(0,100))))