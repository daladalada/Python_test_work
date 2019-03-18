def doc_function(doc_para):
    """
    This is a test About
    __doc__
    function
    """
    #函数说明
    print(doc_para * 6.5)
    return doc_para * 6.5
doc_function(int(input("please input a number:")));
print(doc_function.__doc__)#__doc__打印出函数的所有说明字符串