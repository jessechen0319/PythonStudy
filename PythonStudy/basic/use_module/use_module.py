#!/usr/bin/env python
# coding=gb2312

#���ⲿʹ��ʱ������
#use_module.py  ����
#use_module.py 1 2 argu
#�ͻ�ͨ��sys.argv��ӡ�����г������
#����C�����е�int main(int argc[], char **argv)

import sys
import mymodule

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')


print("--------------------\n")
mymodule.sayHi()

print('mymodule.version : ', mymodule.version)
print(mymodule.sayHi.__doc__)


#ʹ���ڽ���dir�������г�ģ�鶨��ı�ʶ������ʶ���к�������ͱ�����
#����Ϊdir()�ṩһ��ģ������ʱ��������ģ�鶨��������б�������ṩ�����������ص�ǰģ���ж���������б�
s = dir(mymodule.sayHi)
print(s)

print("\n")
print(dir())  # ��������ʱ���ص�ǰģ��������б�