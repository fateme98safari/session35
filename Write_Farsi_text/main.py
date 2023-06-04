import cv2
import numpy as np 
from PIL import ImageFont,ImageDraw, Image
from bidi.algorithm import get_display

import matplotlib.pyplot as plt
import arabic_reshaper


img=Image.open("Write_Farsi_text\input\images.jpg")
draw = ImageDraw.Draw(img)  

reshaped_text = arabic_reshaper.reshape("خلیج همیشه فارس")    
bidi_text = get_display(reshaped_text)        

font=ImageFont.truetype("C:/Users/Erfam/Desktop/Narm.ttf",30)   
draw.text((0, 0), bidi_text, (255,255,255),font=font)
# draw.text((100, 100),reshaped_text , font=font)

img.save("Write_Farsi_text/output/result.png") 
img.show()