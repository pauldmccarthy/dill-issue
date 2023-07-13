#!/usr/bin/env python

from pkg.run import run


def func():
    print('somemod.func')


def modfunc():
    run(func)
