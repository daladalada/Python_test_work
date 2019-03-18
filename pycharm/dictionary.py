#赋值方法1
dic1 = {'李宁':'一切皆有可能', '耐克':'Just do it', '阿迪达斯':'impossible is nothing', '小猪儿':'白白胖胖好可爱'}
#print(dic1)
print('阿迪达斯:', dic1['阿迪达斯'])
#赋值方法2
dic2 = dict((('李宁','一切皆有可能'),('耐克','Just do it'),('阿迪达斯','impossible is nothing'),('小猪儿','白白胖胖好可爱')))
print(dic2)
print(dic2['李宁'])
#键值操作
#增加
dic2['x'] = 100
dic2["""我
告
诉
你
"""] = """不告诉你"""
print(dic2)
#修改
dic2["x"] = 200
print(dic2)
#删除
dic2.pop("x")
dic2["x"] = 200
dic2.pop("x")
print(dic2)
dic2.pop('阿迪达斯')
print(dic2)

