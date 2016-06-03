#!/usr/bin/env python

import struct, signal

import impulse
import os, numpy as np

def get_snapshot():
    return impulse.getSnapshot( True ) 

def setup():
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, "Impulse.py", 0, 0, 0)
    except:
        pass

while(True):
    data = np.array(get_snapshot()[:52])
    data = (data * 100) * (data * 100) * (data * 100)
    int_data = data.astype(int)
    print("\n".join(map(str, int_data)))
    os.system('clear')
