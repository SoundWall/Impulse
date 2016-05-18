#!/usr/bin/env python

import struct, signal

import impulse

def get_snapshot():
    return impulse.getSnapshot( True ) 

def setup():
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, "ledweb.py", 0, 0, 0)
    except:
        pass
