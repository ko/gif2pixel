#!/usr/bin/python3

import re
import array

from ledshow import *

def setupHeader():
    out = array.array('B')
    out.append(0)
    out.append(50)
    out.append(8)
    out.append(0)
    out.append(4)
    out.append(0)
    return out

def parseLine(frame, line):
    if line.strip():
        tuple = line.partition(':')
        frame.addPixel(tuple[0],tuple[2])
        return True
    else:
        return False

def writeFile(frames,out_file):
    f = file(out_file, 'wb')
    output = setupHeader()
    for frame in frames:
        print('Add frame')
        output += frame.toString(True)
    output.tofile(f)
    f.close()

def rgb2bin(txt_file,out_file):
    frames = []
    frame = Frame()
    with open(txt_file, 'rw') as f:
        for line in f:
            if not parseLine(frame,line):
                if not frame.isEmpty():
                    frames.append(frame)
                    frame = Frame()
    writeFile(frames,out_file)

