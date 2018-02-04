#COMPUTER SCRIPT

import wx
import ftplib
from PIL import Image
from VideoCapture import Device
imageVersion = 6
cam = Device()
imageName = 'image'+str(imageVersion)+'.jpg'

class MyFrame(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Add Face to Authorized List', size=(800,800))
		panel=wx.Panel(self)
		picButton=wx.Button(panel,label="Take Picture",pos=(200,10),size=(100,30))
		saveButton=wx.Button(panel,label="Save Picture",pos=(400,10),size=(100,30))
		
		self.Bind(wx.EVT_BUTTON, self.takePic, picButton)
		self.Bind(wx.EVT_BUTTON, self.savePic, saveButton)
		
	def takePic(self,event):
		imageName = 'image'+str(imageVersion)+'.jpg'
		cam.saveSnapshot(imageName)
		jpg = wx.Image(imageName, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		wx.StaticBitmap(self, -1, jpg, (50, 50), (700, 700))
		
	def savePic(self,event):
		session = ftplib.FTP('ftp.easyin.org','apiaccess@easyin.org','h@lZN2x2eCX)')
		file = open(imageName,'rb')                  # file to send
		session.storbinary('STOR '+imageName, file)     # send the file
		file.close()                                    # close file and FTP
		session.quit()
		
	# def savePic(self, event):
		
if __name__ == '__main__':		
	app=wx.App()
	frame=MyFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()