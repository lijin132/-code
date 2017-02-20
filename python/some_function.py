#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-19 22:23:55
# @Author  : Lijin (18511681337@163.com)


def func(*num):
    """
    该func可以引入任意多的整型参数，结果返回其中最大与最小的值.

    """
    max = 0
    min = 0
    for x in num:
        if not isinstance(x, int):
            pass
        else:

            if x > max:
                max = x
            elif x < min:
                min = x

    return (max, min)


def func2(*word):
    """
    该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
    拓展：
    返回最长和最短的
    """
    leng = len(word[0])
    ma = word[0]
    for i in word:
        if not isinstance(i, str):
            pass
        else:
            if len(i) > leng:
                leng = len(i)
                ma = i
    return ma


if __name__ == '__main__':
    # print(func('-4', '1', 2, 4, -5, 6, '7', 8))
    print(func2('sssssssssssssssssssssfffff',
                'sd', 'ninininininininii', 'nishishui'))
