#!/usr/bin/env python
# coding=gb2312

# ����python�еĺ�������͵��÷�ʽ��ע�ⶨ��ʱ�����������":"��
def sayHello():
    '''my first function, using python'''
    print("hello world")

def sayHello2(msg):   # �˴�����дsayHello��ò��û�к�������
    '''my second function, using python'''
    print(msg)

def sayHello3(msg, times = 1): 
    '''my third function, using python'''
    print(msg * times)

def add(a, b = 2, c = 10):
    '''add thread int num, and then return the sum'''
    d = a + b + c
    print("%d + %d + %d = %d" % (a, b, c, d))   # ������C�������ƣ�ע�������ǰ��Ҫ��()��Χ������ǰ��%����
    #print(a, "+", b, "+", c, "=", d)  # ok too
    return d;

def test1():
    sayHello()  #call this func
    sayHello2("new function")  #call this func
    sayHello3("sayHello3")
    sayHello3("sayHello3", 3)
    
    add(1)
    add(1, 2)
    add(1, 2, 3)
    add(3, c = 5)   # ���ֵ��÷�ʽ������Cϵ���ԣ�����a,b,c��������ģ��˴���Ϊ�ؼ�����
    add(b = 3, a = 0, c=0)
    print(add(a=3, c=4))
    print(add.__doc__)

#### ���Ա䳤���� ####
# ������ǰ��һ��*����ʾ������в�������һ��Ԫ�飬������**��������в�������һ���ֵ�
def variadic_params(*nkwargs, **kwargs):
    print("print tuple args:"),
    for i in nkwargs:
       print i,
    print("\nprint dict  args��"),
    for k,v in kwargs:
        print("%s : %s" %(k, v))
    print("\nprint over")
# End

def variadic_func(func, *nkwargs, **kwargs):
   try:
       retval = func(*nkwargs, **kwargs)
       result = (True, retval)
   except Exception, diag:
       result = (False, str(diag))
   return result
# End

def test_variadic():
    
    variadic_params(1,2,3)
    variadic_params(1)
    variadic_params(2,5,"d", "a=1", {"b" : "2", "v" : 80})
    variadic_params("v=1", "z=1234")

    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')
    
    for eachFunc in funcs:
        print '-' * 20
        for eachVal in vals:
            retval = variadic_func(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) =' %(eachFunc.__name__, `eachVal`), retval[1]
            else:
                print '%s(%s) = FAILED:' %(eachFunc.__name__, `eachVal`), retval[1]

# End

if __name__ == '__main__':
    test1()
    print("*******************************************")
    test_variadic()
    print("*******************************************")
