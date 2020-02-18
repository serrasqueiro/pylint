# -*- coding: utf-8 -*-
# Copyright (c) 2020 HMoreira <h@serrasqueiro.com>

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING
# or at this repository fork: https://github.com/serrasqueiro/pylint.git

# pylint: disable=broad-except


"""Prized module.

Companion for debug.
"""

from sys import stdout


class PDebug():
    """
    PDebug - a simple class for debugging.
    """
    def __init__(self, module_name=".", class_name=None, default_level=0, err_file=None):
        self.name = module_name
        self.cname = class_name
        self.set_debug_level(default_level)
        self.err_file = err_file if err_file is not None else stdout
        self._auto_nl = True


    def has_debug(self):
        assert 0 <= self.level <= 9
        return self.level > 0


    def set_debug_level(self, level):
        assert isinstance(level, int)
        assert 0 <= level <= 9
        self.level = level


    def echo(self, *args):
        if self.level <= 0:
            return False
        assert self.err_file is not None
        if args == []:
            return False
        one = args[0]
        rest = args[1:]
        if one == "[DEBUG]":
            one = "[DEBUG:{}] ".format(self._best_name())
        s = one
        for arg in rest:
            s += "{}".format(arg)
        if s == "":
            return s
        if self._auto_nl:
            if not s.endswith("\n"):
                s += "\n"
        self.err_file.write(s)
        return True


    def _best_name(self):
        if self.cname == None:
            s = self.name
        else:
            s = self.cname
        return s

if __name__ == "__main__":
    print("Import this module!")
