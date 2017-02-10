from __future__ import absolute_import


def green(string, bold=False):
    num = 32
    if not bold:
        return '\x1b[%sm%s\x1b[0m' % (num, string)
    else:
        return "\033[1;%sm%s\033[1;0m" % (num, string)


def red(string, bold=False):
    num = 31
    if not bold:
        return '\x1b[%sm%s\x1b[0m' % (num, string)
    else:
        return "\033[1;%sm%s\033[1;0m" % (num, string)


def cyan(string, bold=False):
    num = 36
    if not bold:
        return '\x1b[%sm%s\x1b[0m' % (num, string)
    else:
        return "\033[1;%sm%s\033[1;0m" % (num, string)
