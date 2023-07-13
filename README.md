# Dill issue #604

This repository contains a small example that causes [dill](https://github.com/uqfoundation/dill/) to raise a `RecursionError` in certain situations. The issue is reported at https://github.com/uqfoundation/dill/issues/604

I'm sure that it would be possible to devise a more minimal example, but I don't understand dill well enough to propose something simpler.


The code is structured as follows:

 - There are two functions - `pkg.somefunc.somefunc` and `pkg.somemod.modfunc`.
 - Both of these functions are exposed in the `pkg` namespace (refer to `pkg/__init__py`).
 - Both functions use a utility function, `pkg.run.run`, to execute a process.
 - The `pkg.run.run` function has a feature whereby it can perform a "dry run", where it prints out what would be executed, rather than actually executing. This feature is controlled by a module-level global variable `pkg.run.DRY_RUN`.
 - The `pkg.run` module has another function - `pkg.run.dryrun` - which can be used as a context manager to temporarily enable `DRY_RUN`, e.g.:
     ```
     import pkg
     import pkg.run
     with pkg.run.dryrun():
         pkg.somefunc()
         pkg.modfunc()
     ```
 - The `dryrun` context manager function attaches a list to itself, `dryrun_calls` - whenever the `run` function performs a dry run, it adds the command that would be executed to that list. This is used for testing/diagnostic purposes.


Run with a Python environment with dill installed:

```
git clone https://github.com/pauldmccarthy/dill-issue.git
cd dill-issue
python fail.py
```
