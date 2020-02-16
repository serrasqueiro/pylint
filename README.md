# pylint fork @serrasqueiro

This is a fork from pylint ([github pylint](https://github.com/PyCQA/pylint)).
Motivation was the fact I like code-style
        ``f = a( 1, 2, 3)``
and warnings like
* ``C0326: No space allowed after bracket``
  + due to the following code (example):
    - ``        year = int( self.xdate / (10**4) )``
are annoying!
* See also [stack overflow - thread](https://stackoverflow.com/questions/33876495/how-to-disable-no-space-allowed-around-keyword-argument-assignment-in-pylint).

## Hints

Just do ``git remote add upstream https://github.com/PyCQA/pylint``
to keep this repo syncronized with the original project from where this got
forked from.

To keep up with upstream (original) repo, do:
* ``git merge upstream/master``
* See also [github help](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork).

