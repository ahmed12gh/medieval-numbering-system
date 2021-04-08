from PIL import Image , ImageDraw 
from oldNumPresset import *
import sys

imageSize = (64,64) # (width , height ) using -> imagesize[0] = firstNumber



def main():
    if sys.argv.__len__() == 2 : 
        old = OldNumber((600,600) , int(sys.argv[1]))
        old.img.show()

    elif sys.argv.__len__() == 1 :
        for i in range(0,10000): 
            oldimg = OldNumber(imageSize , i)
            oldimg.img.save('images/%s.png'%i)

if __name__ == '__main__':
    main()
