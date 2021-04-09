from oldNumPresset import *
import sys ,os 

imageSize = (64,64) # (width , height ) 
backgroundColor = (0,0,0,0) # transparneta
fgColor = (255,255,255,255)
borderSize = 3
imagespath = 'data/' # should have a '/'

def main():
    if not os.path.isdir(imagespath):
        os.makedirs(imagespath)
    if sys.argv.__len__() == 2 and int(sys.argv[1]) <= 9999: 
        old = OldNumber(imageSize , int(sys.argv[1]) , backgroundColor,fgColor , borderSize)
        old.img.save(imagespath + '%s.png'%sys.argv[1])
        old.img.show()

    elif sys.argv.__len__() == 1 :
        for i in range(0,10000): 
            oldimg = OldNumber(imageSize , i , bgcolor=backgroundColor , fgcolor = fgColor , border=borderSize)
            oldimg.img.save(imagespath + '%s.png'%i)
    else :
        print("Sorry there is no number like that in this numbering system \n"
       , " , But you can type any number from 0 -> 9999 and its fine" )
        
if __name__ == '__main__':
    main()
