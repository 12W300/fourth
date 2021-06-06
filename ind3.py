#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    st = input('Введите текст ')
    sy = input('Символ ')
    t = st.find('.')
    if t != -1:
        st = st.replace('и', 'и'+sy, 1)
        print(st)
