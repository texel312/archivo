import sys
import serial
from PyQt5.QtCore import Qt
puertoserie = serial.Serial(
 port="COM1",
#"/dev/ttyUSB0"
    #/dev/ttyS0
 baudrate= 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1

)

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget
from ejemplo16 import *

class MyForm(QMainWindow):
   def __init__(self):
       super().__init__()
       # this will hide the title bar
       self.setWindowFlag(Qt.FramelessWindowHint)
    
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)
       self.ui.pushButton_2.clicked.connect(self.dispmessage)
       self.ui.pushButton.clicked.connect(self.dispmessage2)
       self.ui.pushButton_3.clicked.connect(self.dispmessage3)
       self.ui.pushButton_4.clicked.connect(self.dispmessage4)
       self.ui.var=0x00
       self.show()
   def dispmessage(self):
       self.ui.stackedWidget.setCurrentIndex(0)
       self.var=0x11


   def dispmessage2(self):
       self.ui.stackedWidget.setCurrentIndex(1)

   def dispmessage3(self):
           packet = bytearray()
           packet.append(0x0B)
           packet.append(self.var)
           packet.append(0x00)
           packet.append(0x00)
           packet.append(0x00)
           puertoserie.write(packet)

   def dispmessage4(self):
           packet1 = bytearray()
           packet1.append(0x09)
           packet1.append(0x20)
           packet1.append(0x04)
           packet1.append(0x01)
           packet1.append(0x01)
           puertoserie.write(packet1)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     w = MyForm()
     w.show()
     sys.exit(app.exec_())