#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    st = input('Введите слово ')
    sy = input('Символ ')
    n = int(input('Номер символа '))
    t = st.find('.')
    if t != -1:
        st2 = st[:n] + sy + st[n+1:]
#        st2 = st.replace(st[n], st[n] +sy)
        print(st2)
