#!/usr/bin/env python
# coding=gb2312

def test_assert():
    mylist = ['item']
    assert len(mylist) >= 1
    mylist.pop()
    assert len(mylist) >= 1   # oohs...
# End

def test_basic():
    s = [x ** 2 for x in range(5)]  # �б����
    print(s);   # [0, 1, 4, 9, 16]

    x,y,z = 1 # ���ظ�ֵ
    x,y,z = 2, 1.25, "hello"

    x,y = 1,2
    x,y = y,x  # ֵ����
# End
if __name__ == '__main__':
    test_basic();
    test_assert();
