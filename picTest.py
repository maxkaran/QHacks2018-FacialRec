#test taking pictures

from PIL import Image
from VideoCapture import Device

cam = Device() #devnum=0 means you are using the device set in 0 position probably your webcam
blackimg = cam.getImage() #this return a PIL image but I don't know why the first is always black
#blackimg.show()#try to check if you want
Image=cam.getImage() #this is a real image PIL image
#Image.show()

cam.saveSnapshot('image.jpg')