old_number = 100
#全局变量和局部变量的作用域
def change_func():
    old_number = 99 #复制产生了了一个同名的局部变量
    old_number2 = old_number
    old_number2 -= 3
    old_number = 96
    print('old_number in func is :', old_number)
    print('old_number in func is :', old_number2)
change_func()
print('old_number out func is:', old_number)