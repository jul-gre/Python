def division(var_1,var_2):
    '''Division of two numbers'''
    if var_2 == 0:
        print ('It is incorrect')
    elif var_2 !=0:
        res = var_1 / var_2
        print ('Result: ', res)
        return division
var_1 = int(input())
var_2 = int(input())
print (division(var_1, var_2))