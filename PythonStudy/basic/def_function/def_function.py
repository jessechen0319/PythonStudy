#!/usr/bin/env python
# coding=gb2312
from time import ctime, sleep
from random import randint

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
def variadic_params(one, *nkwargs, **kwargs):
    print("print main args: %s" %str(one))
    print("print tuple args:"),
    for i in nkwargs:
       print i,
    print("\nprint dict  args��"),
    for k,v in kwargs.items():
        print("(%s : %s) " %(k, v)),
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
    variadic_params("huo",5,"d",a=1)
    variadic_params(1,v=1, z=1234)
    variadic_params(2, *(4, 6, 8), **{'foo': 10, 'bar': 12}) 
    aTuple = (6, 7, 8) 
    aDict = {'z': 9} 
    variadic_params(4, 9, x=2, y=1, *aTuple, **aDict)  # ���ַ�ʽ̫����ˣ�

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

# �ڲ�����
def outerFunc():
    def innerFunc():
        print("innerFunc")
    print("outerFunc")
    innerFunc()
# End

def test_innerFunc():
    outerFunc()   # ok
   # innerFunc()   # error, �������ɼ�
# End

# װ�������������ڰ�װ�Ļ������ں��ʵ�ʱ����������������ִ�к���֮ǰ����������ЩԤ�����룬Ҳ������
# ִ�д���֮����Щ�����������Ե��㿴��һ��װ����������ʱ�򣬺ܿ����������ҵ�����һЩ���룬 
# ��������ĳ���������ڶ����ڵ�ĳ��Ƕ���˶�Ŀ�꺯���ĵ��û�������һЩ���á� �ӱ����Ͽ���
#��Щ���������� java �����߳ƺ�֮Ϊ AOP ��Aspect Oriented Programming�� �������̣� �ĸ��
# װ�������﷨��@��ͷ��������װ�������������ֺͿ�ѡ�Ĳ�����������װ�����������Ǳ����εĺ�������װ�κ����Ŀ�ѡ������
def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    print("---foo()---")

def test_aop():
    foo()   # �൱������������foo֮ǰ����ִ��tsfunc
    sleep(3)
    for i in range(2):
        sleep(1)
        foo()
    tsfunc(foo)()
# End

# ���ݺ����������ǿɵ��õ�
def convert(func, seq):
	'conv. sequence of numbers to same type'
	return [func(eachNum) for eachNum in seq]

def test_func():
    myseq = (123, 45.67, -6.2e8, 999999999L)
    print convert(int, myseq)
    print convert(long, myseq)
    bar = convert  # bar ���� convert
    print bar(float, myseq)
# End

# �ڽ�����filter��map��reduce��ʹ��
def test_filter_map_reduce():
    #### filter(func, seq)
    def is_odd(n):     # �ж�����
        return n % 2 != 0

    num1 = []
    for i in range(9):   # ����9�������
        num1.append(randint(1,99))
    print num1

    num = filter(is_odd, num1)   # ������num1Ԫ����ε��ò�������is_odd��Ϊtrue�򷵻ظ�Ԫ��
    print num

    num = filter(lambda n : n%2!=0, num1)
    print num

    num = [n for n in num1 if n %2!=0]
    print num

    num = [n for n in [randint(1, 99) for i in range(9)] if n%2 !=0]
    print num

    #### map(func, seq1, seq2...)
    num = map(lambda x : x + 2, [0,1,2,3,4])
    print num 

    num = map(lambda x : x**2, range(5))
    print num 

    num = [x**2 for x in range(5)]
    print num 

    num = map(lambda x,y : x+y, [1,2,3], [4,5,6])
    print num 
    num = map(lambda x,y : (x+y,x-y), [1,2,3], [4,5,6])
    print num 
    num = map(None, [1,2,3], [4,5,6])
    print num 

    #### reduce(func, seq[, init])
    def mysum(x,y) : return x+y
    num2 = range(1,6)
    total = 0
    for x in num2:
        total = mysum(total, x)
    print total
    
    total = reduce((lambda x,y : x+y), range(1,6))
    print total 

# End

if __name__ == '__main__':
    test1()
    print("*******************************************")
    test_variadic()
    print("*******************************************")
    test_innerFunc()
    print("*******************************************")
    test_aop()
    print("*******************************************")
    test_func()
    print("*******************************************")
    test_filter_map_reduce()