def closure_1(para_1 = 5):
    para_3 = 5
    def closure_2(para_2 = 9):
        nonlocal para_3, para_1 #nonlocal表示引用外部一层变量
        para_3 -= para_1
        print('para_3 in para_1 is:' + str(para_1) +  ' value is:', para_3)
        print('para_1:' + str(para_1) +  ' * para_2:' + str(para_2) +  ' * para_3:' + str(para_3) + ' = ', para_1 * para_2 * para_3)
        return para_1 * para_2 * para_3
    return closure_2

para_3 = 50
print('para_3 first is:', para_3)
square_1 = closure_1(8)
print(square_1(6))
square_2 = closure_1()
print(square_2())
func_point = closure_1
print(func_point(7)(7))
print('para_3 final value is:', para_3)
