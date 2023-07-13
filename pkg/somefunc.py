from pkg.run import run


def func():
    print('somefunc.func')


def somefunc():
    run(func)
