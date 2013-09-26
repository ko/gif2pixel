#!/usr/bin/python3

class Frame:

    def __init__(self):
        self.pixels = [];
        self.empty = True

    def addPixel(self, xy, rgb):
        # flag
        self.empty = False

        pixel = Pixel()
        tuple = xy.split(',')
        pixel.setXY(tuple)

        rgb = re.sub('[()]', '', rgb)
        tuple = rgb.split(',')
        pixel.setRGB(tuple)
        self.pixels.append(pixel)

    def isEmpty(self):
        return self.empty

    def getPixel(self, x, y):
        # lol so bad
        for item in self.pixels:
            if item.getX() == str(x) and item.getY() == str(y):
                return item
        print("Could not find",str(x),",",str(y))
        return None

    def toString(self, binary=False):
        out = []
        if binary is True:
            out = array.array('B')
        # dimensions here
        """
       o------------>   #1 
        <------------   #2
        ------------>x  #3
        """
        for j in range(3,-1,-1):
            if j % 2 == 1:
                for i in range(0,8):
                    pixel = self.getPixel(i,j)
                    if pixel is not None:
                        if binary is True:
                            out.append(int(pixel.toBinaryString()[0],2))
                            out.append(int(pixel.toBinaryString()[1],2))
                            out.append(int(pixel.toBinaryString()[2],2))
