


import sys
import serial
import principal
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QTimer, QTime, Qt
import time

puertoserie = serial.Serial(
 port="/dev/ttyS0",
#"/dev/ttyUSB0"
    #/dev/ttyS0
 baudrate= 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1

)


from pantallaprincipal2 import *

class MyForm(QDialog):
   def __init__(self):
       super().__init__()
       # this will hide the title bar
       self.setWindowFlags(Qt.FramelessWindowHint)
       self.setMouseTracking(True)
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
       self.posxy = [0, 0]
       self.posxy2 = [0, 0]
       self.pausarsesion=0
       self.v1 = 0
       self.v2 = 0
       self.v3 = 0
       self.v4 = 0
       self.v5 = 0
       self.v6 = 0
       self.v7 = 0
       self.v8 = 0

       self.sumafrec=8
       self.contadorpotencia=0
       self.potencia=0
       self.counter = 60
       self.segundo=60
       self.minute = '10'
       self.minuto=10
       self.second = '00'
       self.count = '00'
       self.contador=0
       self.minutosesion='10'
       self.segundosesion='00'
       self.aux1=10
       self.aux2=0
       self.valorpotencia=0
       self.potencia=0
       self.iniciarsesion = False
       self.pause=False
       self.cambiarsexo = 0
       self.varx=0
       self.vary=0
       self.text=""
       self.minutomodif=0
       self.minutostr=""
       self.cabezalactivo=0
       self.frio=0
       self.estado=bytearray(5)
       self.setMouseTracking(True)
       self.seteosesion = True
       self.auxiliar = 0
       self.timerest1 = QtCore.QTimer(self)
       self.timerest1.timeout.connect(self.leerestado)
       self.timerest2 = QtCore.QTimer(self)
       self.timerest2.timeout.connect(self.pedirestado)
       self.timerf1 = QtCore.QTimer(self)
       self.timerf1.timeout.connect(self.parar_gif_f1)
       self.timerf2 = QtCore.QTimer(self)
       self.timerf2.timeout.connect(self.parar_gif_f2)
       self.timerf3 = QtCore.QTimer(self)
       self.timerf3.timeout.connect(self.parar_gif_f3)
       self.timerf4 = QtCore.QTimer(self)
       self.timerf4.timeout.connect(self.parar_gif_f4)
       self.timer = QTimer(self)
       self.reproducirgifpresentacion()
       self.ui.verticalSlider.valueChanged.connect(self.cambiarpotencia)
       self.ui.verticalSlider.sliderReleased.connect(self.actualizar)
       # adding action to timer
       self.timer.timeout.connect(self.iniciartimersesion)
       self.ui.lcdNumber.hide()
       # update the timer every second
       self.timer.start(1000)
       self.inicializar()
       self.ui.confirmar.clicked.connect(self.confirmardetener)
       self.ui.cancelar.clicked.connect(self.cancelardetener)
       self.bloquearpag0=0
       self.bloquearpag1 = 1
       self.show()


#////////// BLOQUE INICIALIZACION Y CICLO DE CONSULTA DE ESTADO DEL SISTEMA////////////////////////////////////////

   def inicializar(self):

       self.v1 = 8
       self.reproducir1_gif()
       self.cabezalactivo = 1
       self.ui.label6.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal1_activ.png);\n" "")
       self.ui.label7.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal2_desac.png);\n" "")
       self.ui.label8.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal4_desac.png);\n" "")
       self.ui.label9.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal3_desac.png);\n" "")
       self.pedirestado()


       # escribe datos serie, en particular envia el comando 0x01

   def pedirestado(self):

       packet = bytearray()
       packet.append(0x01)
       packet.append(0x00)
       packet.append(0x00)
       packet.append(0x00)
       packet.append(0x00)
       puertoserie.write(packet)
       self.timerest1.start(1000)


#lee datos serie
   def leerestado(self):

       if(puertoserie.in_waiting > 0):

           self.estado = puertoserie.read(5)
           if self.estado[0]==0x01:


            if self.estado[2] == 255:
               self.ui.label_3.setText("-1")
            else:
               self.ui.label_3.setText(str(self.estado[2]) + '°C')


            self.estadodelsistema()
            #print(self.estado[0])
            print(hex(self.estado[0]))
            print(hex(self.estado[1]))
            print(self.estado[2])


       # esta funcion se encarga llamar a la funcion de consulta de estado cada 4 segundos

   def estadodelsistema(self):
       self.timerest2.start(4000)

#//////////////////////////////////////////////////////////////////////////////////////////////////////





#manejo de nivel de potencia. La funcion "actualizar" se llama cada vez que se suelta el slider. la razon que se llame a  la funcion "enviardatos..." es para asegurarse de enviar el valor correspondiente actualziado. si no uso la funcion actualizar, sucede que al bajar la potencia a cero, en la placa no va a cero sino a nu valor cercano.
   def cambiarpotencia(self):

       self.valorpotencia = int(self.ui.lcdNumber.value())
       self.ui.label19.setText(str(self.valorpotencia) + '%')


       if self.iniciarsesion == True:
           self.enviardatosdesesion()


   def actualizar(self):
       if self.iniciarsesion == True:
           self.enviardatosdesesion()



# tiempo de sesion
   def iniciartimersesion(self):

     if  self.iniciarsesion==True and self.pause==False:
         self.segundo= self.segundo -1
         if self.segundo < 10 and self.segundo>=0:
             self.segundosesion = '0' + str(self.segundo)
         else:
             self.segundosesion = str(self.segundo)
         if self.segundo < 0:
             self.segundosesion = '59'
             self.segundo=59
             self.minuto=self.minuto-1
         if self.minuto<=10 and self.minuto>=0:
             self.minutosesion= '0' + str(self.minuto-1)
         else:
             self.minutosesion= str(self.minuto-1)

         self.text = self.minutosesion + ':' + self.segundosesion
         self.ui.label16.setText(self.text)

         if self.minutosesion == '00' and self.segundosesion == '00':
            self.iniciarsesion = False
            self.parar_gif_reloj()
            self.detenersesion()
            self.auxiliar = 1
            self.segundo=60
            self.minuto = self.aux1
            self.confirmardetener()





   

   #la siguiente funcion se ejecuta cada vez que se detecta un click en la pantalla
   def mousePressEvent(self, event):

       #manejo de las paginas


       self.posxy[0], self.posxy[1] = event.pos().x()*self.bloquearpag0, event.pos().y()*self.bloquearpag0
       self.posxy2[0], self.posxy2[1] = event.pos().x()*self.bloquearpag1, event.pos().y()*self.bloquearpag1


       #print(self.posxy[0])
       #print(self.posxy[1])



       if self.posxy2[0] < 1280 and self.posxy2[0] > 0 and self.posxy2[1] < 800 and self.posxy2[1] > 0:

           self.ui.stackedWidget.setCurrentIndex(0)
           self.ui.stackedWidget.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/Pantalla Grande8.png);\n""")
           self.bloquearpag0 = 1
           self.bloquearpag1 = 0

       if self.posxy[0] < 150 and self.posxy[0] > 67 and self.posxy[1] < 98 and self.posxy[1] > 34:

           self.ui.stackedWidget.setCurrentIndex(1)
           self.ui.stackedWidget.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/Pantalla Grande5.png);\n""")
           self.bloquearpag0 = 0
           self.bloquearpag1 = 1


       # Manejo de la seleccion de frecuencias y sus respectivas animaciones

       if self.posxy[0] <114  and self.posxy[0] > 50 and self.posxy[1] < 613 and self.posxy[1] > 550 :
           self.v1 = 8
           self.reproducir1_gif()
           self.resolverfrec()




       if self.posxy[0] < 270 and self.posxy[0] > 206 and self.posxy[1] < 613 and self.posxy[1] > 550 :
           self.v2 = 4
           self.reproducir2_gif()
           self.resolverfrec()



       if self.posxy[0] < 424 and self.posxy[0] > 362 and self.posxy[1] < 613 and self.posxy[1] > 550 :
           self.v3 = 2
           self.reproducir3_gif()
           self.resolverfrec()



       if self.posxy[0] < 579 and self.posxy[0] > 515 and self.posxy[1] < 613 and self.posxy[1] > 550  :
           self.v4 = 1
           self.reproducir4_gif()
           self.resolverfrec()







   # Manejo de la imagen de seleccion de sexo

       if self.posxy[0] < 1200 and self.posxy[0] > 1000 and self.posxy[1] < 700 and self.posxy[1] > 300  :
           if self.cambiarsexo==0:
              self.ui.label5.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/figura_hombre.png);\n""")
           if self.cambiarsexo==1:
              self.ui.label5.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/figura_mujer.png);\n""")
           self.cambiarsexo= not self.cambiarsexo

   #Manejo de la parte de seleccion de cabezal

       if self.posxy[0] < 730 and self.posxy[0] > 670 and self.posxy[1] < 670 and self.posxy[1] > 536 :
                 self.cabezalactivo = 1
                 self.ui.label6.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal1_activ.png);\n" "")
                 self.ui.label7.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal2_desac.png);\n" "")
                 self.ui.label8.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal4_desac.png);\n" "")
                 self.ui.label9.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal3_desac.png);\n" "")
                 if self.iniciarsesion == True:
                     self.enviardatosdesesion()





       if self.posxy[0] < 800 and self.posxy[0] > 750 and self.posxy[1] < 670 and self.posxy[1] > 536 :
                 self.cabezalactivo = 2
                 self.ui.label6.setStyleSheet( "background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal1_desac.png);\n" "")
                 self.ui.label7.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal2_activ.png);\n" "")
                 self.ui.label8.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal4_desac.png);\n" "")
                 self.ui.label9.setStyleSheet( "background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal3_desac.png);\n" "")
                 if self.iniciarsesion == True:
                     self.enviardatosdesesion()





       if self.posxy[0] < 870 and self.posxy[0] > 830 and self.posxy[1] < 670 and self.posxy[1] > 536 :
                 self.cabezalactivo = 3
                 self.ui.label6.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal1_desac.png);\n" "")
                 self.ui.label7.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal2_desac.png);\n" "")
                 self.ui.label8.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal4_activ.png);\n" "")
                 self.ui.label9.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal3_desac.png);\n" "")
                 if self.iniciarsesion == True:
                     self.enviardatosdesesion()





       if self.posxy[0] < 940 and self.posxy[0] > 900 and self.posxy[1] < 670 and self.posxy[1] > 536 :
                 self.cabezalactivo = 4
                 self.ui.label6.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal1_desac.png);\n" "")
                 self.ui.label7.setStyleSheet( "background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal2_desac.png);\n" "")
                 self.ui.label8.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal4_desac.png);\n" "")
                 self.ui.label9.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR/cabezal3_activ.png);\n" "")
                 if self.iniciarsesion == True:
                     self.enviardatosdesesion()



      #manejo de nivel de frio


       if self.posxy[0] < 360 and self.posxy[0] > 310 and self.posxy[1] < 330 and self.posxy[1] > 280 :

                 if self.contador==0:
                    self.ui.label13.setStyleSheet( "border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/hielo.jpg);\n"" border-radius: 10px;")
                    self.frio=3
                    self.ui.label_2.hide()
                 if self.contador==1:
                    self.ui.label14.setStyleSheet("border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/hielo.jpg);\n"" border-radius: 10px;")
                    self.frio=2
                 if self.contador==2:
                    self.ui.label15.setStyleSheet("border-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/hielo.jpg);\n"" border-radius: 10px;")
                    self.frio=1
                 self.contador= 1+self.contador
                 if self.contador>3:
                     self.contador=3

                 #print(self.frio)
       if self.posxy[0] < 360 and self.posxy[0] > 310 and self.posxy[1] < 380 and self.posxy[1] > 340 :
                 if self.contador==3:
                    self.ui.label15.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/fondoreloj.png);")
                    self.frio=2
                 if self.contador == 2:
                    self.ui.label14.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/fondoreloj.png);")
                    self.frio=3
                 if self.contador == 1:
                    self.ui.label13.setStyleSheet("background-image: url(:/prefijoNuevo/PycharmProjects/Proyecto display CR v1.1/fondoreloj.png);")
                    self.frio = 0


                 self.contador= self.contador-1
                 if self.contador == 0:
                     self.ui.label_2.show()
                 if self.contador<0:
                     self.contador=0


       if self.iniciarsesion == True:
           self.enviardatosdesesion()

       #manejo de seteo tiempo de sesion

       if self.posxy[0] < 360 and self.posxy[0] > 310 and self.posxy[1] < 450 and self.posxy[1] > 400 and self.seteosesion==True :
           self.incrementarreloj()



       if self.posxy[0] < 360 and self.posxy[0] > 310 and self.posxy[1] < 500 and self.posxy[1] > 460 and self.seteosesion==True :
          self.decrementarreloj()





       #funcion para arrancar sesion

       if self.posxy[0] < 770 and self.posxy[0] > 430 and self.posxy[1] < 760 and self.posxy[1] > 670  :
           self.comenzarsesion()


       #funcion para detener sesion

       if self.posxy[0] < 1000 and self.posxy[0] > 800 and self.posxy[1] < 760 and self.posxy[1] > 670 and self.pausarsesion == 0 and self.pause == False:
           self.pausarsesion = 0
           self.detenersesion()

           if self.auxiliar==0 and self.iniciarsesion ==True:
                self.ui.cartel.raise_()
                self.ui.confirmar.raise_()
                self.ui.cancelar.raise_()
                self.ui.textocartel.raise_()
                self.ui.cartel.show()
                self.ui.confirmar.show()
                self.ui.cancelar.show()
                self.ui.textocartel.show()


       # funcion para pausar la sesion

       if self.posxy[0] < 410 and self.posxy[0] > 170 and self.posxy[1] < 760 and self.posxy[1] > 670  and self.pausarsesion == 0:

           self.pausarsesion=1
           self.detenersesion()
           if self.auxiliar == 0 and self.iniciarsesion == True:
               self.ui.cartel.raise_()
               self.ui.confirmar.raise_()
               self.ui.cancelar.raise_()
               self.ui.textocartel.raise_()
               self.ui.cartel.show()
               self.ui.confirmar.show()
               self.ui.cancelar.show()
               self.ui.textocartel.show()



       self.bloquearpag=False
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
       #funcion intermedia para confirmar detencion de sesion

   def confirmardetener(self):
       self.auxiliar=1
       self.detenersesion()

   def cancelardetener(self):
       self.auxiliar=1
       self.comenzarsesion()










   def resolverfrec(self):
       self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
       if self.sumafrec == 10 or self.sumafrec == 11 or self.sumafrec == 9:
           self.v2 = 4
           self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
           self.reproducir2_gif()


       if self.sumafrec == 5 or self.sumafrec == 13 or self.sumafrec == 9:
           self.v3 = 2

           self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
           self.reproducir3_gif()
       if self.iniciarsesion == True:
           self.enviardatosdesesion()


   def comenzarsesion(self):
       self.pause = False
       self.pausarsesion=0

       self.iniciarsesion = True
       self.reproducirgifreloj()
       self.seteosesion = False
       self.enviardatosdesesion()
       if self.auxiliar == 1:
           self.ui.cartel.hide()
           self.ui.confirmar.hide()
           self.ui.cancelar.hide()
           self.ui.textocartel.hide()
       self.auxiliar = 0





   def enviardatosdesesion(self):
     if self.pausarsesion==0:
       self.seteosesion = False
       packet1 = bytearray()
       packet1.append(9)
       packet1.append(self.valorpotencia)
       packet1.append(self.sumafrec)
       packet1.append(self.cabezalactivo)
       packet1.append(self.frio)
       puertoserie.write(packet1)
       #print(self.sumafrec)
       #print(self.valorpotencia)
       #print(self.cabezalactivo)
       #print(self.contador)


   def detenersesion(self):

       if self.auxiliar==1:
          if self.pausarsesion==0:
             self.resetearreloj()
          self.seteosesion = True
          self.iniciarsesion=False
          self.ui.cartel.hide()
          self.ui.confirmar.hide()
          self.ui.cancelar.hide()
          self.ui.textocartel.hide()
          self.parargifreloj()
          if self.pausarsesion == 1:
              self.pause = True
              self.iniciarsesion = True
       packet2 = bytearray()
       packet2.append(11)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       puertoserie.write(packet2)


   def incrementarreloj(self):
       self.aux1 = self.aux1 + 1
       if self.aux1 > 20:
           self.aux1 = 20
       self.minute = str(self.aux1)
       if self.aux1 < 10:
           self.ui.label17.setText('0' + self.minute + ':' + self.second)

       else:
           self.ui.label17.setText(self.minute + ':' + self.second)
       self.minuto = self.aux1





   def decrementarreloj(self):
       self.aux1 = self.aux1 - 1
       if self.aux1 < 0:
           self.aux1 = 0
       self.minute = str(self.aux1)

       if self.aux1 < 10:
           self.ui.label17.setText('0' + self.minute + ':' + self.second)

       else:
           self.ui.label17.setText(self.minute + ':' + self.second)
       self.minuto = self.aux1


   def resetearreloj(self):
           self.iniciarsesion = False
           self.segundo=60
           self.minutosesion='00'
           self.segundosesion='00'
           self.minuto=self.aux1


           text = self.minutosesion + ':' + self.segundosesion

           self.ui.label16.setText(text)

   # la siguiente funcion se ejecuta cada vez que se detecta que se solto el boton del mouse, o el dedo de la pantalla
   #def mouseReleaseEvent(self, event):





   # para los videos de las frecuencias

   def parar_gif_f1(self):
       self.movie1.stop()

   def parar_gif_f2(self):
       self.movie2.stop()

   def parar_gif_f3(self):
       self.movie3.stop()

   def parar_gif_f4(self):
       self.movie4.stop()

   def parar_gif_reloj(self):
       self.movie5.stop()

   #reproduce los videos de las frecuencias

   def reproducir1_gif(self):
       self.timerf1.start(1000)
       if self.v5 == 0:
           self.movie1 = QMovie("encendido10.gif")
       if self.v5 == 1 and self.sumafrec!=8:
           self.movie1 = QMovie("apagado10.gif")
           self.v1 = 0
       self.ui.label.setMovie(self.movie1)
       self.movie1.start()
       self.v5 = not self.v5

   def reproducir2_gif(self):
       self.timerf2.start(1000)
       if self.v6 == 0:
           self.movie2 = QMovie("encendido10.gif")
       if self.v6 == 1 and self.sumafrec!=4:
           self.movie2 = QMovie("apagado10.gif")
           self.v2 = 0
       self.ui.label2.setMovie(self.movie2)
       self.movie2.start()
       self.v6 = not self.v6

   def reproducir3_gif(self):
       self.timerf3.start(1000)
       if self.v7 == 0:
           self.movie3 = QMovie("encendido10.gif")
       if self.v7 == 1 and self.sumafrec!=2:
           self.movie3 = QMovie("apagado10.gif")
           self.v3 = 0
       self.ui.label3.setMovie(self.movie3)
       self.movie3.start()
       self.v7 = not self.v7

   def reproducir4_gif(self):
       self.timerf4.start(1000)
       if self.v8 == 0:
           self.movie4 = QMovie("encendido10.gif")
       if self.v8 == 1 and self.sumafrec!=1:
           self.movie4 = QMovie("apagado10.gif")
           self.v4 = 0
       self.ui.label4.setMovie(self.movie4)
       self.movie4.start()
       self.v8 = not self.v8

#reproduce el video del reloj animado
   def reproducirgifreloj(self):
       self.movie5 = QMovie("relojanimado3.gif")
       self.ui.label12.setMovie(self.movie5)
       self.movie5.start()

#para la animacion del reloj

   # reproduce el video del reloj animado
   def parargifreloj(self):

       self.movie5.stop()

   def reproducirgifpresentacion(self):
       self.movie6 = QMovie("videopresentacion.gif")

       self.ui.label23.setMovie(self.movie6)
       self.movie6.start()



if __name__ == "__main__":
     app = QApplication(sys.argv)
     w = MyForm()
     w.show()
     sys.exit(app.exec_())