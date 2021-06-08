#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    st = input('Введите текст ')
    n = input('Введите 2 символа ')
    count = st.count(n)
    i = 0
    while i != count:
        i += 1
        print(n)
