#!/usr/bin/python3

from ledshow import *

def isEmptyLine(line):
    if line.strip():
        return False
    else:
        return True

def getWidth(line):
    return len(line.split(' '))

def getDimensions(infile):
    height = 0
    width = 0

    with open(infile, 'r') as f:
        for line in f:
            if isEmptyLine(line):
                if height is 0:
                    continue
                else:
                    break
            else:
                width = getWidth(line)
                height += 1
                
    return width, height

def line2frame(line, height, lines_read):
    row = []
    points = line.split(' ')
    for i in range(0,len(points)):
        x = i
        y = lines_read
        rgb = points[i]
        txt = str(x) + "," + str(y) + ":"
        txt = txt + " " + rgb
        row.append(txt)
    return row

def ani2rgb(infile):
    frames = []
    frame = []
    row = []
    lines_read = 0
    (width, height) = getDimensions(infile)
    with open(infile, 'r') as f:
        for line in f:
            if isEmptyLine(line):
                frames.append(frame)
                frame = []
                row = []
                lines_read = 0
                continue
            row = line2frame(line, height, lines_read)
            frame = frame + row
            lines_read += 1

    print("\n".join(frames[1]))
    #writeFile(frames,out_file)

ani2rgb("../topline.ani")
