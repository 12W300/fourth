#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input('Введите текст ')
    c1 = s.count('жы')
    c2 = s.count('шы')
    print('Ошибок жы - ', c1)
    print('Ошибок шы - ', c2)
