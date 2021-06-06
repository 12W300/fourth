#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s1 = input('Первое слово ')
    s2 = input('Второе слово ')
    s3 = ('')
    l1 = len(s1)
    l2 = len(s2)
    f = 1
    for i in range(l2):
        if s3.find(s2[i]) == -1:
            s3 += s2[i]
    l3 = len(s3)
    for i in range(l3):
        if s1.find(s3[i]) == -1:
            f = 0
    if f == 1:
        print('Условие 1 выполнено')
    else:
        print('Условие 1 не выполнено')
    if l1 == l2:
        for i in range(l2):
            if s1.find(s2[i]) != -1:
                s1 = s1.replace(s2[i], '')
        if s1 == '':
            print('Условие 2 выполнено')
        else:
            print('Условие 2 не выполнено')
    else:
        print('Условие 2 не выполнено')
