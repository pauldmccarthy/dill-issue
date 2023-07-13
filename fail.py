#!/usr/bin/env python

import dill
import pkg
import pkg.run as run

pkg.modfunc()
pkg.somefunc()

with run.dryrun():
    pkg.modfunc()
    pkg.somefunc()


dill.dumps(pkg.modfunc,  recurse=True)
dill.dumps(pkg.somefunc, recurse=True)
