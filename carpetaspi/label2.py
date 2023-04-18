import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from label import *
class MyForm(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.posxy = [0,0]
            self.sumafrec=0
            self.v1=0
            self.v2=0
            self.v3=0
            self.v4=0
            self.v5=0
            self.v6=0
            self.v7=0
            self.v8=0
            self.timerf1 = QtCore.QTimer(self)
            self.timerf1.timeout.connect(self.parar_gif_f1)
            self.timerf2 = QtCore.QTimer(self)
            self.timerf2.timeout.connect(self.parar_gif_f2)
            self.timerf3= QtCore.QTimer(self)
            self.timerf3.timeout.connect(self.parar_gif_f3)
            self.timerf4 = QtCore.QTimer(self)
            self.timerf4.timeout.connect(self.parar_gif_f4)
            self.show()

        def mousePressEvent(self, event):
            self.posxy[0], self.posxy[1] = event.pos().x(), event.pos().y()

            if self.posxy[0]<92 and self.posxy[0]>30 and self.posxy[1]<252 and self.posxy[1]>190:
                    self.v1 = 8
                    self.reproducir1_gif()

            if self.posxy[0] < 160 and self.posxy[0] > 100 and self.posxy[1] < 252 and self.posxy[1] > 190:
                    self.v2 = 4
                    self.reproducir2_gif()

            if self.posxy[0] < 230 and self.posxy[0] > 173 and self.posxy[1] < 252 and self.posxy[1] > 190:
                    self.v3 = 2
                    self.reproducir3_gif()

            if self.posxy[0] < 300 and self.posxy[0] > 240 and self.posxy[1] < 252 and self.posxy[1] > 190:
                    self.v4 = 1
                    self.reproducir4_gif()
            self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4


        def mouseReleaseEvent(self, event):

            if self.sumafrec==10 or self.sumafrec==11 or self.sumafrec==9:
                self.v2=4
                self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
                self.reproducir2_gif()
            if self.sumafrec==5 or self.sumafrec==13 or self.sumafrec==9:
                self.v3=2
                self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
                self.reproducir3_gif()
            print(self.v1)
            print(self.v2)
            print(self.v3)
            print(self.v4)
        def parar_gif_f1(self):
            self.movie1.stop()
        def parar_gif_f2(self):
            self.movie2.stop()
        def parar_gif_f3(self):
            self.movie3.stop()
        def parar_gif_f4(self):
            self.movie4.stop()

        def reproducir1_gif(self):
            self.timerf1.start(2000)
            if self.v5==0:
               self.movie1 = QMovie("prendido.gif")
            if self.v5==1:
                self.movie1 = QMovie("apagado.gif")
                self.v1=0
            self.ui.label.setMovie(self.movie1)
            self.movie1.start()
            self.v5 = not self.v5
        def reproducir2_gif(self):
            self.timerf2.start(2000)
            if self.v6 == 0:
                self.movie2 = QMovie("prendido.gif")
            if self.v6 == 1:
                self.movie2 = QMovie("apagado.gif")
                self.v2=0
            self.ui.label2.setMovie(self.movie2)
            self.movie2.start()
            self.v6 = not self.v6
        def reproducir3_gif(self):
            self.timerf3.start(2000)
            if self.v7 == 0:
                self.movie3 = QMovie("prendido.gif")
            if self.v7 == 1:
                self.movie3 = QMovie("apagado.gif")
                self.v3=0
            self.ui.label3.setMovie(self.movie3)
            self.movie3.start()
            self.v7 = not self.v7
        def reproducir4_gif(self):
            self.timerf4.start(2000)
            if self.v8 == 0:
                self.movie4 = QMovie("prendido.gif")
            if self.v8 == 1:
                self.movie4 = QMovie("apagado.gif")
                self.v4=0
            self.ui.label4.setMovie(self.movie4)
            self.movie4.start()
            self.v8 = not self.v8



if __name__=="__main__":
 app = QApplication(sys.argv)
 w = MyForm()
 w.show()
 sys.exit(app.exec_())