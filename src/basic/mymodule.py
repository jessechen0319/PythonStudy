#!/usr/bin/env python
# coding=gb2312

#�����Լ���ģ�飬���������ط�import

version = 1.0

def sayHi():
    '''mymodule sayHi, my first module'''
    print("Hi, i am mymodule\n")

if __name__ == '__main__' :
    print("----run by myself----")
else:
    print("----run by others call----")