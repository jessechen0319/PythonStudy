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