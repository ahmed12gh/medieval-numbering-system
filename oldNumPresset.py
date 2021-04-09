from PIL import Image , ImageDraw , ImageOps

class OldNumber():

    size = (300 , 300)
    img = None ; draw = None  
    borderLength = 6
    color = (255,255,255,255)
    
    def zero(self):
        # just create line 
        x ,  y  = self.size[0] / 2 , 0      # x = half  width , y = start image
        x2 , y2 = self.size[0] /2 , self.size[1] # the same x , y = end

        self.draw.line((x,y ,x2,y2) , fill=self.color , width = self.borderLength)

    def scale(self, num :int):
        if num == 0 :        # if number is units 
            return (1 ,1)

        elif num == 1 :     # if number is tens
            return (-1 , 1 ) 

        elif num == 2 :     # if number is hundreds 
            return (1 , -1 ) 

        elif num == 3 :     # if number is thousands 
            return (-1 , -1 ) 

    def num_1(self , level : int ):
        # draws one in eithir tens or units or hundreds or thousands 
        b = self.borderLength
        w , h = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy  = (  -halfW , -halfH ) 
        sclx , scly = self.scale(level) 
        
        # horizantal line 
        x  , y  = ( (halfW+ offx)*sclx      , ( b + offy)*scly ) # (halfSize , 0) 
        x2 , y2 = ( ( (3/4*w) + offx)*sclx  , (b + offy)*scly ) # (3/4 size , 0)
  
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy # removing offset  

        self.draw.line((x,y,x2,y2) , fill = self.color , width = self.borderLength)

    def num_2(self , level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 

        # horizantal line 
        x  , y  = ((halfW+offx )*sclx , (offy+halfH/2)*scly ) # (halfSize , 1/4 height)
        x2 , y2 = ((3/4 * w +offx)*sclx , (offy + halfH/2)*scly) #( 3/4 size , 1/4 height )
 
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy  # removing the offset 

        self.draw.line((x,y,x2,y2) , fill =self.color , width = self.borderLength) 


    def num_3(self , level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 

        x  , y  = ((offx + halfW)*sclx , (offy+b)*scly) # (half , 0 )
        x2 , y2 = ((3/4*w + offx)*sclx , (offy + b + halfH /2)*scly ) # 3/4 wdith , 1/4 height
 
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy # removing offset  

        self.draw.line((x,y,x2,y2) , fill=self.color , width = self.borderLength) 


    def num_4(self , level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 

        x  , y  = ((offx + 3/4*w)*sclx , (offy+b)*scly) # 3/4 width , 0  
        x2 , y2 = ((halfW + offx)*sclx , (offy + b + halfH /2)*scly ) # 1/2 width , 1/4 height 
 
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy 

        self.draw.line((x,y,x2,y2) , fill =self.color , width = self.borderLength) 

    def num_5(self, level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2)
        offx , offy   = (  -halfW , -halfH )
        sclx , scly   = self.scale(level)

        # diagonal line
        x  , y  = ((offx + 3/4*w)*sclx , (offy+b)*scly) # 3/4 width , 0
        x2 , y2 = ((halfW + offx)*sclx , (offy + b + halfH /2)*scly ) # 1/2 width , 1/4 height
        # horizantal line 
        x3 , y3 = ( (halfW+ offx)*sclx      , ( b + offy)*scly )  # 1/2 width , 0 
        x4 , y4 = ( ( (3/4*w) + offx)*sclx  , (b + offy)*scly ) # (3/4 size , 0)
        #removing offset 
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy 
        x3-=offx ; y3-=offy ; x4-=offx ; y4-=offy
        
        self.draw.line((x,y,x2,y2) , fill =self.color  , width = self.borderLength) 
        self.draw.line((x3,y3,x4,y4) , fill =self.color , width = self.borderLength)
    
    def num_6(self, level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 
        # vertical line 
        x  , y  = ((offx + 3/4*w)*sclx , (offy+b)*scly) # 3/4 width , 0 
        x2 , y2 = ((offx + 3/4*w)*sclx , (offy + b + halfH /2)*scly ) # 3/4 width , 1/4 height 
 
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy # removing offset 

        self.draw.line((x,y,x2,y2) , fill = self.color , width = self.borderLength) 


    def num_7(self, level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 
        #vertical line
        x  , y  = ( (offx + 3/4*w)*sclx , (offy+b)*scly) 
        x2 , y2 = ( (offx + 3/4*w)*sclx , (offy + b + halfH /2)*scly )
        # horizantal line  
        x3 , y3 = ( (halfW+ offx )*sclx   , ( b + offy)*scly )  
        x4 , y4 = (((3/4*w) + offx)*sclx  , (b + offy)*scly )  

        x-=offx ; y-=offy ; x2-=offx ; y2-=offy 
        x3-=offx ; y3-=offy ; x4-=offx ; y4-=offy 

        self.draw.line((x,y,x2,y2) , fill = self.color , width = self.borderLength) 
        self.draw.line((x3,y3,x4,y4) , fill =self.color , width = self.borderLength) 


    def num_8(self, level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 
        #vertical line 
        x  , y  = ( (offx + 3/4*w)*sclx   , (offy+b)*scly) # (150 , 3)
        x2 , y2 = ( (offx + 3/4*w)*sclx   , (offy + b + halfH /2)*scly )
        # down horizantal line 
        x3 , y3 = ( (halfW+ offx )*sclx   , (halfH/2 + offy)*scly ) 
        x4 , y4 = (((3/4*w) + offx)*sclx  , (halfH/2 + offy)*scly ) 
  
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy 
        x3-=offx ; y3-=offy ; x4-=offx ; y4-=offy 

        self.draw.line((x,y,x2,y2) , fill = self.color , width = self.borderLength) 
        self.draw.line((x3,y3,x4,y4) , fill = self.color , width = self.borderLength) 


    def num_9(self, level : int ):
        b             = self.borderLength
        w , h         = self.size
        halfW , halfH = (self.size[0]/2 , self.size[1] /2) 
        offx , offy   = (  -halfW , -halfH ) 
        sclx , scly   = self.scale(level) 

        # vertical line
        x  , y  = ( (offx + 3/4*w)*sclx   , (offy+b)*scly) 
        x2 , y2 = ( (offx + 3/4*w)*sclx   , (offy + b + halfH /2)*scly )
        #horizntal line up 
        x3 , y3 = ( (halfW+ offx )*sclx   , (b + offy)*scly ) 
        x4 , y4 = (((3/4*w) + offx)*sclx  , (b + offy)*scly )
        # horziantal line down 
        x5 , y5 = ((halfH + offx)*sclx , (halfH/2 + offy)*scly)
        x6 , y6 = ((3/4*w + offx)*sclx , (halfH/2 + offy)*scly)
        
        x-=offx ; y-=offy ; x2-=offx ; y2-=offy 
        x3-=offx ; y3-=offy ; x4-=offx ; y4-=offy 
        x5 -= offx ;y5 -= offy ; x6 -=offx ; y6 -=offy
        
        self.draw.line((x,y,x2,y2) , fill = self.color , width = self.borderLength) 
        self.draw.line((x3,y3,x4,y4) , fill = self.color , width = self.borderLength) 
        self.draw.line((x5,y5,x6,y6) , self.color , width=self.borderLength)
 

    def ones_tens_hudrs_thous(self, num:int):
        thousand , remain = divmod(num , 1000)
        hundreds , remain = divmod(remain ,100 )
        tens , remain = divmod(remain , 10)
        ones = remain
        
        return { 0 : ones , 1 : tens , 2 : hundreds , 3 : thousand  } 
  
    def draw_zero(self , level:int):
        # if any unit is zero this fucntion handels its args so no error
        pass

    call ={
        0 : draw_zero  ,
        1 : num_1 ,
        2 : num_2 ,
        3 : num_3 ,
        4 : num_4 ,
        5 : num_5 ,
        6 : num_6 ,
        7 : num_7 ,
        8 : num_8 ,
        9 : num_9 ,
    }
 

    def final_img(self , num : int):
        numbers = self.ones_tens_hudrs_thous(num) # gets indexes of number
        self.zero()
        self.call[ numbers[0] ](self , 0 ) # drawing ones 
        self.call[ numbers[1] ](self , 1 ) # drawing tens 
        self.call[ numbers[2] ](self , 2 ) # drawing hundreds 
        self.call[ numbers[3] ](self , 3 ) # drawing thousands 

    def __init__(self , size = (300,300) , num : int = 1111 , bgcolor = (0,0,0,0), fgcolor = (255,255,255,255) ,  border:int = 3):
        if num >= 10000:
            pass

        else : 
            self.size = size
            self.color = fgcolor
            self.img = Image.new("RGBA" ,size , bgcolor)
            self.borderLength = border
            self.draw = ImageDraw.Draw(self.img)
            self.final_img(num)

