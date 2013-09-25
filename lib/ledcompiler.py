#!/usr/bin/python2

import re
import array

class Frame:

    def __init__(self):
        self.pixels = [];

    def addPixel(self, xy, rgb):
        pixel = Pixel()
        tuple = xy.split(',')
        pixel.setXY(tuple)

        rgb = re.sub('[()]', '', rgb)
        tuple = rgb.split(',')
        pixel.setRGB(tuple)
        self.pixels.append(pixel)

    def newFrame(self):
        print "Found new frame"
        """
        if self.pixels is not None:
            self.pixels.append(Pixel())
        """

    def getPixel(self, x, y):
        # lol so bad
        for item in self.pixels:
            if item.getX() == str(x) and item.getY() == str(y):
                return item
        print "Could not find " + str(x) + "," + str(y)
        return None

    def toString(self, binary=False):
        out = []
        if binary is True:
            out = array.array('B')
        # dimensions here
        """
       o------------>   #1 
        ------------>   #2
        ------------>x  #3
        """
        for i in range(0,8):
            for j in range(3,-1,-1):
                pixel = self.getPixel(i,j)
                if pixel is not None:
                    if binary is True:
                        out.append(int(pixel.toBinaryString()[0],2))
                        out.append(int(pixel.toBinaryString()[1],2))
                        out.append(int(pixel.toBinaryString()[2],2))
                    else:
                        out.append(pixel.toString())
        if binary is True:
            return out
        else:
            return ''.join(out).strip()

class Pixel:

    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.x = 0
        self.y = 0

    def setXY(self, tuple):
        self.x = tuple[0]
        self.y = tuple[1]

    def getX(self):
        return str(self.x).strip()

    def getY(self):
        return str(self.y).strip()

    def setRGB(self, tuple):
        self.r = tuple[0]
        self.g = tuple[1]
        self.b = tuple[2]

    def getR(self):
        return str(self.r).strip()

    def getG(self):
        return str(self.g).strip()

    def getB(self):
        return str(self.b).strip()

    def getBinaryR(self):
        return int(bin(int(self.r))[2:])

    def getBinaryG(self):
        return int(bin(int(self.g))[2:])

    def getBinaryB(self):
        return int(bin(int(self.b))[2:])

    def toString(self):
        out = []
        out.append(self.getR())
        out.append(self.getG())
        out.append(self.getB())
        return ''.join(out)

    def toBinaryString(self):
        out = []
        out.append(str(self.getBinaryR()))
        out.append(str(self.getBinaryG()))
        out.append(str(self.getBinaryB()))
        return out

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

def rgb2bin(txt_file,out_file):
    frames = []
    frame = Frame()
    with open(txt_file, 'rw') as f:
        for line in f:
            if not parseLine(frame,line):
                frames.append(frame)
    f = file(out_file, 'wb')
    output = setupHeader()
    for frame in frames:
        output += frame.toString(True)
    output.tofile(f)
    f.close()

