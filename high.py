#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s1 = input('Первое слово ')
    s2 = input('Второе слово ')
    s3 = s1 + s2
    l3 = len(s3)
    i = 0
    while i < l3:
        f = 1
        ch = s3[i]
        j = 0
        while j < l3:
            if (ch == s3[j]) and (i != j):
                f = 0
            j += 1
        if f == 1:
            print(ch)
        i += 1
