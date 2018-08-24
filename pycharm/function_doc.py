def doc_function(doc_para):
    """
    This is a test About
    __doc__
    function
    """
    print(doc_para * 6.5)
    return doc_para * 6.5
doc_function(int(input("please input a number:")));
print(doc_function.__doc__)