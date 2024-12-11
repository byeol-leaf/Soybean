from PIL import Image
import os

file_path = 'E:\deeplearning project\code\Soybean\ImgTools\Bean'
file_names = os.listdir(file_path)

i=1
for name in file_names:
    img= Image.open(str(i)+'.jpg')
    img_cropped = img.crop((1008,0,4032,3024))
    img_cropped.save(str(i)+str('_Crop')+'.jpg')
    
    i+=1