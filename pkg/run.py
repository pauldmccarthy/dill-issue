#!/usr/bin/env python

from contextlib import contextmanager


DRY_RUN = False


@contextmanager
def dryrun():

    global DRY_RUN

    DRY_RUN = True
    dryrun.dryrun_calls = []
    try:
        yield

    finally:
        DRY_RUN = False


def run(func, *args, **kwargs):
    if DRY_RUN:
        print(f'Dry run: {func.__name__}({args}, {kwargs})')
        getattr(dryrun, 'dryrun_calls', []).append((func.__name__, args, kwargs))
    else:
        print(f'Running: {func.__name__}({args}, {kwargs})')
        return func(*args, **kwargs)
