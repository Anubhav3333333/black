from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode
import cv2
import time
os.system(" ID CARD Generator ")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
 
# starting position of the message
print('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company=message
color = 'rgb(0, 0, 255)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)


# adding an unique id number
(x, y) = (600, 75)
idno=random.randint(10000000,99999999)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' 
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)




(x, y) = (40, 250)
message = input('Enter Your Full Name: ')
name=message
color = 'rgb(0, 0, 0)' 
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y),"NAME: "+message, fill=color, font=font)



(x, y) = (40, 350)
message = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y),"GENDER: "+message, fill=color, font=font)

(x, y) = (420, 350)
message = input('Enter Your Age: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y),message+'yrs', fill=color, font=font)



(x, y) = (40, 450)
message = input('Enter Your Date Of Birth(EG:25JAN1961): ')
dob=message
color = 'rgb(0, 0, 0)' 
draw.text((x, y),"DOB:   "+message, fill=color, font=font)



(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
bgroup=message
color = 'rgb(0, 0, 0)'  
draw.text((x, y),"BLOODGP:   "+message, fill=color, font=font)



(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)'  
draw.text((x, y),"MOB:   "+message, fill=color, font=font)




(x, y) = (40, 750)
message = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)'  
draw.text((x, y),"ADD:   "+message, fill=color, font=font)

print('Kindly focus on your webcam')
time.sleep(1)





# save the edited image
 
image.save(str(name)+'.png')



img = qrcode.make("$Company: "+str(company)+"  $Idno: "+str(idno)+"\n$Name: "+str(name)+"\n$Bloodgp: "+str(bgroup)+"\n$Dob: "+str(dob)+")")   # this info is added in QR code
img.save(str(idno)+'.bmp')  #image is saved in bmp format

camera = cv2.VideoCapture(0)
time.sleep(0.5)
return_value, image = camera.read()
image=cv2.resize(image,(300,300))
cv2.imwrite(str(idno)+str(dob)+'.bmp', image)
del(camera) 


til = Image.open(name+'.png')
im1 =Image.open(str(idno)+str(dob)+'.bmp')
im = Image.open(str(idno)+'.bmp')
til.paste(im1,(600,180))
til.paste(im,(540,450))
til.save(name+'.png')

print(('\n\n\nYour ID Card Successfully Generated '+name+'.png'))

