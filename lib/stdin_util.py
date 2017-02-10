#!/usr/bin/env python

import fcntl
import os
import subprocess
import sys
import tempfile
import termios


def iter_read_char():
    """ iterate each character coming from standard input """
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:
        while 1:
            try:
                yield sys.stdin.read(1)
            except IOError:
                pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


def iter_read_line():
    """ yields each line from standard input """
    lines = {}
    try:
        for r in iter_read_char():
            if 'line' not in lines:
                lines['line'] = ''
            if r != "\n":
                lines['line'] += r
            else:
                print '{0}'.format(lines['line'])
                yield lines['line']
                del(lines['line'])

    except KeyboardInterrupt:
        raise StopIteration


def read_from_editor(start_buffer='', editor=os.environ.get('EDITOR', 'vim')):
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tmp:
        tmp.write(start_buffer)
        tmp.flush()
        subprocess.call([editor, tmp.name])
        # tmp.write('\n')
        tmp.seek(0)
        return tmp.read()
