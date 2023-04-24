from datetime import datetime
from wifi import Cell
from script_actualizacion import miwidget
#import board
#import digitalio
#from pyqtgraph import PlotWidget, plot
#import pyqtgraph as pg
import sqlite3 as sql
import webbrowser
import socket
import subprocess
import RPi.GPIO as gpio
#import urllib.request
import pickle
import os
import sys
import serial
from time import sleep
#from PyQt5.QtGui import QMovie
#from PyQt5.QtGui import QPainter, QPen
#from PyQt5.QtCore import Qt
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget, QTableWidgetItem,QListWidgetItem, QInputDialog,QListWidget,QMessageBox,QTableWidget
from PyQt5.QtCore import QTimer, QTime, Qt,QPropertyAnimation,QSize,QEasingCurve,QParallelAnimationGroup,QSequentialAnimationGroup,pyqtProperty
import time


puertoserie = serial.Serial(
 port="/dev/ttyS0",
    #"devttyS0"
#"devttyUSB0"
    #devttyS0
 baudrate= 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1

)

from vr_gui3 import *



class tratamientos(object):
    def __init__(self, niveldepotencia, frecuenciasseleccionada, niveldefrio, cabezalseleccionado, tiempo,pemf,laser,vacio,pp,niveldevacio,pv):
       self.niveldepotencia=niveldepotencia
       self.frecuenciaseleccionada=frecuenciasseleccionada
       self.niveldefrio=niveldefrio
       self.cabezalseleccionado=cabezalseleccionado
       self.tiempo=tiempo
       self.pemf=pemf
       self.laser=laser
       self.vacio=vacio
       self.pp=pp
       self.niveldevacio=niveldevacio
       self.pv=pv




class MyForm(QDialog):
   def __init__(self):
       super().__init__()
       self.setWindowFlags(Qt.FramelessWindowHint)
       self.setMouseTracking(True)
       self.setCursor(Qt.BlankCursor)
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
       self.mostrarredesinicio()
       gpio.setwarnings(False)
       gpio.setmode(gpio.BCM)
       gpio.setup(17, gpio.OUT)
       #self.mostrarredeswifi()
       #self.buzzer2()
       #self.x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
       #self.y = [2,4,3,5,9,1,4,4,4,5,4,3,5,9,1,4,4,4,5,4]  # 100 data points
       #self.ui.PlotWidget.setBackground((70,70,70))
       ## setting horizontal range
       #self.ui.PlotWidget.setYRange(10, 60,padding=0)
       # setting vertical range
       #self.ui.PlotWidget.hideAxis('bottom')
       #self.ui.PlotWidget.hideAxis('left')
       #pen = pg.mkPen(color=(0, 255, 0),width=3)
       #self.data_line = self.ui.PlotWidget.plot(self.x, self.y, pen=pen)
       self.ui.selecciondetratrapidobloqueo.hide()
       #self.ui.temperatura.hide()
       self.versionactual = "1_6"
       self.ui.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
       self.ui.texto_iniciorapidoencabezado_2.hide()
       self.sehabilitoperfil=0
       self.posxy0 = [0, 0]
       self.vecespulsadas=0
       self.posxy1 = [0, 0]
       self.ui.pulsiguiente.setEnabled(False)
       self.ui.pulsatras.setEnabled(False)
       self.posxy2=[0,0]
       self.codigonumerico=""
       self.cursor_buzzer = 0
       self.pagina_actual=1
       self.pagina_anterior=0
       self.paginastotales=0
       #self.ui.pushButton_13.setEnabled(False)
       #self.ui.pushButton_13.hide()
       self.variableauxiliar=0
       self.vecespulsadasflag = False
       self.continuar=False
       self.cabezalelegido=""
       self.cabezalbipolarseguridad=False
       self.versionactualsoft=""
       self.deshabilitar_buzzer_perfil=0
       self.vecespulsadasfinalizar=0
       self.ui.cartelzona2.hide()
       self.ui.cartelaceptar2.hide()
       self.ui.cartelcancelar2.hide()
       self.ui.ustehaseleccionado2.hide()
       self.ui.cartelconfirmarhombre.hide()
       self.cambiominuscula=0
       self.infoadicional=0
       self.counter=0
       #desactivacion de pulsadores de laser
       self.ui.pushButtonmanual.setEnabled(False)
       self.ui.pushButtonmanual.hide()
       self.ui.texto_ayuda.hide()
       #################################
       self.flag=0
       self.posxy3 = [0, 0]
       self.posxy4 = [0, 0]
       self.posxy5 = [0, 0]
       self.posxy6 = [0, 0]
       self.posxy7 = [0, 0]
       self.posxy8 = [0, 0]
       self.posxy9 = [0, 0]
       self.posxy10 = [0, 0]
       self.posxy11 = [0, 0]
       self.posxy12 = [0, 0]
       self.posxy13 = [0, 0]
       self.posxy14 = [0, 0]
       self.posxy15 = [0, 0]
       self.posxy16 = [0, 0]
       self.posxy17 = [0, 0]
       #self.verificarversion()

       self.id=0
       self.nombredered=""
       self.contrasena=""
       self.versionnuevasoft=""
       self.activarradio=0
       self.k=0
       self.nombre="casual"
       self.pausarsesion=0
       self.niveldefrioelegido=""
       self.niveldepotencia = 0
       self.frecuenciaseleccionada = 0
       self.niveldefrio = 0
       self.cabezalseleccionado = 0
       self.programavacio=1
       self.contadorvacio=1
       self.programalaser = 1
       self.contadorlaser = 1
       self.programapemf = 1
       self.contadorpemf = 1
       self.activarvacio=0
       self.habilitarlaser=0
       self.habilitarpemf=0
       self.animarpulsadorseleccion=0
       self.tiempo = 0
       self.contador=0
       self.flag=0
       self.guardarperfilnombre = 0
       self.infoadicionalflag = 0
       self.v1 = 0
       self.v2 = 0
       self.v3 = 0
       self.v4 = 0
       self.v5 = 0
       self.v6 = 0
       self.v7 = 0
       self.v8 = 0
       self.activarconfig=0
       self.activarperfil=0
       self.frecuenciaelegida=""
       self.tratamientoelegido=""
       self.prioridadenviodatossesion = 0
       self.eleccion=""
       self.numpagina=1
       self.inhibirresolverfrec = 0
       self.wifiactivado = False

       self.bitshift=0
       self.tratamiento = ""
       self.sumafrec=8
       self.potencia=0
       self.segundo=60
       self.minute = '10'
       self.minuto=10
       self.second = '00'
       self.ui.label_16.setGeometry(QtCore.QRect(690, 305, 81, 31))
       self.ui.label_17.setGeometry(QtCore.QRect(695, 345, 76, 21))
       #self.ui.texto_iniciar.setText('<font color="black">iniciar<font>')
       #self.ui.texto_iniciar.setGeometry(QtCore.QRect(890, 729, 96, 41))
       #self.ui.texto_finalizar.setText('<font color="grey">finalizar<font>')
       #self.ui.texto_finalizar.setGeometry(QtCore.QRect(1131, 730, 146, 41))
       #self.ui.label_24.setStyleSheet("background-image: url(Icono Finalizar instancia.png);")
       self.contadorniveldefrio=0
       self.minutosesion='10'
       self.segundosesion='00'
       self.aux1=10
       self.valorpotencia=0
       self.potencia=0
       self.iniciarsesion = False
       self.pause=False
       self.cambiarsexo = 0
       self.varx=0
       self.bloqueozona=0
       self.text=""
       self.cabezalactivo=0
       self.frio=0
       self.genero=""
       self.estado=bytearray(5)
       self.setMouseTracking(True)
       self.seteosesion = True
       self.ui.tecladoencabezado.hide()
       self.auxiliar = 0
       self.bloquear_animaciones = 0
       self.ui.lineEditpass_2.setEchoMode(QtWidgets.QLineEdit.Normal)

       self.ui.lineEditpass_2.setText("                                   ")
       self.flagzonatratamientosmujer = 0
       self.flagzonatratamientoshombre = 0
       self.timerest1 = QtCore.QTimer(self)
       self.timerest1.timeout.connect(self.leerestado)
       self.timerest2 = QtCore.QTimer(self)
       self.timerest2.timeout.connect(self.pedirestado)
       self.timer = QtCore.QTimer(self)
       self.timer.timeout.connect(self.iniciartimersesion)
       self.timer.start(1000)
       self.inicializar()
       self.ui.pushButtonmanual.released.connect(self.mostrarmanual)

       self.ui.confirmar.clicked.connect(lambda: self.animarlabel4(self.ui.confirmar,20,24,1))
       #self.ui.confirmar.clicked.connect(self.cancelardetener)
       self.ui.cancelar.clicked.connect(lambda: self.animarlabel4(self.ui.cancelar, 20, 23, 2))
       self.ui.cancelar_2.clicked.connect(lambda: self.animarlabel4(self.ui.cancelar_2, 20, 24, 3))
       #self.ui.cancelar.clicked.connect(self.confirmardetener)
       #self.ui.cancelar_2.clicked.connect(self.confirmardetener2)
       self.ui.pushButtonverificar.clicked.connect(lambda: self.animarpulsadorestransicion(self.ui.pushButtonverificar, 1043, 314,1038,309, 220, 56,4))
       #self.ui.pushButtonverificar.clicked.connect(self.actualizarredes)
       #self.ui.pushButtonverificar.clicked.connect(self.buzzer)
       self.contadortratamiento=1
       self.timerwifi = QtCore.QTimer(self)
       self.timerwifi.timeout.connect(self.conectarwifi)
       self.timerwifi2 = QtCore.QTimer(self)
       self.timerwifi2.timeout.connect(self.mostrarredeswifi)
       self.ui.pushButtonagregar.clicked.connect(lambda: self.animarpulsadores(self.ui.pushButtonagregar, 285, 654,280,649,221, 57))
       self.ui.pushButtonagregar.clicked.connect(self.adddatosperfil)

       self.ui.listWidget.itemClicked.connect(self.habilitarpulsador)
       # self.ui.pushButtoneliminar.clicked.connect(self.delitem)  # obs: python me deja que al pulsar, se llame a dos funciones.
       self.ui.pushButtoncrear.clicked.connect(lambda: self.animarpulsadores(self.ui.pushButtoncrear, 285, 218, 280, 213, 221, 57))
       self.ui.pushButtoncrear.clicked.connect(self.habilitarentradadedatos)


       self.ui.pushButtoncrear.clicked.connect(self.buzzer)
       self.ui.pushButtoneliminar.clicked.connect(lambda: self.animarpulsadores(self.ui.pushButtoneliminar, 285, 520,280,515, 221, 57))
       self.ui.pushButtoneliminar.clicked.connect(self.eliminarperfil)
       self.ui.pushButtonseleccionar.clicked.connect(self.seleccionarnombreperfil)
       self.ui.deseleccionarperfil.clicked.connect(self.deseleccionarnombreperfil)
       self.ui.deseleccionarperfil.clicked.connect(lambda: self.animarpulsadores(self.ui.deseleccionarperfil, 285, 370,280,365, 221, 57))
       #self.ui.pushButtonseleccionar.clicked.connect(self.iraselecciondesexo)



       self.ui.label_11.setStyleSheet("background-image: url(lipolisis laser.png);")
       self.ui.pushButtoninfo.clicked.connect(lambda: self.animarpulsadorestransicion(self.ui.pushButtoninfo,285, 445,280,440, 221, 57,2))
       #self.ui.pushButtoninfo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(10))
       self.vectordeperfiles = ["", "", "", "", ""]
       self.indicefichero = 0
       self.indice1 = 0
       self.vectordeperfiles2 = ["", "", "", "", ""]
       self.nombreperfil = ""
       self.correo=""
       self.direccion=""
       self.dni=""
       self.apellidoperfil = ""
       self.textolistaperfil = ""
       self.indice3 = 0
       self.cartelsecundario=0
       self.i = 0
       self.l=0
       self.posicionombre = 0
       self.indice2 = 0
       self.ui.deseleccionarperfil.setEnabled(False)
       self.ui.pushButtonagregar.setEnabled(False)
       self.ui.pushButtoneliminar.setEnabled(False)
       self.ui.pushButtonseleccionar.setEnabled(False)
       self.bloqueopaginas=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       self.bloqueodepaginas(self.numpagina)
       #self.ui.tableWidget.verticalScrollBar().setStyleSheet(
          # "QScrollBar:vertical {width: 25px; background-color: #000000; border-radius: 10px;}")
       self.ui.pantalla1b.setText('<font color="white">presione la pantalla para continuar<font>')
       self.ui.cartelaceptar.setText('<font color="#197BFC">CONTINUAR<font>')
       self.ui.cartelcancelar.setText('<font color="#197BFC">CANCELAR<font>')
       self.ui.cartelaceptar2.setText('<font color="#197BFC">CONTINUAR<font>')
       self.ui.cartelcancelar2.setText('<font color="#197BFC">CANCELAR<font>')
       self.ui.ustedhaseleccionado.setText('<font color="#949899">¿desea continuar?<font>')
       self.ui.ustehaseleccionado2.setText('<font color="#949899">¿desea continuar?<font>')

       self.habilitarcontrol = False
       self.j = 0
       self.h = 0
       self.bloqueofrecuencias=0
       self.f = 0
       self.usuario=""
       self.laser="desactivado"
       self.vacio="desactivado"
       self.pemf="desactivado"
       self.bloqueoporcarteliniciorapido=1
       self.flag=0
       self.deshabilitar_buzzer=0
       self.ui.pushButtoninfo.setEnabled(False)
       self.itemseleccionado=""
       self.ui.listWidget_2.itemSelectionChanged.connect(self.adquirirusuario)
       self.ui.lineEditpass_2.setText("pulse y escriba para modificar")
       self.timerpulsador = QTimer(self)
       self.timerpulsador.timeout.connect(self.on_timer_timeout)
       # creacion de objetos de clase tratamiento:
       #niveldepotencia, frecuenciasseleccionada, niveldefrio, cabezalseleccionado, tiempo,pemf,laser,vacio,pp,pl,pv

       #zona rostro#
       self.zonaorbicular=tratamientos(0, 8, 0, 3, 16,0,0,0,4,1,3)
       self.flacidezsuprostro = tratamientos(0, 12, 0, 4, 16,0,0,0,4,1,3)    # p,f,frio,cab,tiempo
       self.flacidezprofrostro = tratamientos(0, 4, 0, 4, 16,0,0,0,4,1,3)

       #zona gluteos#
       self.flacidezsupgluteos=tratamientos(0, 12, 2, 1, 16,1,1,1,4,2,2)
       self.flacidezprofgluteos = tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.estriasgluteos = tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.celyflacgluteos = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.celulitisgluteos = tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.adipycelgluteos = tratamientos(0, 3, 3, 1, 16,1,1,1,4,2,3)
       self.adiplevegluteos = tratamientos(0, 6, 3, 1, 16,1,1,1,4,2,3)
       self.adipmodgluteos = tratamientos(0, 3, 3, 1, 16,1,1,1,4,2,3)

       #zona muslos anteriores#
       self.muslosantflacidezsup=tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.muslosantflacidezprof=tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.muslosantestrias = tratamientos(0, 12, 0, 1, 16,1,1,1,3,4,3)
       self.muslosantcelyflac = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.muslosantcelulitis = tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.muslosantadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.muslosantadiposidad = tratamientos(0, 1, 3, 1, 16,0,0,0,0,0,0)
       self.adiplevemuslosant = tratamientos(0, 6, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodmuslosant =tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       #abdomen
       self.abdomenflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.abdomenflacidezprof = tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.abdomenestrias =  tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.abdomencelyflac = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.abdomencelulitis = tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.abdomenadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.abdomenadiposidad = tratamientos(0, 1, 3, 1, 12,0,0,0,0,0,0)
       self.adipleveabdomen =tratamientos(0, 6, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodabdomen = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       # flancos
       self.flancosflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.flancosflacidezprof = tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.flancosestrias =  tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.flancoscelyflac =tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.flancoscelulitis =tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.flancosadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.flancosadiposidad = tratamientos(0, 1, 3, 1, 16,0,0,0,0,0,0)
       self.adipleveflancos = tratamientos(0, 6, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodflancos = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       #trocanteriana
       self.trocanflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.trocanflacidezprof =tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.trocanestrias = tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.trocancelyflac = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.trocancelulitis = tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.trocanadipycel =tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.trocanadiposidad = tratamientos(0, 1, 3, 1, 16,0,0,0,0,0,0)
       self.adiplevetrocan = tratamientos(0, 6, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodtrocan = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       #muslos internos
       self.muslosintflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.muslosintflacidezprof = tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.muslosintestrias = tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.muslosintcelyflac =  tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.muslosintcelulitis =tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.muslosintadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.muslosintadiposidad = tratamientos(0, 1, 3, 1, 16,0,0,0,0,0,0)
       self.adiplevemuslosint =tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodmuslosint = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       #brazoant y pos
       self.brazosflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.brazosflacidezprof =tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.brazosestrias =  tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.brazoscelyflac = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.brazoscelulitis = tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.brazosadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.brazosadiposidad = tratamientos(0, 1, 3, 1, 10,0,0,0,0,0,0)
       self.adiplevebrazos =tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodbrazos = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       #subescapular
       self.escapularflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.escapularflacidezprof =tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.escapularestrias =  tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.escapularcelyflac = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.escapularcelulitis =  tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.escapularadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.escapularadiposidad = tratamientos(0, 1, 3, 1, 12,0,0,0,0,0,0)
       self.adipleveescapular =tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodescapular = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)

       #cuello
       self.cuelloflacidezsup = tratamientos(0, 12, 2, 1, 10,1,1,1,4,1,2)
       self.cuelloflacidezprof = tratamientos(0, 7, 2, 1, 10,1,1,1,4,1,3)
       #escote
       self.escoteflacidezsup = tratamientos(0, 12, 2, 1, 8,1,1,1,4,1,2)
       self.escoteflacidezprof = tratamientos(0, 7, 2, 1, 8,1,1,1,4,1,3)

       #muslospos
       self.muslosposflacidezsup = tratamientos(0, 12, 2, 1, 16,1,1,1,4,1,2)
       self.muslosposflacidezprof = tratamientos(0, 7, 2, 1, 16,1,1,1,4,1,3)
       self.muslosposestrias = tratamientos(0, 12, 0, 1, 16,1,1,1,4,1,3)
       self.muslosposcelyflac = tratamientos(0, 15, 2, 1, 16,1,1,1,4,1,3)
       self.muslosposcelulitis = tratamientos(0, 7, 3, 1, 16,1,1,1,4,1,3)
       self.muslosposadipycel = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       #self.muslosposadiposidad = tratamientos(0, 1, 3, 1, 16,0,0,0,0,0,0)
       self.adiplevemuslospos = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)
       self.adipmodmuslospos = tratamientos(0, 3, 3, 1, 16,1,1,1,4,1,3)




       self.ui.pulsbajapotencia.pressed.connect(self.bajarpotencia)
       self.ui.pulsbajapotencia.released.connect(self.instanciabaja)
       self.ui.pulssubepotencia.pressed.connect(self.subirpotencia)
       self.ui.pulssubepotencia.released.connect(self.instanciasube)


       self.ui.pulsbajatiempo.pressed.connect(self.decrementarreloj)
       self.ui.pulsbajatiempo.released.connect(self.instanciabajatiempo)
       self.ui.pulssubetiempo.pressed.connect(self.incrementarreloj)
       self.ui.pulssubetiempo.released.connect(self.instanciasubetiempo)

       self.ui.pulssubetratamiento.released.connect(self.instanciasubetrat)
       self.ui.pulsbajatratamiento.released.connect(self.instanciabajatrat)
       self.ui.pulssubetratamiento.pressed.connect(self.subetratamiento)
       self.ui.pulsbajatratamiento.pressed.connect(self.bajatratamiento)
       self.habilitar5=0
       self.habilitar6=0


       #variables para el uso del teclado
       self.dato = ""
       self.texto1 = ""
       self.texto2 = ""
       self.texto3 = ""
       self.texto4 = ""
       self.habilitar1 = 0
       self.habilitar2 = 0
       self.habilitar3 = 0
       self.habilitar4 = 0
       self.datos1 = ""
       self.datos2 = ""
       self.datos3 = ""
       self.datos4 = ""
       self.datos5 = ""
       self.datos6 = ""
       self.bloqueoregresopagina = 0



       #self.ui.tableWidget.setHorizontalHeaderLabels(["nombre", "genero", "zona", "tratamiento", "potencia", "frecuencia", "cabezal", "nivel de vacio","laser","PEMF", "duración","fecha de sesión"])

       self.ui.lineEditpass_2.cursorPositionChanged.connect(self.habilitarentradadedatosintermedio2)
       self.ui.lineEditnombre.cursorPositionChanged.connect(self.habilitar_linea1)
       self.ui.lineEditdni.cursorPositionChanged.connect(self.habilitar_linea2)
       self.ui.lineEditdireccion.cursorPositionChanged.connect(self.habilitar_linea3)
       self.ui.lineEditcorreo.cursorPositionChanged.connect(self.habilitar_linea4)




       #self.ui.lineEditnombre.textChanged.connect(lambda: print("text changed"))

       self.ui.letraq_2.pressed.connect(lambda: self.letraQ(self.ui.letraq_2))
       self.ui.letraq_2.released.connect(lambda: self.instanciateclas(self.ui.letraq_2))

       self.ui.letraw_2.pressed.connect(lambda: self.letraW(self.ui.letraw_2))
       self.ui.letraw_2.released.connect(lambda: self.instanciateclas(self.ui.letraw_2))

       self.ui.letrae_2.pressed.connect(lambda: self.letraE(self.ui.letrae_2))
       self.ui.letrae_2.released.connect(lambda: self.instanciateclas(self.ui.letrae_2))

       self.ui.letrar_2.pressed.connect(lambda: self.letraR(self.ui.letrar_2))
       self.ui.letrar_2.released.connect(lambda: self.instanciateclas(self.ui.letrar_2))


       self.ui.letrat_2.pressed.connect(lambda: self.letraT(self.ui.letrat_2))
       self.ui.letrat_2.released.connect(lambda: self.instanciateclas(self.ui.letrat_2))



       self.ui.letray_2.pressed.connect(lambda: self.letraY(self.ui.letray_2))
       self.ui.letray_2.released.connect(lambda: self.instanciateclas(self.ui.letray_2))

       self.ui.letrau_2.pressed.connect(lambda: self.letraU(self.ui.letrau_2))
       self.ui.letrau_2.released.connect(lambda: self.instanciateclas(self.ui.letrau_2))


       self.ui.letrai_2.pressed.connect(lambda: self.letraI(self.ui.letrai_2))
       self.ui.letrai_2.released.connect(lambda: self.instanciateclas(self.ui.letrai_2))


       self.ui.letrao_2.pressed.connect(lambda: self.letraO(self.ui.letrao_2))
       self.ui.letrao_2.released.connect(lambda: self.instanciateclas(self.ui.letrao_2))


       self.ui.letrap_2.pressed.connect(lambda: self.letraP(self.ui.letrap_2))
       self.ui.letrap_2.released.connect(lambda: self.instanciateclas(self.ui.letrap_2))

       self.ui.letraa_2.pressed.connect(lambda: self.letraA(self.ui.letraa_2))
       self.ui.letraa_2.released.connect(lambda: self.instanciateclas(self.ui.letraa_2))


       self.ui.letras_2.pressed.connect(lambda: self.letraS(self.ui.letras_2))
       self.ui.letras_2.released.connect(lambda: self.instanciateclas(self.ui.letras_2))


       self.ui.letrad_2.pressed.connect(lambda: self.letraD(self.ui.letrad_2))
       self.ui.letrad_2.released.connect(lambda: self.instanciateclas(self.ui.letrad_2))


       self.ui.letraf_2.pressed.connect(lambda: self.letraF(self.ui.letraf_2))
       self.ui.letraf_2.released.connect(lambda: self.instanciateclas(self.ui.letraf_2))


       self.ui.letrag_2.pressed.connect(lambda: self.letraG(self.ui.letrag_2))
       self.ui.letrag_2.released.connect(lambda: self.instanciateclas(self.ui.letrag_2))


       self.ui.letrah_2.pressed.connect(lambda: self.letraH(self.ui.letrah_2))
       self.ui.letrah_2.released.connect(lambda: self.instanciateclas(self.ui.letrah_2))


       self.ui.letraj_2.pressed.connect(lambda: self.letraJ(self.ui.letraj_2))
       self.ui.letraj_2.released.connect(lambda: self.instanciateclas(self.ui.letraj_2))


       self.ui.letrak_2.pressed.connect(lambda: self.letraK(self.ui.letrak_2))
       self.ui.letrak_2.released.connect(lambda: self.instanciateclas(self.ui.letrak_2))


       self.ui.letral_2.pressed.connect(lambda: self.letraL(self.ui.letral_2))
       self.ui.letral_2.released.connect(lambda: self.instanciateclas(self.ui.letral_2))

       self.ui.letraz_2.pressed.connect(lambda: self.letraZ(self.ui.letraz_2))
       self.ui.letraz_2.released.connect(lambda: self.instanciateclas(self.ui.letraz_2))


       self.ui.letrax_2.pressed.connect(lambda: self.letraX(self.ui.letrax_2))
       self.ui.letrax_2.released.connect(lambda: self.instanciateclas(self.ui.letrax_2))


       self.ui.letrac_2.pressed.connect(lambda: self.letraC(self.ui.letrac_2))
       self.ui.letrac_2.released.connect(lambda: self.instanciateclas(self.ui.letrac_2))


       self.ui.letrav_2.pressed.connect(lambda: self.letraV(self.ui.letrav_2))
       self.ui.letrav_2.released.connect(lambda: self.instanciateclas(self.ui.letrav_2))


       self.ui.letrab_2.pressed.connect(lambda: self.letraB(self.ui.letrab_2))
       self.ui.letrab_2.released.connect(lambda: self.instanciateclas(self.ui.letrab_2))


       self.ui.letran_2.pressed.connect(lambda: self.letraN(self.ui.letran_2))
       self.ui.letran_2.released.connect(lambda: self.instanciateclas(self.ui.letran_2))


       self.ui.letram_2.pressed.connect(lambda: self.letraM(self.ui.letram_2))
       self.ui.letram_2.released.connect(lambda: self.instanciateclas(self.ui.letram_2))

       self.ui.numero0_2.pressed.connect(lambda: self.num0(self.ui.numero0_2))
       self.ui.numero0_2.released.connect(lambda: self.instanciateclas(self.ui.numero0_2))

       self.ui.numero1_2.pressed.connect(lambda: self.num1(self.ui.numero1_2))
       self.ui.numero1_2.released.connect(lambda: self.instanciateclas(self.ui.numero1_2))

       self.ui.numero2_2.pressed.connect(lambda: self.num2(self.ui.numero2_2))
       self.ui.numero2_2.released.connect(lambda: self.instanciateclas(self.ui.numero2_2))

       self.ui.numero3_2.pressed.connect(lambda: self.num3(self.ui.numero3_2))
       self.ui.numero3_2.released.connect(lambda: self.instanciateclas(self.ui.numero3_2))

       self.ui.numero4_2.pressed.connect(lambda: self.num4(self.ui.numero4_2))
       self.ui.numero4_2.released.connect(lambda: self.instanciateclas(self.ui.numero4_2))

       self.ui.numero5_2.pressed.connect(lambda: self.num5(self.ui.numero5_2))
       self.ui.numero5_2.released.connect(lambda: self.instanciateclas(self.ui.numero5_2))

       self.ui.numero6_2.pressed.connect(lambda: self.num5(self.ui.numero6_2))
       self.ui.numero6_2.released.connect(lambda: self.instanciateclas(self.ui.numero6_2))

       self.ui.numero7_2.pressed.connect(lambda: self.num7(self.ui.numero7_2))
       self.ui.numero7_2.released.connect(lambda: self.instanciateclas(self.ui.numero7_2))

       self.ui.numero8_2.pressed.connect(lambda: self.num8(self.ui.numero8_2))
       self.ui.numero8_2.released.connect(lambda: self.instanciateclas(self.ui.numero8_2))

       self.ui.numero9_2.pressed.connect(lambda: self.num9(self.ui.numero9_2))
       self.ui.numero9_2.released.connect(lambda: self.instanciateclas(self.ui.numero9_2))

       self.ui.arroba_2.pressed.connect(lambda: self.arroba(self.ui.arroba_2))
       self.ui.arroba_2.released.connect(lambda: self.instanciateclas(self.ui.arroba_2))

       self.ui.teclamayus_2.pressed.connect(lambda: self.mayuscula(self.ui.teclamayus_2))
       self.ui.teclamayus_2.released.connect(lambda: self.instanciateclas(self.ui.teclamayus_2))

       self.ui.teclapunto_2.pressed.connect(lambda: self.punto(self.ui.teclapunto_2))
       self.ui.teclapunto_2.released.connect(lambda: self.instanciateclas(self.ui.teclapunto_2))

       self.ui.teclaborrar_2.pressed.connect(lambda: self.borrarentrada(self.ui.teclaborrar_2))
       self.ui.teclaborrar_2.released.connect(lambda: self.instanciateclas(self.ui.teclaborrar_2))

       self.ui.teclaespacio_2.pressed.connect(lambda: self.teclaespaciadora(self.ui.teclaespacio_2))
       self.ui.teclaespacio_2.released.connect(lambda: self.instanciateclas(self.ui.teclaespacio_2))

       self.ui.teclaescape_2.clicked.connect(self.escape2)


       self.ui.shift.pressed.connect(lambda: self.funcionshift1(self.ui.shift))
       self.ui.shift.released.connect(lambda: self.instanciateclas(self.ui.shift))

       self.ui.tecla_shift.pressed.connect(lambda: self.funcionshift2(self.ui.tecla_shift))
       self.ui.tecla_shift.released.connect(lambda: self.instanciateclas(self.ui.tecla_shift))


       self.ui.letraq.pressed.connect(lambda: self.letraQ(self.ui.letraq))
       self.ui.letraq.released.connect(lambda: self.instanciateclas(self.ui.letraq))

       self.ui.letraw.pressed.connect(lambda: self.letraW(self.ui.letraw))
       self.ui.letraw.released.connect(lambda: self.instanciateclas(self.ui.letraw))

       self.ui.letrae.pressed.connect(lambda: self.letraE(self.ui.letrae))
       self.ui.letrae.released.connect(lambda: self.instanciateclas(self.ui.letrae))

       self.ui.letrar.pressed.connect(lambda: self.letraR(self.ui.letrar))
       self.ui.letrar.released.connect(lambda: self.instanciateclas(self.ui.letrar))

       self.ui.letrat.pressed.connect(lambda: self.letraT(self.ui.letrat))
       self.ui.letrat.released.connect(lambda: self.instanciateclas(self.ui.letrat))

       self.ui.letray.pressed.connect(lambda: self.letraY(self.ui.letray))
       self.ui.letray.released.connect(lambda: self.instanciateclas(self.ui.letray))

       self.ui.letrau.pressed.connect(lambda: self.letraU(self.ui.letrau))
       self.ui.letrau.released.connect(lambda: self.instanciateclas(self.ui.letrau))

       self.ui.letrai.pressed.connect(lambda: self.letraI(self.ui.letrai))
       self.ui.letrai.released.connect(lambda: self.instanciateclas(self.ui.letrai))

       self.ui.letrao.pressed.connect(lambda: self.letraO(self.ui.letrao))
       self.ui.letrao.released.connect(lambda: self.instanciateclas(self.ui.letrao))

       self.ui.letrap.pressed.connect(lambda: self.letraP(self.ui.letrap))
       self.ui.letrap.released.connect(lambda: self.instanciateclas(self.ui.letrap))

       self.ui.letraa.pressed.connect(lambda: self.letraA(self.ui.letraa))
       self.ui.letraa.released.connect(lambda: self.instanciateclas(self.ui.letraa))

       self.ui.letras.pressed.connect(lambda: self.letraS(self.ui.letras))
       self.ui.letras.released.connect(lambda: self.instanciateclas(self.ui.letras))

       self.ui.letrad.pressed.connect(lambda: self.letraD(self.ui.letrad))
       self.ui.letrad.released.connect(lambda: self.instanciateclas(self.ui.letrad))

       self.ui.letraf.pressed.connect(lambda: self.letraF(self.ui.letraf))
       self.ui.letraf.released.connect(lambda: self.instanciateclas(self.ui.letraf))

       self.ui.letrag.pressed.connect(lambda: self.letraG(self.ui.letrag))
       self.ui.letrag.released.connect(lambda: self.instanciateclas(self.ui.letrag))

       self.ui.letrah.pressed.connect(lambda: self.letraH(self.ui.letrah))
       self.ui.letrah.released.connect(lambda: self.instanciateclas(self.ui.letrah))

       self.ui.letraj.pressed.connect(lambda: self.letraJ(self.ui.letraj))
       self.ui.letraj.released.connect(lambda: self.instanciateclas(self.ui.letraj))

       self.ui.letrak.pressed.connect(lambda: self.letraK(self.ui.letrak))
       self.ui.letrak.released.connect(lambda: self.instanciateclas(self.ui.letrak))

       self.ui.letral.pressed.connect(lambda: self.letraL(self.ui.letral))
       self.ui.letral.released.connect(lambda: self.instanciateclas(self.ui.letral))

       self.ui.letraz.pressed.connect(lambda: self.letraZ(self.ui.letraz))
       self.ui.letraz.released.connect(lambda: self.instanciateclas(self.ui.letraz))

       self.ui.letrax.pressed.connect(lambda: self.letraX(self.ui.letrax))
       self.ui.letrax.released.connect(lambda: self.instanciateclas(self.ui.letrax))

       self.ui.letrac.pressed.connect(lambda: self.letraC(self.ui.letrac))
       self.ui.letrac.released.connect(lambda: self.instanciateclas(self.ui.letrac))

       self.ui.letrav.pressed.connect(lambda: self.letraV(self.ui.letrav))
       self.ui.letrav.released.connect(lambda: self.instanciateclas(self.ui.letrav))

       self.ui.letrab.pressed.connect(lambda: self.letraB(self.ui.letrab))
       self.ui.letrab.released.connect(lambda: self.instanciateclas(self.ui.letrab))

       self.ui.letran.pressed.connect(lambda: self.letraN(self.ui.letran))
       self.ui.letran.released.connect(lambda: self.instanciateclas(self.ui.letran))

       self.ui.letram.pressed.connect(lambda: self.letraM(self.ui.letram))
       self.ui.letram.released.connect(lambda: self.instanciateclas(self.ui.letram))

       self.ui.numero0.pressed.connect(lambda: self.num0(self.ui.numero0))
       self.ui.numero0.released.connect(lambda: self.instanciateclas(self.ui.numero0))

       self.ui.numero1.pressed.connect(lambda: self.num1(self.ui.numero1))
       self.ui.numero1.released.connect(lambda: self.instanciateclas(self.ui.numero1))

       self.ui.numero2.pressed.connect(lambda: self.num2(self.ui.numero2))
       self.ui.numero2.released.connect(lambda: self.instanciateclas(self.ui.numero2))

       self.ui.numero3.pressed.connect(lambda: self.num3(self.ui.numero3))
       self.ui.numero3.released.connect(lambda: self.instanciateclas(self.ui.numero3))

       self.ui.numero4.pressed.connect(lambda: self.num4(self.ui.numero4))
       self.ui.numero4.released.connect(lambda: self.instanciateclas(self.ui.numero4))

       self.ui.numero5.pressed.connect(lambda: self.num5(self.ui.numero5))
       self.ui.numero5.released.connect(lambda: self.instanciateclas(self.ui.numero5))

       self.ui.numero6.pressed.connect(lambda: self.num6(self.ui.numero6))
       self.ui.numero6.released.connect(lambda: self.instanciateclas(self.ui.numero6))

       self.ui.numero7.pressed.connect(lambda: self.num7(self.ui.numero7))
       self.ui.numero7.released.connect(lambda: self.instanciateclas(self.ui.numero7))

       self.ui.numero8.pressed.connect(lambda: self.num8(self.ui.numero8))
       self.ui.numero8.released.connect(lambda: self.instanciateclas(self.ui.numero8))

       self.ui.numero9.pressed.connect(lambda: self.num9(self.ui.numero9))
       self.ui.numero9.released.connect(lambda: self.instanciateclas(self.ui.numero9))

       self.ui.arroba.pressed.connect(lambda: self.arroba(self.ui.arroba))
       self.ui.arroba.released.connect(lambda: self.instanciateclas(self.ui.arroba))

       self.ui.teclamayus.pressed.connect(lambda: self.mayuscula(self.ui.teclamayus))
       self.ui.teclamayus.released.connect(lambda: self.instanciateclas(self.ui.teclamayus))

       self.ui.teclapunto.pressed.connect(lambda: self.punto(self.ui.teclapunto))
       self.ui.teclapunto.released.connect(lambda: self.instanciateclas(self.ui.teclapunto))


       #self.ui.pushButton_13.pressed.connect(self.on_button_pressed)
       #self.ui.pushButton_13.released.connect(self.on_button_released)

       self.ui.tecla1.pressed.connect(lambda: self.num1(self.ui.tecla1))
       self.ui.tecla1.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla1))
       self.ui.tecla1.pressed.connect(lambda: self.numeroelegido(1))


       self.ui.tecla2.pressed.connect(lambda: self.num2(self.ui.tecla2))
       self.ui.tecla2.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla2))
       self.ui.tecla2.pressed.connect(lambda: self.numeroelegido(2))

       self.ui.tecla3.pressed.connect(lambda: self.num3(self.ui.tecla3))
       self.ui.tecla3.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla3))
       self.ui.tecla3.pressed.connect(lambda: self.numeroelegido(3))

       self.ui.tecla4.pressed.connect(lambda: self.num4(self.ui.tecla4))
       self.ui.tecla4.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla4))
       self.ui.tecla4.pressed.connect(lambda: self.numeroelegido(4))

       self.ui.tecla5.pressed.connect(lambda: self.num5(self.ui.tecla5))
       self.ui.tecla5.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla5))
       self.ui.tecla5.pressed.connect(lambda: self.numeroelegido(5))

       self.ui.tecla6.pressed.connect(lambda: self.num6(self.ui.tecla6))
       self.ui.tecla6.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla6))
       self.ui.tecla6.pressed.connect(lambda: self.numeroelegido(6))

       self.ui.tecla7.pressed.connect(lambda: self.num7(self.ui.tecla7))
       self.ui.tecla7.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla7))
       self.ui.tecla7.pressed.connect(lambda: self.numeroelegido(7))

       self.ui.tecla8.pressed.connect(lambda: self.num8(self.ui.tecla8))
       self.ui.tecla8.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla8))
       self.ui.tecla8.pressed.connect(lambda: self.numeroelegido(8))

       self.ui.tecla9.pressed.connect(lambda: self.num9(self.ui.tecla9))
       self.ui.tecla9.released.connect(lambda: self.instanciateclasnumerico(self.ui.tecla9))
       self.ui.tecla9.pressed.connect(lambda: self.numeroelegido(9))

       self.ui.teclaborrar.pressed.connect(lambda: self.borrarentrada(self.ui.teclaborrar))
       self.ui.teclaborrar.released.connect(lambda: self.instanciateclas(self.ui.teclaborrar))


       self.ui.teclaespacio.pressed.connect(lambda: self.teclaespaciadora(self.ui.teclaespacio))
       self.ui.teclaespacio.released.connect(lambda: self.instanciateclas(self.ui.teclaespacio))


       self.ui.teclaescape.clicked.connect(self.escape)


       self.ui.tableWidget.setEnabled(True)

       #self.ui.pushButtonconectar.setEnabled(False)
       #print("Current Time =", current_time)
       self.ui.pushButtonconectar.clicked.connect(lambda: self.animarpulsadorestransicion(self.ui.pushButtonconectar, 655, 314,650,309, 220, 56, 3))
       #self.ui.pushButtonconectar.clicked.connect(self.tomardatoswifi)
       #self.ui.pushButtonconectar.clicked.connect(self.conectarred)

       self.ui.pushButtoncancelar.clicked.connect(lambda: self.animarpulsadores(self.ui.pushButtoncancelar,655, 390,650,385, 220, 56))
       self.ui.pushButtoncancelar.clicked.connect(self.limpiarcampowifi)
       self.ui.pushButtonenablefrec.pressed.connect(self.activarradiofrecuencia)

       self.ui.pulsarribavacum.pressed.connect(self.subirvacio)
       self.ui.pulsabajovacum.pressed.connect(self.bajarvacio)

       self.ui.pushButtonvolver16.pressed.connect(lambda: self.instancia_volver_pagina(self.ui.encabezado_menu_actualizar))
       self.ui.pushButtonvolver16.released.connect(lambda: self.volver_a_pagina(15,self.ui.encabezado_menu_actualizar))

       self.ui.pushButtonvolver17.pressed.connect(lambda: self.instancia_volver_pagina(self.ui.encabezado_menu_historial))
       self.ui.pushButtonvolver17.released.connect(lambda: self.volver_a_pagina(15,self.ui.encabezado_menu_historial))

       self.ui.pulssubepemf.pressed.connect(lambda: self.subirpemf(self.formaonda))
       self.ui.pulsbajapemf.pressed.connect(lambda: self.bajarpemf(self.formaonda))

       self.ui.pushButtonenablevacio.pressed.connect(self.activarvacum)
       self.ui.pushButtonenablepemf.pressed.connect(self.activarpemf)
       self.ui.pushButtonenablelaser.pressed.connect(self.activarlaser)

       self.ui.pemftriangular.pressed.connect(self.settriangular)
       self.ui.pemfcuadrado.pressed.connect(self.setcuadrada)

       self.ui.vaciomedio.pressed.connect(self.setvaciomedio)
       self.ui.vacioalto.pressed.connect(self.setvacioalto)

       self.ui.pulsiguiente.clicked.connect(lambda: self.paginasiguiente(self.nombre))
       self.ui.pulsatras.clicked.connect(lambda: self.paginaatras(self.nombre))
       self.ui.pushButtonwifi.released.connect(self.pantallawifi)
       self.ui.pushButtonwifi.pressed.connect(self.instanciawifi)
       self.ui.pushButtonupdate.released.connect(self.verificarversion)
       self.ui.pushButtonupdate.pressed.connect(lambda: self.instancia_pulsadores(self.ui.pushButtonupdate))
       self.ui.pushButtonvolver_update.clicked.connect(lambda: self.animarpulsadorestransicion(self.ui.pushButtonvolver_update,370, 475,362,467, 220, 56,5))
       self.ui.pushButtonlimpiar.pressed.connect(lambda: self.instancia_pulsadores(self.ui.pushButtonlimpiar))
       self.ui.pushButtonlimpiar.released.connect(self.pantallaborrarhistorial)
       self.ui.pushButtonactualizar_confirmar.clicked.connect(self.actualizarsoft)
       self.ui.pushButtonconfirmarpass.pressed.connect(self.confirmarpassnumerico)
       self.ui.pushButtonconfirmarpass.released.connect(self.cambiarfondopass)
       self.timercab = QtCore.QTimer(self)
       self.ui.cartel.hide()
       self.ui.textocartel.hide()
       self.ui.textocartel.hide()
       self.ui.cancelar_2.hide()
       self.ui.cancelar.hide()
       self.ui.confirmar.hide()
       self.ui.cartelconfirmarmujer.hide()
       self.ui.cartelconfirmarzona.hide()
       self.ui.ustedhaseleccionado.hide()
       self.ui.cartelcancelar.hide()
       self.ui.cartelaceptar.hide()
       #.ui.graphicsView.hide()
       self.ui.f1desac.hide()
       self.ui.f1.raise_()
       self.ui.f2.raise_()
       self.ui.f3.raise_()
       self.ui.f4.raise_()
       self.ui.areatiempobloqueo.hide()
       self.ui.selecciondetratrapidobloqueo.hide()
       self.cargardatosenlista()
       self.cargardatosentabla()
       #self.mostrarredeswifi()

       self.show()
       self.buzzer2()


# BLOQUE INICIALIZACION Y CICLO DE CONSULTA DE ESTADO DEL SISTEMA


   def instanciateclas(self,tecla):
       sleep(0.1)
       tecla.setStyleSheet("background-image: url(trasnp.png);\n"
                                  "border-image: url(trasnp.png);")
       tecla.setStyleSheet("background-image: url(trasnp.png);\n"
                                     "border-image: url(trasnp.png);")

   def instanciateclasnumerico(self,tecla):
       sleep(0.1)
       tecla.setStyleSheet("background-image: url(Teclado tecla chica.png);\n"
                                 "border-image: url(trasnp.png);")


   def numeroelegido(self,numeroe):

       self.codigonumerico +=str(numeroe)
       self.ui.lineEditpass_limpiar.setText(self.codigonumerico)

   def confirmarpassnumerico(self):
       if self.ui.lineEditpass_limpiar.text() =="1983":
           self.codigonumerico=""
           self.ui.label_46.setStyleSheet("background-image: url(verde.png);")
           self.animarpulsadores(self.ui.pushButtonconfirmarpass, 705, 345, 697, 337, 220, 56)
           self.eliminar_historial2()

       else:
           self.ui.label_46.setStyleSheet("background-image: url(rojo.png);")
           self.animarpulsadores(self.ui.pushButtonconfirmarpass,705, 345, 697,337, 220, 56)

           self.ui.lineEditpass_limpiar.clear()
           self.codigonumerico=""

   def cambiarfondopass(self):
       self.ui.label_46.setStyleSheet("background-image: url(Seleccionar perfil nombre y apellido.png);")

   def pantallaborrarhistorial(self):
       self.ui.stackedWidget.setCurrentIndex(17)
       self.numpagina = 17
       self.bloqueodepaginas(self.numpagina)
       self.ui.pushButtonlimpiar.setStyleSheet("background-image: url(3 - Boton configuracion.png);\n"
                                            "border-image: url(trasnp.png);")




   def buzzer(self):
       #print("beep")
       gpio.output(17,True)
       #self.buzzers.value = True
       sleep(0.1)
       gpio.output(17,False)
       #self.buzzers.value = False
       #self.buzzers.value = False

   def buzzer2(self):
       #print("beep beep")
       gpio.output(17,True)
       #self.buzzers.value = True
       sleep(0.3)
       gpio.output(17,False)
       sleep(0.1)
       gpio.output(17,True)
       #self.buzzers.value = True
       sleep(0.3)
       gpio.output(17,False)
       #self.buzzers.value = False
       #self.buzzers.value = False


   def buzzer3(self):
       #print("beep beep beep")
       gpio.output(17,True)
       sleep(0.35)
       gpio.output(17,False)
       sleep(0.1)
       gpio.output(17,True)
       sleep(0.35)
       gpio.output(17,False)
       sleep(0.1)
       gpio.output(17,True)
       sleep(0.35)
       gpio.output(17,False)



   def bloqueoeleccionfrecuencias(self):
       self.bloqueofrecuencias=1
       self.ui.f1.hide()
       self.ui.f2.hide()
       self.ui.f3.hide()
       self.ui.f4.hide()
       self.ui.frecuencia1bloqueo_4.raise_()
       self.ui.frecuencia1bloqueo.raise_()
       self.ui.frecuencia1bloqueo_2.raise_()
       self.ui.frecuencia1bloqueo_3.raise_()
       self.ui.frecuencia1bloqueo_4.show()
       self.ui.frecuencia1bloqueo.show()
       self.ui.frecuencia1bloqueo_2.show()
       self.ui.frecuencia1bloqueo_3.show()


   def habilitacioneleccionfrecuencias(self):
       self.bloqueofrecuencias=0
       self.ui.f1.raise_()
       self.ui.f2.raise_()
       self.ui.f3.raise_()
       self.ui.f4.raise_()
       self.ui.f1.show()
       self.ui.f2.show()
       self.ui.f3.show()
       self.ui.f4.show()
       self.ui.frecuencia1bloqueo_4.hide()
       self.ui.frecuencia1bloqueo.hide()
       self.ui.frecuencia1bloqueo_2.hide()
       self.ui.frecuencia1bloqueo_3.hide()




   def instancia_pulsadores(self,pulsador):
       pulsador.setStyleSheet("background-image: url(3 - Boton configuracion.png);\n"
                                              "border-image: url(4 - Boton configuracion instancia.png);")

   def verificarversion(self):
       self.buzzer()
       self.ui.pushButtonupdate.setStyleSheet("background-image: url(3 - Boton configuracion.png);\n"
                                              "border-image: url(trasnp.png);")
       self.ui.stackedWidget.setCurrentIndex(16)
       self.numpagina = 16
       self.bloqueodepaginas(self.numpagina)

       try:
           connection = sql.connect('versionactual.db')
           cur = connection.cursor()
           instruccion = 'SELECT version FROM codigo'
           cur.execute(instruccion)
           version = cur.fetchone()
           connection.commit()
           connection.close()

           connection = sql.connect('versionnueva.db')
           cur = connection.cursor()
           instruccion = 'SELECT version FROM codigonuevo'
           cur.execute(instruccion)
           versionnueva = cur.fetchone()
           connection.commit()
           connection.close()
           #print(version)
           #print(versionnueva)

           if version[0] != versionnueva[0]:
               self.ui.label_20.setGeometry(QtCore.QRect(450, 385, 636, 56))
               self.ui.label_20.setText(f'<font color="white">version disponible para actualizar:  V{versionnueva[0]} <font>')

               self.ui.pushButtonvolver_update.setGeometry(QtCore.QRect(370, 475, 220, 56))
               self.ui.pushButtonactualizar_confirmar.setEnabled(True)
               #self.ui.pushButtonactualizar_confirmar.raise_()
               #self.ui.pushButtonactualizar_confirmar.show()



           else:
             self.ui.label_20.setGeometry(QtCore.QRect(350, 385, 636, 56))
             self.ui.label_20.setText("el software se encuentra actualizado a la versión más reciente.")
             self.ui.pushButtonactualizar_confirmar.setEnabled(False)
             #self.ui.pushButtonvolver_update.setGeometry(QtCore.QRect(500, 475, 220, 56))
             #self.ui.pushButtonactualizar_confirmar.hide()
       except:
           self.auxiliar10=0







   def instancia_volver_pagina(self,encabezado):
       self.buzzer()
       encabezado.setStyleSheet("background-image: url(encabezado instancia.png);")

   def volver_a_pagina(self,indice,encabezado):
       encabezado.setStyleSheet("background-image: url(Inicio encabezado.png);")
       self.ui.stackedWidget.setCurrentIndex(indice)
       self.numpagina = indice
       self.bloqueodepaginas(self.numpagina)



   def actualizarsoft(self):
      try:
       os.system("sudo python3 /home/texel/script_actualizacion.py")
      except:
        self.auxiliar10=0

   def instanciasubetrat(self):
        self.auxiliar10=0


   def instanciabajatrat(self):
       self.auxiliar10 = 0


# instancias para los pushbutton: potencia, frio, y tiempo
   def instanciasube(self):
       self.auxiliar10=0

   def instanciabaja(self):
       self.auxiliar10=0


   def instanciasubetiempo(self):
       self.auxiliar10=0


   def instanciabajatiempo(self):
       self.auxiliar10=0



   def habilitarpulsador(self):
       self.buzzer()
       self.ui.pushButtoninfo.setEnabled(True)
       self.ui.pushButtoneliminar.setEnabled(True)
       self.ui.pushButtonseleccionar.setEnabled(True)
       self.ui.deseleccionarperfil.setEnabled(True)
       self.ui.pushButtoncrear.setEnabled(True)
       self.ui.pushButtonagregar.setEnabled(False)



#cada vez que se va la pantalla de menu, se inicializa con los valores por defecto
   def inicializar(self):
       self.ui.selecciontrat.setText("manual")
       self.frecuencia1()
       self.cabezalactivo = 1
       self.valorpotencia=0
       self.frecuenciaelegida="1.3 mhz"
       self.tratamientoelegido="manual"
       self.genero="femenino"
       self.eleccion="manual"
       self.cabezalelegido = "corporal multi tec"
       self.niveldefrioelegido="desactivado"
       self.ui.potencia.setText(str(self.valorpotencia) + '%')
       self.ui.cabezal1.setStyleSheet("background-image: url(Cabezal Grande.png);\n" "")
       self.ui.cabezal2.setStyleSheet("background-image: url(6 - Trabajando cabezal 2 inactivo.png);\n" "")
       self.ui.cabezal3.setStyleSheet("background-image: url(6 - Trabajando cabezal 3 inactivo.png);\n" "")
       self.ui.cabezal4.setStyleSheet("background-image: url(6 - Trabajando cabezal 4 inactivo.png);\n" "")
       self.ui.label_13.setText("20 hz")
       ##self.ui.label_15.setText("programa 3")
       self.ui.label_12.setText("2Hz-vacio medio")
       self.ui.programasvacio.setStyleSheet("background-image: url(2Hz.png);")
       self.programapemf=4
       self.contadorpemf=4
       self.programavacio=9
       self.contadorvacio=5
       self.formaonda = "triangular"
       self.nivelvacio = "medio"

       self.bloquearpotencia()

       self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                        "border-image: url(Boton chico activo.png);")
       self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                       "border-image: url(Boton chico inactivo.png);")
       self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                        "border-image: url(Boton chico activo.png);")
       self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                       "border-image: url(Boton chico inactivo.png);")
       self.pedirestado()

   def bloquearpotencia(self):
       self.ui.pulsbajapotencia.setEnabled(False)
       self.ui.pulssubepotencia.setEnabled(False)
       self.ui.pulssubepotencia.setStyleSheet(
           "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
       self.ui.pulsbajapotencia.setStyleSheet(
           "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")

   def desbloquearpotencia(self):
       self.ui.pulsbajapotencia.setEnabled(True)
       self.ui.pulssubepotencia.setEnabled(True)
       self.ui.pulssubepotencia.setStyleSheet(
           "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
       self.ui.pulsbajapotencia.setStyleSheet(
           "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")

   # escribe datos serie, en particular envia el comando 0x01
   def pedirestado(self):
        if self.prioridadenviodatossesion==0:
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
            if self.estado[2] > 250:
               self.ui.temperatura.setText("-1°C")
            else:
               self.ui.temperatura.setText(str(self.estado[2]) + '°C')
            if self.estado[2] ==245:
              self.ui.temperatura.setText("ND")
            #print(self.estado[1])
            self.controldelsistema()
            self.estadodelsistema()
            #print(self.estado[0])
            #print(hex(self.estado[0]))
            #print(hex(self.estado[1]))
            #print(self.estado[2])

   def cartelerrorcabezal(self):
       msgBox1 = QMessageBox()
       msgBox1.setIcon(QMessageBox.Critical)
       msgBox1.setWindowFlags(Qt.FramelessWindowHint)
       msgBox1.setStyleSheet("QPushButton{ width:75px; font-size: 18px; }")
       msgBox1.setStyleSheet("background-image: url(fondoactividad.png);" )

       msgBox1.setFont(QtGui.QFont('Myriad Pro Cond', 15))
       if self.cabezalactivo==1:
          msgBox1.setText("cabezal corporal multitec desconectado")
       if self.cabezalactivo==2:
          msgBox1.setText("cabezal corporal desconectado")
       if self.cabezalactivo==3:
          msgBox1.setText("cabezal facial bipolar desconectado")
       if self.cabezalactivo==4:
          msgBox1.setText("cabezal facial multipolar desconectado")
       msgBox1.setWindowTitle("ERROR:")
       msgBox1.setStandardButtons(QMessageBox.Ok)
       returnValue = msgBox1.exec()
       if returnValue == QMessageBox.Ok:
           self.reconocererror()


   def cartelerrorsensorflujo(self):
       msgBox2 = QMessageBox()
       msgBox2.setIcon(QMessageBox.Critical)
       msgBox2.setWindowFlags(Qt.FramelessWindowHint)
       msgBox2.setFont(QtGui.QFont('Myriad Pro Cond', 15))
       msgBox2.setStyleSheet("QPushButton{ width:75px; font-size: 18px; }")
       msgBox2.setStyleSheet("background-image: url(fondoactividad.png);")
       msgBox2.setText("error sensor de flujo")
       msgBox2.setWindowTitle("ERROR")
       msgBox2.setStandardButtons(QMessageBox.Ok)
       returnValue = msgBox2.exec()
       if returnValue == QMessageBox.Ok:
           self.reconocererror()

   def cartelerrorsensortemp(self):
       msgBox3 = QMessageBox()
       msgBox3.setIcon(QMessageBox.Critical)
       msgBox3.setWindowFlags(Qt.FramelessWindowHint)
       msgBox3.setFont(QtGui.QFont('Myriad Pro Cond', 15))
       msgBox3.setStyleSheet("QPushButton{ width:75px; font-size: 18px; }")
       msgBox3.setStyleSheet("background-image: url(fondoactividad.png);")
       msgBox3.setText("cabezal corporal multitec desconectado")

       msgBox3.setWindowTitle("ERROR")
       msgBox3.setStandardButtons(QMessageBox.Ok)
       returnValue = msgBox3.exec()
       if returnValue == QMessageBox.Ok:
           self.reconocererror()

   def reconocererror(self):
       packet2 = bytearray()
       packet2.append(0x0D)
       packet2.append(0x00)
       packet2.append(0x00)
       packet2.append(0x00)
       packet2.append(0x00)
       puertoserie.write(packet2)
       #sleep(0.1)
       #puertoserie.write(packet2)


   def controldelsistema(self):  # NOTA: SE DEBE CORREGIR EL HECHO QUE PARAQ QUE DETECTE LOS CABEZALES DESCONECTADOS EL FRIO DEBE SER CERO

       if self.habilitarcontrol == True:
           if self.iniciarsesion == True and self.estado[0] == 0x01:
               if (self.estado[1] != 0x8f)or (self.estado[1] != 0xcf):
                   if self.cabezalactivo == 1 and ( self.estado[1] == 0x8e or self.estado[1] == 0x80 or self.estado[1] == 0x82 or self.estado[1] == 0x84 or self.estado[1] == 0x88 or self.estado[1] == 0x86 or self.estado[1] == 0x8a or self.estado[1] == 0x8c):
                       self.detenerportimer()
                       self.cartelerrorcabezal()
                   if self.cabezalactivo == 2 and (self.estado[1] == 0x80 or self.estado[1] == 0x8d or self.estado[1] == 0x89 or self.estado[1] == 0x8c or self.estado[1] == 0x88 or self.estado[1] == 0x81 or self.estado[1] == 0x84 or self.estado[1] == 0x85):
                       self.detenerportimer()
                       self.cartelerrorcabezal()
                   if self.cabezalactivo == 3 and (self.estado[1] == 0x80 or self.estado[1] == 0x8b or self.estado[1] == 0x89 or self.estado[1] == 0x88 or self.estado[1] == 0x8a or self.estado[1] == 0x83 or self.estado[1] == 0x82 or self.estado[1] == 0x81):
                       self.detenerportimer()
                       self.cartelerrorcabezal()
                   if self.cabezalactivo == 4 and (self.estado[1] == 0x80 or self.estado[1] == 0x87 or self.estado[1] == 0x81 or self.estado[1] == 0x83 or self.estado[1] == 0x82 or self.estado[1] == 0x85 or self.estado[1] == 0x86 or self.estado[1] == 0x84):
                       self.detenerportimer()
                       self.cartelerrorcabezal()





   # esta funcion se encarga llamar a la funcion de consulta de estado cada 4 segundos
   def estadodelsistema(self):

       self.timerest2.start(4000)



   #manejo de nivel de potencia. La funcion "actualizar" se llama cada vez que se suelta el slider. la razon que se llame a  la funcion "enviardatos..." es para asegurarse de enviar el valor correspondiente actualziado. si no uso la funcion actualizar, sucede que al bajar la potencia a cero, en la placa no va a cero sino a nu valor cercano.
   def subirpotencia(self):
     if self.iniciarsesion==True:
       self.buzzer()
       #self.ui.pulssubepotencia.setGeometry(QtCore.QRect(411, 232, 75, 56))
       #self.ui.pulssubepotencia.setStyleSheet("background-image: url(Boton arriba instancia.png);\n" "border-image: url(Boton arriba instancia.png);")
       self.valorpotencia+=2
       if self.valorpotencia>100:
           self.valorpotencia=100
       self.animarlabel2(self.ui.potencia,30,40)
       self.ui.potencia.setText(str(self.valorpotencia) + '%')

       if self.iniciarsesion == True: #and self.activarradio==1:
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesion()

       self.animarpulsadores(self.ui.pulssubepotencia,410, 255, 402, 247, 76, 57)



   def bajarpotencia(self):
     if self.iniciarsesion==True:
       self.buzzer()
       #self.ui.pulsbajapotencia.setGeometry(QtCore.QRect(510, 230, 75, 56))
      # self.ui.pulsbajapotencia.setStyleSheet("background-image: url(Boton abajo instancia.png);\n" "border-image: url(Boton abajo instancia.png);")
       self.valorpotencia -= 2
       if self.valorpotencia < 0:
           self.valorpotencia = 0
       self.animarlabel2(self.ui.potencia,30,40)
       self.ui.potencia.setText(str(self.valorpotencia) + '%')
       if self.iniciarsesion == True: #and self.activarradio==1:
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesion()
       self.animarpulsadores(self.ui.pulsbajapotencia,510, 255,502, 247, 76, 57)



   # se encarga de hacer transcurrir el tiempo de sesion, una vez que llega acero, se llama a la funcion "detener por timer"
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
         self.ui.tiemporeloj.setText(self.text)

         if self.minutosesion == '00' and self.segundosesion == '00':
            self.detenerportimer2()

   def detenerportimer2(self):
       self.bloquearpotencia()
       self.timercab.stop()
       packet2 = bytearray()
       packet2.append(11)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       puertoserie.write(packet2)

       sleep(0.1)

       packet9 = bytearray()
       packet9.append(5)
       packet9.append(0)
       packet9.append(0)
       packet9.append(0)
       packet9.append(0)
       puertoserie.write(packet9)

       self.pausarsesion = 0
       # self.detenersesion()
       if self.auxiliar == 0:
           #self.vecespulsadasfinalizar=0
           self.ui.texto_iniciar.setText("iniciar")
           self.pause = True
           self.bloqueoporcarteliniciorapido = 0
           self.ui.cartel.raise_()
           self.ui.confirmar.raise_()
           self.ui.cancelar.raise_()
           self.ui.cancelar_2.raise_()
           self.ui.textocartel.raise_()
           self.ui.cartel.show()
           self.ui.confirmar.show()
           self.ui.cancelar.show()
           self.ui.cancelar_2.show()
           self.ui.textocartel.show()
           self.ui.confirmar.hide()
           self.buzzer3()



   def detenerportimer(self):
       self.detenervaciolaserpemf()
       #self.frecuenciahistorial()
       #self.guardarperfilnombre=1
       self.iniciarsesion = False  ######cambio######
       packet2 = bytearray()
       packet2.append(11)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       puertoserie.write(packet2)
       sleep(0.1)
       puertoserie.write(packet2)
       #self.segundo = 60
       #self.minuto = self.aux1
       #self.seteosesion = True
       #self.resetearreloj()
       #self.ui.pulssubetiempo.setStyleSheet("background-image: url(trasnp.png);\n"
                             #            "border-image: url(Boton arriba.png);")
      # self.ui.pulsbajatiempo.setStyleSheet("background-image: url(trasnp.png);\n"
                            #             "border-image: url(Boton abajo.png);")
       self.ui.label_23.setGeometry(QtCore.QRect(1060, 727, 21, 41))
       self.ui.label_23.setStyleSheet("background-image: url(Icono Iniciar.png);")
       self.vecespulsadas=0
       #self.ui.pulsbajatiempo.setEnabled(True)
       #self.ui.pulssubetiempo.setEnabled(True)
      # if self.guardarperfilnombre == 0:
        #   self.ui.texto_iniciorapidoencabezado_2.hide()
         #  self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 40, 196, 60))
          # self.nombre = "casual"
       self.ui.texto_iniciar.setText("iniciar")
       #self.ui.texto_iniciorapidoencabezado_2.hide()
       #self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 40, 196, 60))
       #self.guardarperfilnombre=0
       #self.agregarpersona()
       #sleep(0.1)
       #self.cargardatosentabla()
       #self.id = 0
       #self.nombre = "casual"
       #self.desbloquearpotencia()
       self.timercab.stop()
       self.buzzer3()



   def seleccionrapidatratamiento(self):

       if self.eleccion=="rostro":
           if self.contadortratamiento > 3:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 3
           if self.contadortratamiento==1:
               self.setearvalorestratamiento(self.flacidezsuprostro)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido="flacidez superficial"
           if self.contadortratamiento==2:
               self.setearvalorestratamiento(self.flacidezprofrostro)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento==3:
               self.setearvalorestratamiento(self.zonaorbicular)
               self.ui.selecciontrat.setText("zona orbicular")
               self.tratamientoelegido = "zona orbicular"

       if self.eleccion=="cuello":
           if self.contadortratamiento > 2:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 2
           if self.contadortratamiento==1:
               self.setearvalorestratamiento(self.cuelloflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento==2:
               self.setearvalorestratamiento(self.cuelloflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"

       if self.eleccion == "escote":
           if self.contadortratamiento > 2:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 2
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.escoteflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.escoteflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"

       if self.eleccion == "abdomen":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.abdomenflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.abdomenflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.abdomenestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.abdomencelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.abdomencelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.abdomenadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"
           #if self.contadortratamiento == 7:
              # self.setearvalorestratamiento(self.abdomenadiposidad)
               #self.ui.selecciontrat.setText("adiposidad")
               #self.tratamientoelegido = "adiposidad"
           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adipleveabdomen)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodabdomen)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"


       if self.eleccion =="brazos ant" or self.eleccion=="brazos post":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.brazosflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.brazosflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.brazosestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.brazoscelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.brazoscelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.brazosadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"
           #if self.contadortratamiento == 7:
               #self.setearvalorestratamiento(self.brazosadiposidad)
               #self.ui.selecciontrat.setText("adiposidad")
               #self.tratamientoelegido = "adiposidad"
           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adiplevebrazos)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodbrazos)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"

       if self.eleccion == "muslos ant":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.muslosantflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.muslosantflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.muslosantestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.muslosantcelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.muslosantcelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.muslosantadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"
           #if self.contadortratamiento == 7:
               #self.setearvalorestratamiento(self.muslosantadiposidad)
               #self.ui.selecciontrat.setText("adiposidad")
               #self.tratamientoelegido = "adiposidad"
           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adiplevemuslosant)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodmuslosant)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"


       if self.eleccion == "muslos int":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.muslosintflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.muslosintflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.muslosintestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.muslosintcelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.muslosintcelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.muslosintadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"
           #if self.contadortratamiento == 7:
               #self.setearvalorestratamiento(self.muslosintadiposidad)
               #self.ui.selecciontrat.setText("adiposidad")
               #self.tratamientoelegido = "adiposidad"
           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adiplevemuslosint)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodmuslosint)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"

       if self.eleccion == "escapular":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.escapularflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.escapularflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.escapularestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.escapularcelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.escapularcelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.escapularadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"

           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adipleveescapular)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodescapular)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"

       if self.eleccion == "flancos":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.flancosflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.flancosflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.flancosestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.flancoscelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.flancoscelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.flancosadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"

           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adipleveflancos)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodflancos)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"

       if self.eleccion == "trocanteriana":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.trocanflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.trocanflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.trocanestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.trocancelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.trocancelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.trocanadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"

           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adiplevetrocan)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodtrocan)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"

       if self.eleccion == "muslos post":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.muslosposflacidezsup)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.muslosposflacidezprof)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.muslosposestrias)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.muslosposcelyflac)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.muslosposcelulitis)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.muslosposadipycel)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"

           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adiplevemuslospos)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodmuslospos)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"

       if self.eleccion == "gluteos":
           if self.contadortratamiento > 8:
               self.contadortratamiento = 1
           if self.contadortratamiento < 1:
               self.contadortratamiento = 8
           if self.contadortratamiento == 1:
               self.setearvalorestratamiento(self.flacidezsupgluteos)
               self.ui.selecciontrat.setText("flacidez superficial")
               self.tratamientoelegido = "flacidez superficial"
           if self.contadortratamiento == 2:
               self.setearvalorestratamiento(self.flacidezprofgluteos)
               self.ui.selecciontrat.setText("flacidez profunda")
               self.tratamientoelegido = "flacidez profunda"
           if self.contadortratamiento == 3:
               self.setearvalorestratamiento(self.estriasgluteos)
               self.ui.selecciontrat.setText("estrias")
               self.tratamientoelegido = "estrias"
           if self.contadortratamiento == 4:
               self.setearvalorestratamiento(self.celyflacgluteos)
               self.ui.selecciontrat.setText("celulitis y flacidez")
               self.tratamientoelegido = "celulitis y flacidez"
           if self.contadortratamiento == 5:
               self.setearvalorestratamiento(self.celulitisgluteos)
               self.ui.selecciontrat.setText("celulitis")
               self.tratamientoelegido = "celulitis"
           if self.contadortratamiento == 6:
               self.setearvalorestratamiento(self.adipycelgluteos)
               self.ui.selecciontrat.setText("adiposidad y celulitis")
               self.tratamientoelegido = "adiposidad y celulitis"
           if self.contadortratamiento == 7:
               self.setearvalorestratamiento(self.adiplevegluteos)
               self.ui.selecciontrat.setText("adiposidad leve")
               self.tratamientoelegido = "adiposidad leve"
           if self.contadortratamiento == 8:
               self.setearvalorestratamiento(self.adipmodgluteos)
               self.ui.selecciontrat.setText("adiposidad moderada")
               self.tratamientoelegido = "adiposidad moderada"




# programacion de instancias
   def mouseReleaseEvent(self, event):

       if self.posxy2[0] < 620 and self.posxy2[0] > 24 and self.posxy2[1] < 750 and self.posxy2[1] > 590:
           self.ui.configuracion.setStyleSheet("background-image: url(3 - Boton configuracion.png);")
           sleep(0.1)
           self.ui.stackedWidget.setCurrentIndex(15)  # estoy en la pantalla de menu y voy a la de configuracion
           self.numpagina = 15
           self.bloqueodepaginas(self.numpagina)



       if self.posxy15[0] < 110 and self.posxy15[0] > 10 and self.posxy15[1] < 110 and self.posxy15[1] > 20:

           sleep(0.05)
           self.ui.encabezado_menu_config.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(2)  # estoy en pagina de seleccion de sexo y voy a la de menu
           self.numpagina = 2
           self.bloqueodepaginas(self.numpagina)


       if self.posxy13[0] < 110 and self.posxy13[0] > 10 and self.posxy13[1] < 110 and self.posxy13[1] > 20:
           sleep(0.1)
           self.ui.encabezadoperfil_2.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.cursor_buzzer=0
           self.ui.stackedWidget.setCurrentIndex(15)  #estoy en pagina de seleccion de sexo y voy a la de menu
           self.numpagina = 15
           self.bloqueodepaginas(self.numpagina)


       if self.posxy0[0] < 1264 and self.posxy0[0] > 1022 and self.posxy0[1] < 775 and self.posxy0[1] > 710:
         sleep(0.1)
         self.ui.inicia1.setStyleSheet("background-image: url(Boton Iniciar-finalizar.png);")

       #if self.posxy0[0] < 1010 and self.posxy0[0] > 780 and self.posxy0[1] < 775 and self.posxy0[1] > 710:
           #sleep(0.1)
           #self.ui.detiene1.setStyleSheet("background-image: url(Boton Iniciar-finalizar.png);")

       if self.posxy5[0] < 110 and self.posxy5[0] > 10 and self.posxy5[1] < 110 and self.posxy5[1] > 20 and self.flagzonatratamientosmujer == 1:
           sleep(0.1)
           self.ui.encabezadotratatmujer.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(4) #estoy en la pagína 5 de seleccion de tratamientos de rostro, y voy a la 4 de seleccion de zonas mujer
           self.numpagina = 4
           self.bloqueodepaginas(self.numpagina)

       if self.posxy5[0] < 110 and self.posxy5[0] > 10 and self.posxy5[1] < 110 and self.posxy5[1] > 20 and self.flagzonatratamientoshombre == 1:
           sleep(0.1)
           self.ui.encabezadotratatmujer.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(6)  ##estoy en la pagína 5 de seleccion de tratamientos de rostro, y voy a la 6 de seleccion de zonas hombre
           self.numpagina = 6
           self.bloqueodepaginas(self.numpagina)

       if self.posxy9[0] < 110 and self.posxy9[0] > 10 and self.posxy9[1] < 110 and self.posxy9[1] > 20 and self.flagzonatratamientosmujer == 1:
           sleep(0.1)
           self.ui.encabezadotratamientomujer2_3.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(4)  ##estoy en la pagína 9 de seleccion de tratamientos de cuello y escote, y voy a la 4 de seleccion de zonas mujer
           self.numpagina = 4
           self.bloqueodepaginas(self.numpagina)

       if self.posxy9[0] < 110 and self.posxy9[0] > 10 and self.posxy9[1] < 110 and self.posxy9[1] > 20 and self.flagzonatratamientoshombre == 1:
           sleep(0.1)
           self.ui.encabezadotratamientomujer2_3.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(6)  ##estoy en la pagína 9 de seleccion de tratamientos de cuello y escote, y voy a la 6 de seleccion de zonas hombre
           self.numpagina = 6
           self.bloqueodepaginas(self.numpagina)

       if self.posxy8[0] < 110 and self.posxy8[0] > 10 and self.posxy8[1] < 110 and self.posxy8[1] > 20 and self.flagzonatratamientosmujer == 1:
           sleep(0.1)
           self.ui.encabezadotratamientomujer2_2.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(4)  ##estoy en la pagína 9 de seleccion de tratamientos de gluteos, y voy a la 4 de seleccion de zonas mujer
           self.numpagina = 4
           self.bloqueodepaginas(self.numpagina)

       if self.posxy8[0] < 110 and self.posxy8[0] > 10 and self.posxy8[1] < 110 and self.posxy8[1] > 20 and self.flagzonatratamientoshombre == 1:
           sleep(0.1)
           self.ui.encabezadotratamientomujer2_2.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(6)  ##estoy en la pagína 8 de seleccion de tratamientos de gluteos, y voy a la 6 de seleccion de zonas hombre
           self.numpagina = 6
           self.bloqueodepaginas(self.numpagina)

       if self.posxy7[0] < 110 and self.posxy7[0] > 10 and self.posxy7[1] < 110 and self.posxy7[1] > 20 and self.flagzonatratamientosmujer == 1:
           sleep(0.1)
           self.ui.encabezadotratamientomujer2.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(4)  ##estoy en la pagína 7 de seleccion de tratamientos de zonas restantes, y voy a la 4 de seleccion de zonas mujer
           self.numpagina = 4
           self.bloqueodepaginas(self.numpagina)

       if self.posxy7[0] < 110 and self.posxy7[0] > 10 and self.posxy7[1] < 110 and self.posxy7[1] > 20 and self.flagzonatratamientoshombre == 1:
           sleep(0.1)
           self.ui.encabezadotratamientomujer2.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(6) ##estoy en la pagína 7 de seleccion de tratamientos de zonas restantes, y voy a la 4 de seleccion de zonas hombre
           self.numpagina = 6
           self.bloqueodepaginas(self.numpagina)


       if self.posxy6[0] < 110 and self.posxy6[0] > 10 and self.posxy6[1] < 110 and self.posxy6[1] > 20 and self.bloqueoregresopagina==0:
           sleep(0.1)
           self.ui.encabezadoselecciontrat_2.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(3)  # estoy en pagina de seleccion de zonas hombre y voy a la de seleecion de sexo - regreso
           self.numpagina = 3
           self.bloqueodepaginas(self.numpagina)
           self.flagzonatratamientoshombre = 0


       if self.posxy4[0] < 110 and self.posxy4[0] > 10 and self.posxy4[1] < 110 and self.posxy4[1] > 20 and self.bloqueoregresopagina==0:
           sleep(0.1)
           self.ui.encabezadoselecciontrat.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(3)  # estoy en pagina de seleccion de zonas de mujer y voy a la de seleccion de sexo - regreso
           self.numpagina = 3
           self.bloqueodepaginas(self.numpagina)
           self.flagzonatratamientosmujer = 0


       if self.posxy3[0] < 110 and self.posxy3[0] > 10 and self.posxy3[1] < 110 and self.posxy3[1] > 20:
           sleep(0.1)
           self.ui.encabezadosexo.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.selecciontratamiento.setStyleSheet("background-image: url(3 - Boton seleccionar tratamiento.png);")
           self.ui.stackedWidget.setCurrentIndex(2)  # estoy en pagina de seleccion de sexo y voy a la de menu
           self.numpagina = 2
           self.bloqueodepaginas(self.numpagina)


       if self.posxy11[0] < 110 and self.posxy11[0] > 10 and self.posxy11[1] < 110 and self.posxy11[1] > 20:
           self.quitarteclado()
           #sleep(0.05)
           self.cursor_buzzer=0
           self.ui.encabezadoperfil.setStyleSheet("background-image: url(Inicio encabezado.png);")
           if self.infoadicional==0:
              self.ui.stackedWidget.setCurrentIndex(2)  # estoy en pagina de seleccion de sexo y voy a la de menu
              self.numpagina = 2
              self.bloqueodepaginas(self.numpagina)
              self.cargardatosentabla()
              self.activarperfil = 0

           if self.infoadicional==1:
              self.ui.stackedWidget.setCurrentIndex(11)  # estoy en pagina de seleccion de sexo y voy a la de menu
              self.numpagina = 11
              self.bloqueodepaginas(self.numpagina)
              self.cargardatosentabla()
              self.infoadicional=0
              self.activarperfil = 1
              #self.acondicionarelementosperfil()





       if self.posxy10[0] < 110 and self.posxy10[0] > 10 and self.posxy10[1] < 110 and self.posxy10[1] > 20:

           sleep(0.05)
           self.ui.encabezadoactividad.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(2)  # estoy en pagina de seleccion de sexo y voy a la de menu
           self.numpagina = 2
           self.bloqueodepaginas(self.numpagina)





       if self.posxy2[0] < 110 and self.posxy2[0] > 10 and self.posxy2[1] < 110 and self.posxy2[1] > 20:
           sleep(0.1)
           self.ui.encabezado_menu.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(1)  # estoy en de menu y voy a la de presentacion - regreso
           self.numpagina = 1
           self.bloqueodepaginas(self.numpagina)


       if self.posxy0[0] < 110 and self.posxy0[0] > 10 and self.posxy0[1] < 110 and self.posxy0[1] > 20 and self.iniciarsesion==False and self.vecespulsadasflag==False:
           sleep(0.1)
           self.ui.iniciorapido.setStyleSheet("background-image: url(3 - Boton Inicio rapido.png);")
           self.ui.selfemenino.setStyleSheet("background-image: url(9 - Seleccion genero femenino.png);")
           self.ui.selmasculino.setStyleSheet("background-image: url(9 - Seleccion genero masculino.png);")
           self.ui.selecciontratamiento.setStyleSheet("background-image: url(3 - Boton seleccionar tratamiento.png);")
           self.ui.encabezado_iniciorapido.setStyleSheet("background-image: url(Inicio encabezado.png);")
           self.ui.stackedWidget.setCurrentIndex(2)  # estoy en pagina de inicio rapido y voy a la de menu - regreso
           self.ui.pulssubetratamiento.setEnabled(True)
           self.ui.pulsbajatratamiento.setEnabled(True)
           self.ui.pulssubetratamiento.setStyleSheet("background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsbajatratamiento.setStyleSheet("background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           #self.ui.selecciondetratrapidobloqueo.hide()
           self.numpagina = 2
           self.bloqueodepaginas(self.numpagina)
           self.resetearfrecuencias()


       # zona orbicular
       if self.posxy5[0] < 630 and self.posxy5[0] > 20 and self.posxy5[1] < 300 and self.posxy5[1] > 150:
           sleep(0.1)
           self.ui.pulsadorflacidez_sup.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.flacidezsuprostro)
           self.ui.selecciontrat.setText("flacidez superficial")
           self.tratamientoelegido="flacidez superficial"





       if self.posxy5[0] < 630 and self.posxy5[0] > 20 and self.posxy5[1] < 415 and self.posxy5[1] > 310:
           sleep(0.1)
           self.ui.pulsadorflacidez_prof.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.flacidezprofrostro)
           self.ui.selecciontrat.setText("flacidez profunda")
           self.tratamientoelegido="flacidez profunda"

       if self.posxy5[0] < 1250 and self.posxy5[0] > 650 and self.posxy5[1] < 300 and self.posxy5[1] > 150:
           sleep(0.1)
           self.ui.pulsadorzonaorbic_2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.zonaorbicular)
           self.ui.selecciontrat.setText("zona orbicular")
           self.tratamientoelegido="zona orbicular"


       # zona gluteos

       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 300 and self.posxy8[1] > 160:
           sleep(0.1)
           self.ui.pulsadorflacidezcutaneasup.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.flacidezsupgluteos)
           self.ui.selecciontrat.setText("flacidez cutanea superficial")
           self.tratamientoelegido="flacidez cut sup"

       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 450 and self.posxy8[1] > 315:
           sleep(0.1)
           self.ui.pulsadorflacidezcutaneaprof.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.flacidezprofgluteos)
           self.ui.selecciontrat.setText("flacidez cutanea profunda")
           self.tratamientoelegido="flacidez cut prof"
       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 600 and self.posxy8[1] > 470:
           sleep(0.1)
           self.ui.pulsadorestrias_2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.estriasgluteos)
           self.ui.selecciontrat.setText("estrias")
           self.tratamientoelegido="estrias"


       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 760 and self.posxy8[1] > 630:
           sleep(0.1)
           self.ui.pulsadorflacidezycelu_2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.celyflacgluteos)
           self.ui.selecciontrat.setText("celulitis y flacidez")
           self.tratamientoelegido="celulitis y flacidez"

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 290 and self.posxy8[1] > 160:
           sleep(0.1)
           self.ui.pulsadorcelulitis_3.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.celulitisgluteos)
           self.ui.selecciontrat.setText("celulitis")
           self.tratamientoelegido="celulitis"

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 450 and self.posxy8[1] > 315:
           sleep(0.1)
           self.ui.pulsadoradiposidadycelu_3.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.adipycelgluteos)
           self.ui.selecciontrat.setText("adiposidad y celulitis")
           self.tratamientoelegido="adip y celulitis"

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 600 and self.posxy8[1] > 470:
           sleep(0.1)
           self.ui.pulsador_adiposidad_4.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.adiplevegluteos)
           self.ui.selecciontrat.setText("adiposidad leve")
           self.tratamientoelegido="adiposidad leve"

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 760 and self.posxy8[1] > 630:
           sleep(0.1)
           self.ui.pulsador_adiposidad_3.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.setearvalorestratamiento(self.adipmodgluteos)
           self.ui.selecciontrat.setText("adiposidad moderada")
           self.tratamientoelegido="adiposidad mod."

       # zonas restantes #

       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 300 and self.posxy7[1] > 160:
           sleep(0.1)
           self.ui.pulsadorflacidez_sup2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.muslosantflacidezsup)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.escapularflacidezsup)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.brazosflacidezsup)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.flancosflacidezsup)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.trocanflacidezsup)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.muslosposflacidezsup)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.abdomenflacidezsup)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.muslosintflacidezsup)
           self.ui.selecciontrat.setText("flacidez superficial")
           self.tratamientoelegido="flacidez superficial"

       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 450 and self.posxy7[1] > 315:
           sleep(0.1)
           self.ui.pulsadorflacidez_prof2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.muslosantflacidezprof)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.escapularflacidezprof)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.brazosflacidezprof)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.flancosflacidezprof)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.trocanflacidezprof)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.muslosposflacidezprof)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.abdomenflacidezprof)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.muslosintflacidezprof)
           self.tratamientoelegido="flacidez profunda"
           self.ui.selecciontrat.setText("flacidez profunda")


       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 600 and self.posxy7[1] > 470:
           sleep(0.1)
           self.ui.pulsadorestrias.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.muslosantestrias)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.escapularestrias)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.brazosestrias)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.flancosestrias)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.trocanestrias)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.muslosposestrias)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.abdomenestrias)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.muslosintestrias)
           self.tratamientoelegido="estrias"
           self.ui.selecciontrat.setText("estrias")


       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 760 and self.posxy7[1] > 630:
           sleep(0.1)
           self.ui.pulsadorflacidezycelu.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.muslosantcelyflac)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.escapularcelyflac)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.brazoscelyflac)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.flancoscelyflac)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.trocancelyflac)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.muslosposcelyflac)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.abdomencelyflac)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.muslosintcelyflac)
           self.tratamientoelegido="celulitis y flacidez"
           self.ui.selecciontrat.setText("celulitis y flacidez")


       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 290 and self.posxy7[1] > 160:
           sleep(0.1)
           self.ui.pulsadorcelulitis.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.muslosantcelulitis)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.escapularcelulitis)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.brazoscelulitis)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.flancoscelulitis)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.trocancelulitis)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.muslosposcelulitis)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.abdomencelulitis)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.muslosintcelulitis)
           self.tratamientoelegido="celulitis"
           self.ui.selecciontrat.setText("celulitis")


       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 450 and self.posxy7[1] > 315:
           sleep(0.1)
           self.ui.pulsadoradiposidadycelu.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.muslosantadipycel)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.escapularadipycel)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.brazosadipycel)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.flancosadipycel)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.trocanadipycel)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.muslosposadipycel)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.abdomenadipycel)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.muslosintadipycel)
           self.tratamientoelegido="adip. y celulitis"
           self.ui.selecciontrat.setText("adiposidad y celulitis")


       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 600 and self.posxy7[1] > 470:
           sleep(0.1)
           self.ui.pulsador_adiposidad.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.adiplevemuslosant)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.adipleveescapular)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.adiplevebrazos)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.adipleveflancos)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.adiplevetrocan)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.adiplevemuslospos)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.adipleveabdomen)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.adiplevemuslosint)
           self.tratamientoelegido="adiposidad leve"
           self.ui.selecciontrat.setText("adiposidad leve")

       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 760 and self.posxy7[1] > 630:
           sleep(0.1)
           self.ui.pulsador_adiposidad_5.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "muslos ant":
               self.setearvalorestratamiento(self.adipmodmuslosant)
           if self.eleccion == "escapular":
               self.setearvalorestratamiento(self.adipmodescapular)
           if self.eleccion == "brazos post" or self.eleccion == "brazos ant":
               self.setearvalorestratamiento(self.adipmodbrazos)
           if self.eleccion == "flancos":
               self.setearvalorestratamiento(self.adipmodflancos)
           if self.eleccion == "trocanteriana":
               self.setearvalorestratamiento(self.adipmodtrocan)
           if self.eleccion == "muslos post":
               self.setearvalorestratamiento(self.adipmodmuslospos)
           if self.eleccion == "abdomen":
               self.setearvalorestratamiento(self.adipmodabdomen)
           if self.eleccion == "muslos int":
               self.setearvalorestratamiento(self.adipmodmuslosint)
           self.tratamientoelegido="adiposidad mod."
           self.ui.selecciontrat.setText("adiposidad moderada")


       # cuello y escote
       if self.posxy9[0] < 630 and self.posxy9[0] > 30 and self.posxy9[1] < 300 and self.posxy9[1] > 160:
           sleep(0.1)
           self.ui.pulsadorflacidez_sup_2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "cuello":
               self.setearvalorestratamiento(self.cuelloflacidezsup)
           if self.eleccion == "escote":
               self.setearvalorestratamiento(self.escoteflacidezsup)
           self.ui.selecciontrat.setText("flacidez superficial")
           self.tratamientoelegido="flacidez superficial"

       if self.posxy9[0] < 1250 and self.posxy9[0] > 660 and self.posxy9[1] < 290 and self.posxy9[1] > 160:
           sleep(0.1)
           self.ui.pulsadorflacidez_prof_2.setStyleSheet("background-image: url(16 - Tipo de tratamiento botones.png);")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de seleccion de tratamientos y voy a la  de inicio rapido,
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           if self.eleccion == "cuello":
               self.setearvalorestratamiento(self.cuelloflacidezsup)
           if self.eleccion == "escote":
               self.setearvalorestratamiento(self.escoteflacidezprof)
           self.ui.selecciontrat.setText("flacidez profunda")
           self.tratamientoelegido="flacidez profunda"


       # pantalla de actividad
       if self.posxy2[0] < 1250 and self.posxy2[0] > 650 and self.posxy2[1] < 550 and self.posxy2[1] > 350:


           sleep(0.1)
           self.ui.actividad.setStyleSheet("background-image: url(3 - Boton actividad.png);")
           self.ui.stackedWidget.setCurrentIndex(10)  # estoy en pagina de menu y voy a actividad

           #if len(self.personas)>1500:
              #self.eliminar2()

              #self.ui.tableWidget.clear()

       #pantalla de inicio rapido
       if self.posxy2[0] < 600 and self.posxy2[0] > 30 and self.posxy2[1] < 350 and self.posxy2[1] > 160:
           sleep(0.1)
           self.ui.texto_iniciorapidoencabezado.setText("inicio rápido")
           self.ui.stackedWidget.setCurrentIndex(0)  # estoy en pagina de menu y voy a la de inicio rapido
           self.ui.pulssubetratamiento.setEnabled(False)
           self.ui.pulsbajatratamiento.setEnabled(False)
           #self.ui.selecciondetratrapidobloqueo.raise_()
           #self.ui.selecciondetratrapidobloqueo.show()
           self.ui.pulssubetratamiento.setStyleSheet("background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsbajatratamiento.setStyleSheet("background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.numpagina=0
           self.bloqueodepaginas(self.numpagina)


       #pantalla de seleccion de perfil
       if self.posxy2[0] < 630 and self.posxy2[0] > 20 and self.posxy2[1] < 560 and self.posxy2[1] > 370:
           sleep(0.1)
           self.ui.seleccionarperfil.setStyleSheet("background-image: url(3 - Boton seleccionar perfil.png);")
           self.ui.stackedWidget.setCurrentIndex(11)  # estoy en pagina de menu y voy a la de perfil
           self.numpagina = 11
           self.bloqueodepaginas(self.numpagina)
           self.cargardatosenlista()
           self.ocultarpulsperfil()
           self.ui.lineEditnombre.setText("pulse y escriba para modificar")
           self.ui.lineEditdni.setText("pulse y escriba para modificar")
           self.ui.lineEditdireccion.setText("pulse y escriba para modificar")
           self.ui.lineEditcorreo.setText("pulse y escriba para modificar")

           #self.ui.listWidget.setStyleSheet("QListWidget::item { background-color: transparent; }")
           #self.ui.listWidget.setStyleSheet("QListWidget::item:selected { background-color: black; }")


       #pantall de seleccion de sexo mujer
       if self.posxy3[0] < 600 and self.posxy3[0] > 54 and self.posxy3[1] < 700 and self.posxy3[1] > 200:
           sleep(0.1)
           self.ui.stackedWidget.setCurrentIndex(4)  # estoy en pagina de seleccion de sexo y voy a la de seleccion de zonas mujer
           self.numpagina = 4
           self.bloqueodepaginas(self.numpagina)
           self.genero="femenino"

       #pantalla de seleccion de sexo hombre
       if self.posxy3[0] < 1100 and self.posxy3[0] > 800 and self.posxy3[1] < 900 and self.posxy3[1] > 163:
          sleep(0.1)
          self.ui.stackedWidget.setCurrentIndex(6)  # estoy en pagina de seleccion de sexo y voy a la de seleccion de zonas hombre
          self.numpagina = 6
          self.bloqueodepaginas(self.numpagina)
          self.genero="masculino"


       #pantalla de menu
       if self.posxy1[0] < 1280 and self.posxy1[0] > 0 and self.posxy1[1] < 800 and self.posxy1[1] > 0:
           sleep(0.1)
           self.ui.stackedWidget.setCurrentIndex(2)   #estoy en pagina de presentacion y voy a la pagina de menu
           self.ui.pantalla1b.setText('<font color="white">presione la pantalla para continuar<font>')
           self.numpagina = 2
           self.bloqueodepaginas(self.numpagina)


       #pantalla de seleccion de sexo
       if self.posxy2[0] < 1250 and self.posxy2[0] > 660 and self.posxy2[1] < 350 and self.posxy2[1] > 160:
           #self.pedirestado()
           sleep(0.1)
           self.ui.stackedWidget.setCurrentIndex(3)  # estoy en pagina de menu y voy a la de seleccion de sexo


       # dependiendo si se elije mujer u hombre que se ativa la página correspondiente
       if self.flagzonatratamientosmujer == 1 and self.bloqueozona==0:
           self.seleccionartratamientoinstancia(self.posxy4[0], self.posxy4[1])

       if self.flagzonatratamientoshombre == 1 and self.bloqueozona==0:
           self.seleccionartratamientoinstancia(self.posxy6[0], self.posxy6[1])



   def seleccionartratamientoinstancia(self,x6,y6):
       if x6 < 310 and x6 > 260 and y6 < 460 and y6> 410 or x6 < 500 and x6 > 450 and y6 < 460 and y6 > 410:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona brazos")
               self.ui.brazospoteriores.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zonas brazos")
               self.ui.brazospoteriores_2.raise_()


       if x6 < 430 and x6 > 310 and y6 < 450 and y6 > 360:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
              self.ui.cartelconfirmarzona.setText("zona sub escapulares")
              self.ui.subescapulares.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona sub escapulares")
               self.ui.subescapulares_2.raise_()



       if x6 < 450 and x6 > 290 and y6 < 510 and y6 > 450:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona flancos")
               self.ui.flancos.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona flancos")
               self.ui.flancos_2.raise_()

       if x6 < 590 and x6 > 300 and y6 < 620 and y6 > 545:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona gluteos")
               self.ui.gluteos.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona gluteos")
               self.ui.gluteos_2.raise_()



       if x6< 295 and x6 > 280 and y6 < 695 and y6 > 620 or x6 < 490 and x6 > 460 and y6 < 700 and y6 > 610:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
              self.ui.cartelconfirmarzona.setText("zonas trocanterianas")
              self.ui.trocanteriana.raise_()
           if self.flagzonatratamientoshombre == 1:
              self.ui.cartelzona2.setText("zonas trocanterianas")
              self.ui.trocanteriana_2.raise_()

       if x6 < 430 and x6 > 315 and y6 < 730 and y6 > 630:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zonas muslos posteriores")
               self.ui.muslospos.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona muslos posteriores")
               self.ui.muslospos_2.raise_()


       if x6 < 940 and x6 > 870 and y6 < 260 and y6 > 180:

           self.bloqueozona=1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona rostro completo")
               self.ui.rostro.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona rostro completo")
               self.ui.rostro_2.raise_()

       if x6 < 940 and x6> 880 and y6< 320 and y6 > 285:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona cuello")
               self.ui.cuello.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona cuello")
               self.ui.cuello_2.raise_()

       if x6 < 980 and x6 > 830 and y6 < 400 and y6 > 330:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona escote")
               self.ui.escote.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona escote")
               self.ui.escote_2.raise_()

       if x6 < 840 and x6 > 790 and y6 < 460 and y6 > 380 or x6 < 1080 and x6 > 980 and y6 < 460 and y6 > 300:

           self.bloqueozona=1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1 :
               self.ui.cartelconfirmarzona.setText("zona brazos anteriores")
               self.ui.brazosanteriores.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona brazos anteriores")
               self.ui.brazosanteriores_2.raise_()

       if x6 < 950 and x6 > 860 and y6 < 550 and y6 > 430:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona abdomen")
               self.ui.abdomen.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona abdomen")
               self.ui.abdomen_2.raise_()

       if x6 < 880 and x6> 830 and y6< 725 and y6 > 560 or x6 < 990 and x6 > 940 and y6 < 725 and y6 > 560:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona muslos anteriores")
               self.ui.muslosanteriores.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona muslos anteriores")
               self.ui.muslosanteriores_2.raise_()


       if x6 < 940 and x6> 900 and y6 < 710 and y6 > 630:

           self.bloqueozona = 1
           sleep(0.3)
           self.cartelemergente()
           if self.flagzonatratamientosmujer == 1:
               self.ui.cartelconfirmarzona.setText("zona muslos internos")
               self.ui.muslosinternos.raise_()
           if self.flagzonatratamientoshombre == 1:
               self.ui.cartelzona2.setText("zona muslos internos")
               self.ui.muslosinternos_2.raise_()

   def ocultarpulsperfil(self):
       self.ui.pushButtonseleccionar.setEnabled(False)
       self.ui.deseleccionarperfil.setEnabled(False)
       self.ui.pushButtoninfo.setEnabled(False)
       self.ui.pushButtoneliminar.setEnabled(False)
       self.ui.pushButtonagregar.setEnabled(False)



   def adquirirusuario(self):
       self.buzzer()
       self.nombredered=self.ui.listWidget_2.currentItem().text()
       self.ui.texto_dni_2.setText(self.nombredered)

   def mostrarredesinicio(self):

     try:
       self.ui.listWidget_2.clear()
       self.ui.listWidget_2.addItem("")
       cmd = "sudo iwlist wlan0 scan | grep 'ESSID'"
       output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       stdout, stderr = output.communicate()
       redes=stdout.decode().strip().split('\n')
       for red in redes:
           #self.ui.listWidget_2.addItem("")
           if "ESSID" in red:
               redwifi=red.split("ESSID:")[1].strip('"')
               redwifi="      " + str(redwifi)
               self.ui.listWidget_2.addItem(redwifi)
     except:
         self.ui.listWidget_2.addItem("no hay redes disponibles")



   def mostrarredeswifi(self):
     self.timerwifi2.stop()
     try:
       self.ui.listWidget_2.clear()
       self.ui.listWidget_2.addItem("")

       cmd = "sudo iwlist wlan0 scan | grep 'ESSID'"
       output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       stdout, stderr = output.communicate()
       redes=stdout.decode().strip().split('\n')
       for red in redes:
           #self.ui.listWidget_2.addItem("")
           if "ESSID" in red:
               redwifi=red.split("ESSID:")[1].strip('"')
               redwifi="      " + str(redwifi)
               self.ui.listWidget_2.addItem(redwifi)
       self.ui.stackedWidget.setCurrentIndex(13)  # estoy en la pantalla de menu y voy a la de configuracion
       self.numpagina = 13
       self.bloqueodepaginas(self.numpagina)
       self.auxiliar10 = 0


     except:
         self.ui.listWidget_2.addItem("no hay redes disponibles")
         self.ui.stackedWidget.setCurrentIndex(13)  # estoy en la pantalla de menu y voy a la de configuracion
         self.numpagina = 13
         self.bloqueodepaginas(self.numpagina)
         self.auxiliar10 = 0

   #def conectarred(essid, key):  esta funcion serviria si se usa WPA/WPA2.
    #   cmd = f"sudo iwconfig wlan0 essid {essid} key {key}"
     #  subprocess.call(cmd, shell=True)

      # result = subprocess.run(["iwgetid", "-r"], stdout=subprocess.PIPE)

       #if result.returncode == 0:
       #    connected_network = result.stdout.decode("utf-8").strip()
        #   print(f"Connected to: {connected_network}")
       #else:
       #    print("Not connected to any network")










# funcion del cartel de confirmar zona
   def cartelemergente(self):
      self.bloqueoregresopagina=1
      if self.flagzonatratamientosmujer==1:
          self.ui.cartelconfirmarmujer.show()
          self.ui.cartelconfirmarzona.show()
          self.ui.cartelaceptar.show()
          self.ui.cartelcancelar.show()
          self.ui.ustedhaseleccionado.show()
          self.ui.cartelconfirmarmujer.raise_()
          self.ui.cartelconfirmarzona.raise_()
          self.ui.cartelaceptar.raise_()
          self.ui.cartelcancelar.raise_()
          self.ui.ustedhaseleccionado.raise_()
      if self.flagzonatratamientoshombre==1:
          self.ui.cartelconfirmarhombre.show()
          self.ui.cartelzona2.show()
          self.ui.cartelaceptar2.show()
          self.ui.cartelcancelar2.show()
          self.ui.ustehaseleccionado2.show()
          self.ui.cartelconfirmarhombre.raise_()
          self.ui.cartelzona2.raise_()
          self.ui.cartelaceptar2.raise_()
          self.ui.cartelcancelar2.raise_()
          self.ui.ustehaseleccionado2.raise_()



   def mostrarmanual(self):
       self.buzzer()
       try:
           os.system("sudo python3 /home/texel/maintext.py")
           #url = 'file:hometexelweb1.0.0manual.html'
           #webbrowser.open(url, new=2)
           #webbrowser.open(url, new=2)
       except:
           self.auxiliar10 = 0

   def quitarcartelemergente(self):
       self.bloqueoregresopagina = 0
       self.ui.cartelconfirmarmujer.hide()
       self.ui.cartelconfirmarzona.hide()
       self.ui.cartelaceptar.hide()
       self.ui.cartelcancelar.hide()
       self.ui.ustedhaseleccionado.hide()
       self.ui.cartelconfirmarhombre.hide()
       self.ui.cartelzona2.hide()
       self.ui.cartelaceptar2.hide()
       self.ui.cartelcancelar2.hide()
       self.ui.ustehaseleccionado2.hide()

       #la siguiente funcion se ejecuta cada vez que se detecta un click en la pantalla
   def mousePressEvent(self, event):

       #manejo de las paginas

       self.posxy0[0], self.posxy0[1] = event.pos().x() * self.bloqueopaginas[0]*self.bloqueoporcarteliniciorapido , event.pos().y() * self.bloqueopaginas[0]*self.bloqueoporcarteliniciorapido  # pantalla de inicio rapido
       self.posxy1[0], self.posxy1[1] = event.pos().x() * self.bloqueopaginas[1] , event.pos().y() * self.bloqueopaginas[1]     # pantalla de presentacion crio
       self.posxy2[0], self.posxy2[1] = event.pos().x() * self.bloqueopaginas[2] , event.pos().y() * self.bloqueopaginas[2]     # pantalla de menu
       self.posxy3[0], self.posxy3[1] = event.pos().x() * self.bloqueopaginas[3] , event.pos().y() * self.bloqueopaginas[3]    # pantalla de seleccion de sexo
       self.posxy4[0], self.posxy4[1] = event.pos().x() * self.bloqueopaginas[4] , event.pos().y() * self.bloqueopaginas[4]   # pantalla de seleccion de zonas mujer
       self.posxy5[0], self.posxy5[1] = event.pos().x() * self.bloqueopaginas[5], event.pos().y() * self.bloqueopaginas[5]    #pantalla de seleccion de tratamientos zona orbicular
       self.posxy6[0], self.posxy6[1] = event.pos().x() * self.bloqueopaginas[6] , event.pos().y() * self.bloqueopaginas[6]     # pantalla de selccion de zonas hombre
       self.posxy7[0], self.posxy7[1] = event.pos().x() * self.bloqueopaginas[7] , event.pos().y() * self.bloqueopaginas[7]     #pantalla de seleccion de tratamientos para zonas restantes
       self.posxy8[0], self.posxy8[1] = event.pos().x() * self.bloqueopaginas[8], event.pos().y() * self.bloqueopaginas[8]       #pantalla de seleccion de tratamientos gluteos
       self.posxy9[0], self.posxy9[1] = event.pos().x() * self.bloqueopaginas[9], event.pos().y() * self.bloqueopaginas[9]       #pantalla de seleccion de tratamientos para cuello y escote
       self.posxy10[0], self.posxy10[1] = event.pos().x() * self.bloqueopaginas[10], event.pos().y() * self.bloqueopaginas[10]   #pantalla de actividad
       self.posxy11[0], self.posxy11[1] = event.pos().x() * self.bloqueopaginas[11], event.pos().y() * self.bloqueopaginas[11]   #pantalla de perfil
       self.posxy12[0], self.posxy12[1] = event.pos().x() * self.bloqueopaginas[12], event.pos().y() * self.bloqueopaginas[12]   # info adicional de perfil seleccionado
       self.posxy13[0], self.posxy13[1] = event.pos().x() * self.bloqueopaginas[13], event.pos().y() * self.bloqueopaginas[13]     #pantalla de configuracion
       self.posxy14[0], self.posxy14[1] = event.pos().x() * self.bloqueopaginas[14], event.pos().y() * self.bloqueopaginas[14]  # info adicional de perfil seleccionado
       self.posxy15[0], self.posxy15[1] = event.pos().x() * self.bloqueopaginas[15], event.pos().y() * self.bloqueopaginas[15]  # pantalla de configuracion
       self.posxy16[0], self.posxy16[1] = event.pos().x() * self.bloqueopaginas[16], event.pos().y() * self.bloqueopaginas[16]  # pantalla de configuracion
       self.posxy17[0], self.posxy17[1] = event.pos().x() * self.bloqueopaginas[17], event.pos().y() * self.bloqueopaginas[17]  # pantalla de configuracion
       #print(self.posxy0[0])
       #print(self.posxy0[1])


       #los siguientes if, funcionan en conjunto con la funcion mouse release event()

       if self.posxy2[0] < 620 and self.posxy2[0] > 24 and self.posxy2[1] < 750 and self.posxy2[1] > 590:
           self.buzzer()
           self.quitarteclado2()
           self.ui.configuracion.setStyleSheet("background-image: url(4 - Boton configuracion instancia.png);")
           self.activarconfig=1
           #self.acondicionarelementosconfig()
           #self.comprobarconexion()



       #pantalla de bienvenida
       if self.posxy1[0] < 1280 and self.posxy1[0] > 0 and self.posxy1[1] < 800 and self.posxy1[1] > 0:
           self.ui.pantalla1b.setText('<font color="grey">presione la pantalla para continuar<font>')
           self.buzzer()

       #pantalla de inicio rapido
       if self.posxy2[0] < 600 and self.posxy2[0] > 30 and self.posxy2[1] < 350 and self.posxy2[1] > 160:
           self.buzzer()
           self.vecespulsadasfinalizar =0
           if self.guardarperfilnombre == 0:
               self.ui.texto_iniciorapidoencabezado_2.hide()
               self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 40, 196, 60))
               self.nombre = "casual"
               self.ui.texto_iniciorapidoencabezado.setText("inicio rápido")
           #self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 20, 196, 60))
           #self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 10, 250, 120))
           #self.ui.texto_iniciorapidoencabezado.setText(
                                            #  "<body><p><span style=\" color:black;\">tratamiento</span></p><p> perfil: felix</p> </body>")
           self.ui.iniciorapido.setStyleSheet("background-image: url(4 - Boton Inicio rapido instancia.png);")
           self.numpagina = 0
           self.bloqueodepaginas(self.numpagina)
           self.resetearfrecuencias()
           self.inhibirresolverfrec=0
           self.deshabilitar_buzzer = 1
           self.bloquear_animaciones=1
           self.activarpemf()
           self.bloquear_animaciones = 1
           self.activarvacum()
           self.bloquear_animaciones = 1
           self.activarradiofrecuencia()
           self.bloquear_animaciones = 1
           self.activarlaser()
           self.inicializar()
           self.deshabilitar_buzzer = 0

       # pantalla de perfil
       if self.posxy2[0] < 630 and self.posxy2[0] > 20 and self.posxy2[1] < 560 and self.posxy2[1] > 370:
          self.buzzer()
          self.ui.pushButtonagregar.setEnabled(False)
          self.ui.seleccionarperfil.setStyleSheet("background-image: url(4 - Boton seleccionar perfil instancia.png);")
          self.activarperfil=1
          #self.acondicionarelementosperfil()

       # pantalla de ayuda
       #if self.posxy2[0] < 1250 and self.posxy2[0] > 650 and self.posxy2[1] < 770 and self.posxy2[1] > 600:
         #self.mostrarmanual()


       # pantalla de  seleccion de sexo
       if self.posxy2[0] < 1250 and self.posxy2[0] > 660 and self.posxy2[1] < 350 and self.posxy2[1] > 160:
           self.buzzer()
           self.ui.selecciontratamiento.setStyleSheet("background-image: url(4 - Boton seleccionar tratamiento instancia.png);")
           self.numpagina = 3
           self.bloqueodepaginas(self.numpagina)




       #pantalla de actividad
       if self.posxy2[0] < 1250 and self.posxy2[0] > 650 and self.posxy2[1] < 550 and self.posxy2[1] > 350:
           self.buzzer()
           sleep(0.1)
           self.ui.actividad.setStyleSheet("background-image: url(4 - Boton actividad instancia.png);")
           self.numpagina = 10
           self.bloqueodepaginas(self.numpagina)



       #pantalla sexo femenino
       if self.posxy3[0] < 600 and self.posxy3[0] > 54 and self.posxy3[1] < 700 and self.posxy3[1] > 200:
           self.animaropcioneszonas(1)
           self.ui.texto_iniciorapidoencabezado.setText("tratamiento")
           #self.animarlabel4()
           self.buzzer()
           self.ui.selfemenino.setStyleSheet("background-image: url(10 - Seleccion genero femenino instancia.png);")
           self.flagzonatratamientosmujer=1
           self.flagzonatratamientoshombre = 0
           self.ui.sexo.setStyleSheet("background-image: url(7 - Trabajando dibujo mujer.png);")
           self.cambiarsexo=0
           self.ui.icono_mujer3_2.setStyleSheet("background-image: url(Seleccionar tratamioento mujer.png);")
           self.ui.icono_mujer3_3.setStyleSheet("background-image: url(Seleccionar tratamioento mujer.png);")
           self.ui.icono_mujer1.setStyleSheet("background-image: url(Seleccionar tratamioento mujer.png);")
           self.ui.icono_mujer2.setStyleSheet("background-image: url(Seleccionar tratamioento mujer.png);")
           self.ui.icono_mujer3.setStyleSheet("background-image: url(Seleccionar tratamioento mujer.png);")



       # pantalla sexo masculino
       if self.posxy3[0] < 1100 and self.posxy3[0] > 800 and self.posxy3[1] < 900 and self.posxy3[1] > 163:
           self.buzzer()
           self.ui.texto_iniciorapidoencabezado.setText("tratamiento")
           self.ui.selmasculino.setStyleSheet("background-image: url(10 - Seleccion genero masculino instancia.png);")
           self.flagzonatratamientosmujer = 0
           self.flagzonatratamientoshombre = 1
           self.animaropcioneszonas(0)
           self.ui.sexo.setStyleSheet("background-image: url(7 - Trabajando dibujo hombre.png);")
           self.cambiarsexo = 1
           self.ui.icono_mujer3_2.setStyleSheet("background-image: url(Seleccionar tratamioento hombre.png);")
           self.ui.icono_mujer3_3.setStyleSheet("background-image: url(Seleccionar tratamioento hombre.png);")
           self.ui.icono_mujer1.setStyleSheet("background-image: url(Seleccionar tratamioento hombre.png);")
           self.ui.icono_mujer2.setStyleSheet("background-image: url(Seleccionar tratamioento hombre.png);")
           self.ui.icono_mujer3.setStyleSheet("background-image: url(Seleccionar tratamioento hombre.png);")

       #dependiendo si se elige femenino o  masculino, se pone el flag en 1 y se llama a la funcion seleccionar tratamiento en la pagina 4 o 6 dependiendo si es masculino o femenino.
       if self.flagzonatratamientosmujer==1:

            self.seleccionartratamiento(self.posxy4[0],self.posxy4[1])
            self.ui.encabezadotratatmujer.setStyleSheet("background-image: url(Inicio encabezado.png);")
            self.ui.encabezadotratamientomujer2.setStyleSheet("background-image: url(Inicio encabezado.png);")
            self.ui.encabezadotratamientomujer2_2.setStyleSheet("background-image: url(Inicio encabezado.png);")
            self.ui.encabezadotratamientomujer2_3.setStyleSheet("background-image: url(Inicio encabezado.png);")

       if self.flagzonatratamientoshombre==1:

          self.seleccionartratamiento(self.posxy6[0], self.posxy6[1])
          self.ui.encabezadotratatmujer.setStyleSheet("background-image: url(Inicio encabezado.png);")
          self.ui.encabezadotratamientomujer2.setStyleSheet("background-image: url(Inicio encabezado.png);")
          self.ui.encabezadotratamientomujer2_2.setStyleSheet("background-image: url(Inicio encabezado.png);")
          self.ui.encabezadotratamientomujer2_3.setStyleSheet("background-image: url(Inicio encabezado.png);")



       # LLAMADA A TRATAMIENTOS: corresponde a la pantalla 5, al presionar se genera la instancia y al soltar,  se va a la pagina de inicio rapido

       #zona orbicular
       if self.posxy5[0] < 630 and self.posxy5[0] > 20 and self.posxy5[1] < 300 and self.posxy5[1] > 150:
           self.ui.pulsadorflacidez_sup.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy5[0] < 630 and self.posxy5[0] > 20 and self.posxy5[1] < 415 and self.posxy5[1] > 310:
           self.ui.pulsadorflacidez_prof.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy5[0] < 1250 and self.posxy5[0] > 650 and self.posxy5[1] < 300 and self.posxy5[1] > 150:
           self.ui.pulsadorzonaorbic_2.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

        #zona gluteos

       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 300 and self.posxy8[1] > 160:
           self.ui.pulsadorflacidezcutaneasup.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 450 and self.posxy8[1] > 315:
           self.ui.pulsadorflacidezcutaneaprof.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 600 and self.posxy8[1] > 470:
           self.ui.pulsadorestrias_2.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 630 and self.posxy8[0] > 30 and self.posxy8[1] < 760 and self.posxy8[1] > 630:
           self.ui.pulsadorflacidezycelu_2.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 290 and self.posxy8[1] > 160:
           self.ui.pulsadorcelulitis_3.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 450 and self.posxy8[1] > 315:
           self.ui.pulsadoradiposidadycelu_3.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 1250 and self.posxy8[0] > 660 and self.posxy8[1] < 600 and self.posxy8[1] > 470:
           self.ui.pulsador_adiposidad_4.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy8[0] < 1250and self.posxy8[0] > 660 and self.posxy8[1] < 760 and self.posxy8[1] > 630:
           self.ui.pulsador_adiposidad_3.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       # zonas restantes #

       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 300 and self.posxy7[1] > 160:
           self.ui.pulsadorflacidez_sup2.setStyleSheet( "background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 450 and self.posxy7[1] > 315:
           self.ui.pulsadorflacidez_prof2.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 600 and self.posxy7[1] > 470:
           self.ui.pulsadorestrias.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 630 and self.posxy7[0] > 30 and self.posxy7[1] < 760 and self.posxy7[1] > 630:
           self.ui.pulsadorflacidezycelu.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 290 and self.posxy7[1] > 160:
           self.ui.pulsadorcelulitis.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 450 and self.posxy7[1] > 315:
           self.ui.pulsadoradiposidadycelu.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 600 and self.posxy7[1] > 470:
           self.ui.pulsador_adiposidad.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy7[0] < 1250 and self.posxy7[0] > 660 and self.posxy7[1] < 760 and self.posxy7[1] > 630:
           self.ui.pulsador_adiposidad_5.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       #cuello y escote
       if self.posxy9[0] < 630 and self.posxy9[0] > 30 and self.posxy9[1] < 300 and self.posxy9[1] > 160:
           self.ui.pulsadorflacidez_sup_2.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()

       if self.posxy9[0] < 1250 and self.posxy9[0] > 660 and self.posxy9[1] < 290 and self.posxy9[1] > 160:
           self.ui.pulsadorflacidez_prof_2.setStyleSheet("background-image: url(17 - Tipo de tratamiento botones instancias.png);")
           self.buzzer()



       ##################################  MANEJO DE FRECUENCIAS         ################################

       if self.posxy0[0] <120  and self.posxy0[0] > 65 and self.posxy0[1] < 320 and self.posxy0[1] > 255 and self.bloqueofrecuencias==0:
          self.frecuencia1()
          self.buzzer()


       if self.posxy0[0] < 200 and self.posxy0[0] > 145 and self.posxy0[1] < 320 and self.posxy0[1] > 255 and self.cabezalbipolarseguridad==False  and self.bloqueofrecuencias==0:
           self.frecuencia2()
           self.buzzer()


       if self.posxy0[0] < 280 and self.posxy0[0] > 225 and self.posxy0[1] < 320 and self.posxy0[1] > 255 and self.cabezalbipolarseguridad==False  and self.bloqueofrecuencias==0 :
          self.frecuencia3()
          self.buzzer()


       if self.posxy0[0] < 365 and self.posxy0[0] > 310 and self.posxy0[1] < 320 and self.posxy0[1] > 255 and self.cabezalbipolarseguridad==False  and self.bloqueofrecuencias==0 :
          self.frecuencia4()
          self.buzzer()



   ############################## MANEJO IMAGEN SELECCION DE SEXO #################################

       #if self.posxy0[0] < 1200 and self.posxy0[0] > 1110 and self.posxy0[1] < 670 and self.posxy0[1] > 430:
           #self.buzzer()
           #if self.cambiarsexo==0:
             # self.ui.sexo.setStyleSheet("background-image: url(7 - Trabajando dibujo hombre.png);\n""")
             # self.genero = "masculino"
           #if self.cambiarsexo==1:
            #  self.genero = "femenino"
             # self.ui.sexo.setStyleSheet("background-image: url(7 - Trabajando dibujo mujer.png);\n""")
          # self.cambiarsexo= not self.cambiarsexo


   #################################      MANEJO DE CABEZALES       ########################################


       if self.posxy0[0] < 1030 and self.posxy0[0] > 960 and self.posxy0[1] < 680 and self.posxy0[1] > 530 :
           self.buzzer()
           self.cabezalbipolarseguridad=False
           self.potenciacero()
           self.ui.cabezal1.setStyleSheet("border-image: url(Cabezal Grande.png);\n"
                                       "background-image: url(trasnp.png);")
           self.cabezalactivo=1
           self.cabezal(self.cabezalactivo)
           self.activarradio = 1
           self.habilitarpemf = 1
           self.habilitarlaser = 1
           self.bloquear_animaciones = 1
           self.activarlaser()
           self.bloquear_animaciones = 1
           self.activarvacio = 1
           self.activarvacum()
           self.bloquear_animaciones = 1
           self.activarpemf()
           self.bloquear_animaciones = 1
           self.activarradiofrecuencia()
           #self.enviardatosdesesion()
           self.valorpotencia = 0
           self.ui.potencia.setText(str(self.valorpotencia) + '%')

           self.cabezalelegido="corporal multi tec"
           self.ui.f2desac.hide()
           self.ui.f3desac.hide()
           self.ui.f4desact.hide()
           #print(self.activarradio)
           if self.iniciarsesion == False:
               self.bloquearpotencia()
           self.timercab.stop()







       if self.posxy0[0] < 930 and self.posxy0[0] > 860 and self.posxy0[1] < 680 and self.posxy0[1] > 530 :
           self.buzzer()
           self.potenciacero()
           self.bloquear_animaciones = 1
           self.activarradio = 1
           self.activarradiofrecuencia()
           self.cabezalactivo = 2
           self.cabezal(self.cabezalactivo)
           self.cabezalbipolarseguridad=False
           self.habilitarpemf = 1
           self.bloquear_animaciones = 1
           self.activarvacio = 1
           self.activarvacum()
           self.bloquear_animaciones = 1
           self.activarpemf()
           self.bloquear_animaciones = 1
           self.habilitarlaser = 1
           self.activarlaser()
           #self.enviardatosdesesion()
           self.valorpotencia=0
           self.ui.potencia.setText(str(self.valorpotencia) + '%')
           self.cabezalelegido = "corporal multi"
           self.ui.f2desac.hide()
           self.ui.f3desac.hide()
           self.ui.f4desact.hide()
           #print(self.activarradio)
           if self.iniciarsesion == False:
               self.bloquearpotencia()
           if self.activarvacio==1 or self.habilitarpemf==1 or self.habilitarlaser==1:
             self.animacioncabezalmultitec()




       if self.posxy0[0] < 830 and self.posxy0[0] > 765 and self.posxy0[1] < 680 and self.posxy0[1] >530 :
           self.buzzer()
           self.potenciacero()
           self.resetearfrecuencias()
           self.frecuencia1()
           self.resolverfrec()
           self.inhibirresolverfrec = 0
           self.cabezalbipolarseguridad = True
           self.bloquear_animaciones = 1
           self.activarradio = 1
           self.activarradiofrecuencia()
           self.cabezalactivo = 3
           self.cabezal(self.cabezalactivo)
           self.ui.f2.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.ui.f3.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.ui.f4.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.habilitarpemf = 1
           self.activarvacio = 1
           self.bloquear_animaciones = 1
           self.activarvacum()
           self.bloquear_animaciones = 1
           self.activarpemf()
           self.bloquear_animaciones = 1
           self.habilitarlaser = 1
           self.activarlaser()


           #self.enviardatosdesesion()
           self.valorpotencia = 0
           self.ui.potencia.setText(str(self.valorpotencia) + '%')
           self.cabezalelegido = "facial bipolar"
           self.ui.f2desac.raise_()
           self.ui.f3desac.raise_()
           self.ui.f4desact.raise_()
           self.ui.f2desac.show()
           self.ui.f3desac.show()
           self.ui.f4desact.show()
           #print(self.activarradio)
           if self.iniciarsesion == False:
               self.bloquearpotencia()
           if self.activarvacio == 1 or self.habilitarpemf == 1 or self.habilitarlaser == 1:
               self.animacioncabezalmultitec()



       if self.posxy0[0] < 730 and self.posxy0[0] > 650 and self.posxy0[1] < 680 and self.posxy0[1] > 530 :
           self.buzzer()
           self.potenciacero()
           self.cabezalbipolarseguridad = False
           self.bloquear_animaciones = 1
           self.activarradio = 1
           self.activarradiofrecuencia()
           self.cabezalactivo = 4
           self.cabezal(self.cabezalactivo)
           self.habilitarpemf = 1
           self.activarvacio = 1
           self.bloquear_animaciones = 1
           self.activarvacum()
           self.bloquear_animaciones = 1
           self.activarpemf()
           self.bloquear_animaciones = 1
           self.habilitarlaser = 1
           self.activarlaser()
           #self.enviardatosdesesion()
           self.valorpotencia = 0
           self.ui.potencia.setText(str(self.valorpotencia) + '%')
           self.cabezalelegido = "facial multi"
           self.ui.f2desac.hide()
           self.ui.f3desac.hide()
           self.ui.f4desact.hide()
           #print(self.activarradio)
           if self.iniciarsesion==False:
               self.bloquearpotencia()
           if self.activarvacio == 1 or self.habilitarpemf == 1 or self.habilitarlaser == 1:
               self.animacioncabezalmultitec()




     ########################### FUNCION PARA ARRANCAR SESION ####################################################

       if self.posxy0[0] < 1264 and self.posxy0[0] > 1022 and self.posxy0[1] < 775 and self.posxy0[1] > 710:

         self.buzzer()
         self.ui.inicia1.setStyleSheet("background-image: url(7 - Trabajando iniciar instancia.png);")
         self.ui.pulssubetiempo.setStyleSheet("background-image: url(trasnp.png);\n"
                                              "border-image: url(Boton arriba inactivo.png);")
         self.ui.pulsbajatiempo.setStyleSheet("background-image: url(trasnp.png);\n"
                                              "border-image: url(Boton abajo inactivo.png);")
         self.ui.pulsbajatiempo.setEnabled(False)
         self.ui.pulssubetiempo.setEnabled(False)
         self.ui.texto_iniciar.setText("pausar")
         self.ui.label_23.setGeometry(QtCore.QRect(1060, 727, 27, 41))
         self.ui.label_23.setStyleSheet("background-image: url(Icono Pausar.png);")
         self.vecespulsadas += 1
         if self.vecespulsadas==1:
           if self.activarradio==1:
              self.desbloquearpotencia()
           self.comenzarsesion()
           #self.ui.texto_iniciar.setText('<font color="grey">iniciar<font>')
           #self.ui.label_23.setStyleSheet("background-image: url(Icono Iniciar instancia.png);")
           #self.ui.texto_finalizar.setText('<font color="black">finalizar<font>')
           #self.ui.label_24.setStyleSheet("background-image: url(Icono Finalizar.png);")
           #self.ui.pushButtonenablefrec.setStyleSheet("background-image: url(3.png);\n" "border-image: url(frec3.png);")


           #self.ui.areatiempobloqueo.raise_()
           #self.ui.areatiempobloqueo.show()
           self.habilitarcontrol=True
           #self.controldelsistema()
           if (self.cabezalactivo==2 or self.cabezalactivo==3 or self.cabezalactivo==4) and (self.activarvacio==1 or self.habilitarpemf==1 or self.habilitarlaser==1):
               self.animacioncabezalmultitec()
         if  self.vecespulsadas==2:
           self.vecespulsadasflag=True
           self.ui.texto_iniciar.setText("continuar")
           self.ui.label_23.setGeometry(QtCore.QRect(1060, 727, 21, 41))
           self.ui.label_23.setStyleSheet("background-image: url(Icono Iniciar.png);")
           self.ui.pulssubepotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsbajapotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulssubepotencia.setEnabled(False)
           self.ui.pulsbajapotencia.setEnabled(False)
           self.vecespulsadas=0

           self.iniciarsesion=False
           packet2 = bytearray()
           packet2.append(11)
           packet2.append(0)
           packet2.append(0)
           packet2.append(0)
           packet2.append(0)
           puertoserie.write(packet2)
           sleep(0.1)
           puertoserie.write(packet2)
           self.detenervaciolaserpemf()
       #print(self.activarradio)

       if (self.posxy0[0] < 1010 and self.posxy0[0] > 780 and self.posxy0[1] < 775 and self.posxy0[1] > 710 and self.iniciarsesion==False and self.vecespulsadasflag==False):
           self.buzzer()
           #self.ui.stackedWidget.setCurrentIndex(2)
           #self.ui.iniciorapido.setStyleSheet("\n""background-image: url(3 - Boton Inicio rapido.png);")
           #self.numpagina = 2
           #self.bloqueodepaginas(self.numpagina)
           self.cartelsecundario = 1
           self.bloqueoporcarteliniciorapido = 0
           self.ui.cartel.raise_()
           self.ui.confirmar.raise_()
           self.ui.cancelar.raise_()
           self.ui.cancelar_2.raise_()
           self.ui.textocartel.raise_()

           self.ui.cartel.show()
           self.ui.confirmar.show()
           self.ui.cancelar.show()
           self.ui.cancelar_2.show()
           self.ui.textocartel.show()






       ########################### FUNCION PARA DETENER SESION ####################################################
        #el self.iniciarsesion==true es para que si la persona enciende el equipo y se le ocurre apretar finzalizar, lo ignore.


       if (self.posxy0[0] < 1010 and self.posxy0[0] > 780 and self.posxy0[1] < 775 and self.posxy0[1] > 710 and self.pausarsesion == 0 and (self.pause == False or self.vecespulsadasfinalizar==0) and ( self.vecespulsadasflag==True or self.iniciarsesion==True ) )or (self.posxy0[0] < 110 and self.posxy0[0] > 10 and self.posxy0[1] < 110 and self.posxy0[1] > 20 and self.pausarsesion == 0 and (self.pause == False or self.vecespulsadasfinalizar==0) and  (self.iniciarsesion==True or self.vecespulsadasflag==True) ) :
           #self.ui.detiene1.setStyleSheet("background-image: url(Trabajando finalizar instancia.png);")
           self.bloquearpotencia()
           self.timercab.stop()
           packet2 = bytearray()
           packet2.append(11)
           packet2.append(0)
           packet2.append(0)
           packet2.append(0)
           packet2.append(0)
           puertoserie.write(packet2)

           sleep(0.1)

           packet9 = bytearray()
           packet9.append(5)
           packet9.append(0)
           packet9.append(0)
           packet9.append(0)
           packet9.append(0)
           puertoserie.write(packet9)

           self.pausarsesion = 0
           #self.detenersesion()
           if self.auxiliar==0 and ( self.vecespulsadasflag==True or self.iniciarsesion ==True):
                self.vecespulsadasfinalizar+=1
                self.ui.texto_iniciar.setText("pausado")
                self.pause=True
                self.bloqueoporcarteliniciorapido=0
                self.ui.cartel.raise_()
                self.ui.confirmar.raise_()
                self.ui.cancelar.raise_()
                self.ui.cancelar_2.raise_()
                self.ui.textocartel.raise_()

                self.ui.cartel.show()
                self.ui.confirmar.show()
                self.ui.cancelar.show()
                self.ui.cancelar_2.show()
                self.ui.textocartel.show()

                self.buzzer3()





       # regreso a paginas anteriores
       if self.posxy15[0] < 110 and self.posxy15[0] > 10 and self.posxy15[1] < 110 and self.posxy15[1] > 20:
           self.buzzer()
           self.ui.encabezado_menu_config.setStyleSheet("background-image: url(encabezado instancia.png);")


       if self.posxy10[0] < 110 and self.posxy10[0] > 10 and self.posxy10[1] < 110 and self.posxy10[1] > 20:
           self.buzzer()
           self.ui.encabezadoactividad.setStyleSheet("background-image: url(encabezado instancia.png);")



       if self.posxy13[0] < 110 and self.posxy13[0] > 10 and self.posxy13[1] < 110 and self.posxy13[1] > 20:
           self.ui.encabezadoperfil_2.setStyleSheet("background-image: url(encabezado instancia.png);")
           self.cursor_buzzer=0
           #self.ui.stackedWidget.setCurrentIndex()  #estoy en pagina de seleccion de sexo y voy a la de menu
           #self.numpagina = 15
           #self.bloqueodepaginas(self.numpagina)
           self.buzzer()

       if self.posxy3[0] < 110 and self.posxy3[0] > 10 and self.posxy3[1] < 110 and self.posxy3[1] > 20:
           self.buzzer()
           self.ui.encabezadosexo.setStyleSheet("background-image: url(encabezado instancia.png);")
           #self.ui.texto_iniciorapidoencabezado_2.hide()


       if self.posxy0[0] < 110 and self.posxy0[0] > 10 and self.posxy0[1] < 110 and self.posxy0[1] > 20 and self.iniciarsesion==False and self.vecespulsadasflag==False:
           self.buzzer()
           self.ui.encabezado_iniciorapido.setStyleSheet("background-image: url(encabezado instancia.png);")
           self.activarvacio=0
           self.habilitarpemf=0
           self.activarradio=0



       if self.posxy2[0] < 110 and self.posxy2[0] > 10 and self.posxy2[1] < 110 and self.posxy2[1] > 20:
           self.buzzer()
           self.ui.encabezado_menu.setStyleSheet("background-image: url(encabezado instancia.png);")

           #self.ui.texto_iniciorapidoencabezado_2.hide()
           #self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 35, 196, 60))

       if self.posxy11[0] < 110 and self.posxy11[0] > 10 and self.posxy11[1] < 110 and self.posxy11[1] > 20:

           self.buzzer()
           self.ui.encabezadoperfil.setStyleSheet("background-image: url(encabezado instancia.png);")
           self.activarconfig=0
           #self.activarperfil=0




       if self.posxy4[0] < 110 and self.posxy4[0] > 10 and self.posxy4[1] < 110 and self.posxy4[1] > 20 and self.bloqueoregresopagina==0:
           self.buzzer()
           self.ui.encabezadoselecciontrat.setStyleSheet("background-image: url(encabezado instancia.png);")
           self.ui.selfemenino.setStyleSheet("background-image: url(9 - Seleccion genero femenino.png);")





       if self.posxy6[0] < 110 and self.posxy6[0] > 10 and self.posxy6[1] < 110 and self.posxy6[1] > 20 and self.bloqueoregresopagina==0:
           self.buzzer()
           self.ui.encabezadoselecciontrat_2.setStyleSheet("background-image: url(encabezado instancia.png);")
           self.ui.selmasculino.setStyleSheet("background-image: url(9 - Seleccion genero masculino.png);")


       if self.posxy2[0] < 1250 and self.posxy2[0] > 650 and self.posxy2[1] < 550 and self.posxy2[1] > 350:
           self.cargardatosentabla()


       if self.posxy5[0] < 110 and self.posxy5[0] > 10 and self.posxy5[1] < 110 and self.posxy5[1] > 20 and self.flagzonatratamientosmujer == 1:
           self.buzzer()
           self.ui.encabezadotratatmujer.setStyleSheet("background-image: url(encabezado instancia.png);")



       if self.posxy5[0] < 110 and self.posxy5[0] > 10 and self.posxy5[1] < 110 and self.posxy5[1] > 20 and self.flagzonatratamientoshombre == 1:
           self.buzzer()
           self.ui.encabezadotratatmujer.setStyleSheet("background-image: url(encabezado instancia.png);")



       if self.posxy7[0] < 110 and self.posxy7[0] > 10 and self.posxy7[1] < 110 and self.posxy7[1] > 20 and self.flagzonatratamientosmujer == 1:
           self.buzzer()
           self.ui.encabezadotratamientomujer2.setStyleSheet("background-image: url(encabezado instancia.png);")



       if self.posxy7[0] < 110 and self.posxy7[0] > 10 and self.posxy7[1] < 110 and self.posxy7[1] > 20 and self.flagzonatratamientoshombre== 1:
           self.buzzer()
           self.ui.encabezadotratamientomujer2.setStyleSheet("background-image: url(encabezado instancia.png);")


       if self.posxy8[0] < 110 and self.posxy8[0] > 10 and self.posxy8[1] < 110 and self.posxy8[1] > 20 and self.flagzonatratamientosmujer == 1:
           self.buzzer()
           self.ui.encabezadotratamientomujer2_2.setStyleSheet("background-image: url(encabezado instancia.png);")


       if self.posxy8[0] < 110 and self.posxy8[0] > 10 and self.posxy8[1] < 110 and self.posxy8[1] > 20 and self.flagzonatratamientoshombre == 1:
           self.buzzer()
           self.ui.encabezadotratamientomujer2_2.setStyleSheet("background-image: url(encabezado instancia.png);")


       if self.posxy9[0] < 110 and self.posxy9[0] > 10 and self.posxy9[1] < 110 and self.posxy9[1] > 20 and self.flagzonatratamientosmujer == 1:
           self.buzzer()
           self.ui.encabezadotratamientomujer2_3.setStyleSheet("background-image: url(encabezado instancia.png);")



       if self.posxy9[0] < 110 and self.posxy9[0] > 10 and self.posxy9[1] < 110 and self.posxy9[1] > 20 and self.flagzonatratamientoshombre == 1:
           self.buzzer()
           self.ui.encabezadotratamientomujer2_3.setStyleSheet("background-image: url(encabezado instancia.png);")




   def emularirdeiniciorapidoainicio(self):
       #self.buzzer()
       self.activarvacio = 0
       self.habilitarpemf = 0
       self.activarradio = 0

       self.ui.iniciorapido.setStyleSheet("background-image: url(3 - Boton Inicio rapido.png);")
       self.ui.selfemenino.setStyleSheet("background-image: url(9 - Seleccion genero femenino.png);")
       self.ui.selmasculino.setStyleSheet("background-image: url(9 - Seleccion genero masculino.png);")
       self.ui.selecciontratamiento.setStyleSheet("background-image: url(3 - Boton seleccionar tratamiento.png);")
       self.ui.encabezado_iniciorapido.setStyleSheet("background-image: url(Inicio encabezado.png);")
       self.ui.stackedWidget.setCurrentIndex(2)  # estoy en pagina de inicio rapido y voy a la de menu - regreso
       self.ui.pulssubetratamiento.setEnabled(True)
       self.ui.pulsbajatratamiento.setEnabled(True)
       self.ui.pulssubetratamiento.setStyleSheet(
           "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
       self.ui.pulsbajatratamiento.setStyleSheet(
           "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
       self.numpagina = 2
       self.bloqueodepaginas(self.numpagina)
       self.resetearfrecuencias()



   ########################### FUNCION PARA SELECCIONAR TRATAMIENTO : funciona en conconrdancia con la de seleccionartratamientoinstancia() para la seleccion de zona y la animacion




   def seleccionartratamiento(self,x4,y4):

       if (x4 < 310 and x4 > 260 and y4 < 460 and y4 > 410 or x4 < 500 and x4 > 450 and y4 < 460 and y4 > 410) and self.bloqueozona==0:    #se ilumina la zona del BRAZO y se muestra el cartel de aceptar o cancelar
           self.buzzer()
           if self.flagzonatratamientosmujer==1:
              self.ui.zonasmujerespalda.setStyleSheet("background-image: url(14 - Mujer instancias espalda  BRAZOS.png);")
              self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente instancias.png);")
           if self.flagzonatratamientoshombre==1:
              self.ui.zonashombreespalda.setStyleSheet("background-image: url(13 - Hombre instancias espalda  BRAZOS.png);")
              self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente instancias.png);")
           #self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="brazos post"
           self.ui.textozonas2_encabezado.setText("zona brazos posteriores")



       if x4 < 430 and x4 > 310 and y4 < 450 and y4 > 360 and self.bloqueozona==0:     #se ilumina la zona del ESCAPULAR y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(14 - Mujer instancias espalda  ESCAPULA.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente instancias.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(13 - Hombre instancias espalda  ESCAPULA.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente instancias.png);")
           #self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="escapular"
           self.ui.textozonas2_encabezado.setText("zona escapular")



       if x4 < 450 and x4 > 290 and y4 < 510 and y4 > 450 and self.bloqueozona==0:     #se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet( "background-image: url(14 - Mujer instancias espalda  FLANCO.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente instancias.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(13 - Hombre instancias espalda  FLANCO.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente instancias.png);")
           #self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="flancos"
           self.ui.textozonas2_encabezado.setText("zona flancos")



       if x4 < 590 and x4 > 300 and y4 < 620 and y4 > 545 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(14 - Mujer instancias espalda  GLUTEOS.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente instancias.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(13 - Hombre instancias espalda  GLUTEO.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente instancias.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="gluteos"
           self.ui.textozonas3_encabezado.setText("zona gluteos")


       if (x4 < 295 and x4 > 280 and y4 < 695 and y4 > 620  or x4 < 490  and x4 > 460 and y4 < 700 and y4 > 610) and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet( "background-image: url(14 - Mujer instancias espalda  TRONCATERIANA.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente instancias.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(13 - Hombre instancias espalda  TRONCATERIANA.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente instancias.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="trocanteriana"
           self.ui.textozonas2_encabezado.setText("zona trocanteriana")



       if x4 < 430 and x4 > 315 and y4 < 730 and y4 > 630 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(14 - Mujer instancias espalda  MUSLO POST.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente instancias.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(13 - Hombre instancias espalda  MUSLO POST.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente instancias.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="muslos post"
           self.ui.textozonas2_encabezado.setText("zona muslos posteriores")





       if x4 < 940 and x4 > 870 and y4 < 260 and y4 > 180 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.buzzer()
           self.eleccion = "rostro"

           self.ui.textozonas1_encabezado.setText("zona rostro")
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente ROSTRO.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente ROSTRO.png);")




       if x4 < 940 and x4 > 880 and y4 < 320 and y4 > 285 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet( "background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente CUELLO.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente CUELLO.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="cuello"
           self.ui.textozonas4_encabezado.setText("zona cuello")


       if x4 < 980 and x4 > 830 and y4 < 400 and y4 > 330 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente ESCOTE.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente ESCOTE);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion="escote"
           self.ui.textozonas4_encabezado.setText("zona escote")




       if (x4 < 840 and x4 > 790 and y4 < 460 and y4 > 390  or x4 < 1080 and x4 > 980 and y4 < 460 and y4 > 390) and self.bloqueozona==0 :  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente BRAZO.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente BRAZO.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion = "brazos ant"
           self.ui.textozonas2_encabezado.setText("zona brazos anteriores")


       if x4 < 950 and x4 > 860 and y4 < 550 and y4 > 430 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente ABDOMEN.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente ABDOMEN.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion = "abdomen"
           self.ui.textozonas2_encabezado.setText("zona abdomen")


       if (x4 < 880 and x4 > 830 and y4 < 725 and y4 > 560 or x4 < 990 and x4 > 940 and y4 < 725 and y4 > 560) and self.bloqueozona==0  :  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente MUSLO ANT.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente MUSLO ANT.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion = "muslos ant"
           self.ui.textozonas2_encabezado.setText("zona muslos anteriores")


       if x4 < 940 and x4 > 900 and y4 < 710 and y4 > 630 and self.bloqueozona==0:  # se ilumina la zona del FLANCO y se muestra el cartel de aceptar o cancelar, ademas se setean los valores de frecuencia, potencia, cabezal, etc
           self.buzzer()
           if self.flagzonatratamientosmujer == 1:
               self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda instancias.png);")
               self.ui.zonasmujerfrente.setStyleSheet("background-image: url(14 - Mujer instancias frente MUSLO INT.png);")
           if self.flagzonatratamientoshombre == 1:
               self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda instancias.png);")
               self.ui.zonashombrefrente.setStyleSheet("background-image: url(13 - Hombre instancias frente MUSLO INT.png);")
           # self.ui.cartelzona2.setText('<font color="red">inicio rapido<font>')
           self.eleccion = "muslos int"
           self.ui.textozonas2_encabezado.setText("zona muslos internos")



       if x4< 730 and x4> 640 and y4 < 480 and y4 > 430:    #pulsador de aceptar

           self.buzzer()
           if self.eleccion == "rostro":
               self.ui.stackedWidget.setCurrentIndex(5)  # pagina actual: seleccion de tratamiento, pagina anterior: seleccion de zona a tratar
               self.numpagina = 5
               self.bloqueodepaginas(self.numpagina)


           if self.eleccion == "abdomen" or self.eleccion=="brazos ant" or self.eleccion=="muslos ant" or self.eleccion=="muslos int" or self.eleccion=="flancos" or self.eleccion=="trocanteriana" or self.eleccion=="brazos post" or self.eleccion=="escapular"  or self.eleccion=="muslos post":
               self.ui.stackedWidget.setCurrentIndex(7)  # pagina actual: seleccion de tratamiento, pagina anterior: seleccion de zona a tratar
               self.numpagina = 7
               self.bloqueodepaginas(self.numpagina)

           if self.eleccion == "cuello" or self.eleccion == "escote":
               self.ui.stackedWidget.setCurrentIndex(9)  # pagina actual: seleccion de tratamiento, pagina anterior: seleccion de zona a tratar
               self.numpagina = 9
               self.bloqueodepaginas(self.numpagina)


           if self.eleccion == "gluteos":
               self.ui.stackedWidget.setCurrentIndex(8)  # pagina actual: seleccion de tratamiento, pagina anterior: seleccion de zona a tratar
               self.numpagina = 8
               self.bloqueodepaginas(self.numpagina)


           self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda.png);")
           self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente.png);")
           self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda.png);")
           self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente.png);")
           self.quitarcartelemergente()
           self.resetearfrecuencias()
           self.bloqueozona=0



       if x4< 630 and x4> 550 and y4 < 480 and y4 > 430:     #pulsador de cancelar
           self.ui.zonasmujerespalda.setStyleSheet("background-image: url(12 - zona a tratar mujer espalda.png);")
           self.ui.zonasmujerfrente.setStyleSheet("background-image: url(12 - zona a tratar mujer frente.png);")
           self.ui.zonashombreespalda.setStyleSheet("background-image: url(11 - zona a tratar hombre espalda.png);")
           self.ui.zonashombrefrente.setStyleSheet("background-image: url(11 - zona a tratar hombre frente.png);")
           self.quitarcartelemergente()
           self.bloqueozona = 0
           self.buzzer()




#   definicionseteos de funciones para elegir el tratamiento


   def setearvalorestratamiento(self, objeto):
       self.setearfrecuencia(objeto.frecuenciaseleccionada)
       if objeto.cabezalseleccionado==1 or objeto.cabezalseleccionado==2 or objeto.cabezalseleccionado==4:
           self.cabezalbipolarseguridad = False
           self.ui.f2desac.hide()
           self.ui.f3desac.hide()
           self.ui.f4desact.hide()
       if objeto.cabezalseleccionado==3:
           self.cabezalbipolarseguridad = True
           self.ui.f2desac.raise_()
           self.ui.f3desac.raise_()
           self.ui.f4desact.raise_()
           self.ui.f2desac.show()
           self.ui.f3desac.show()
           self.ui.f4desact.show()

       self.valorpotencia = objeto.niveldepotencia
       self.cabezal(objeto.cabezalseleccionado)
       self.setearreloj(objeto.tiempo)
       self.inhibirresolverfrec = 0
       self.setearfrecuencia(objeto.frecuenciaseleccionada)
       self.ui.potencia.setText(str(self.valorpotencia) + '%')
       self.bloquear_animaciones = 1
       self.activarradio=0
       self.activarradiofrecuencia()
       self.bloquear_animaciones=1
       if objeto.vacio==0:
          self.activarvacio=1
          self.activarvacum()

       if objeto.vacio==1:
          self.activarvacio=0
          self.activarvacum()
       self.bloquear_animaciones = 1
       if objeto.pemf==0:
          self.habilitarpemf=1
          self.activarpemf()
       if objeto.pemf==1:
          self.habilitarpemf=0
          self.activarpemf()
       self.bloquear_animaciones = 1
       if objeto.laser==0:
          self.habilitarlaser=1
          self.activarlaser()

       if objeto.laser==1:
          self.habilitarlaser=0
          self.activarlaser()
       self.contadorvacio = objeto.pv
       self.contadorpemf = objeto.pp

       self.modificar_pemf_durantetratamiento(objeto.pp)
       self.modificar_vacio_durantetratamiento(objeto.pv,objeto.niveldevacio)
       self.animarlabel3()


       if self.iniciarsesion==True: #and self.activarradio==1:
           self.enviardatosdesesion()
       #self.buzzer()




   ########################### FUNCION PARA CARTEL DE DETENER SESION Y PAUSAR  ####################################################

   def confirmardetener2(self):

       self.guardarperfilnombre=1
       if self.cartelsecundario==0:

          self.vecespulsadasflag = False
          self.bloqueoporcarteliniciorapido=1
          self.auxiliar=1
          self.detenersesion()
          self.emularirdeiniciorapidoainicio()

       if self.cartelsecundario == 1:
          self.cartelsecundario=0

          self.ui.stackedWidget.setCurrentIndex(2)
          self.ui.iniciorapido.setStyleSheet("\n""background-image: url(3 - Boton Inicio rapido.png);")
          self.numpagina = 2
          self.bloqueodepaginas(self.numpagina)
          self.cartelsecundario = 0
          self.bloqueoporcarteliniciorapido = 1
          self.ui.cartel.hide()
          self.ui.confirmar.hide()
          self.ui.cancelar.hide()
          self.ui.cancelar_2.hide()
          self.ui.textocartel.hide()

          self.resetearfrecuencias()
          self.inhibirresolverfrec = 0
          self.deshabilitar_buzzer = 1
          self.bloquear_animaciones = 1
          self.activarpemf()
          self.bloquear_animaciones = 1
          self.activarvacum()
          self.bloquear_animaciones = 1
          self.activarradiofrecuencia()
          self.bloquear_animaciones = 1
          self.activarlaser()
          self.inicializar()
          self.deshabilitar_buzzer = 0


   def confirmardetener(self):

       self.guardarperfilnombre = 0
       if self.cartelsecundario==0:
          self.vecespulsadasflag = False
          self.bloqueoporcarteliniciorapido=1
          self.auxiliar=1
          self.detenersesion()
          self.emularirdeiniciorapidoainicio()
       if self.cartelsecundario == 1:
          self.cartelsecundario=0

          self.ui.stackedWidget.setCurrentIndex(2)
          self.ui.iniciorapido.setStyleSheet("\n""background-image: url(3 - Boton Inicio rapido.png);")
          self.numpagina = 2
          self.bloqueodepaginas(self.numpagina)
          self.cartelsecundario = 0
          self.bloqueoporcarteliniciorapido = 1
          self.ui.cartel.hide()
          self.ui.confirmar.hide()
          self.ui.cancelar.hide()
          self.ui.cancelar_2.hide()
          self.ui.textocartel.hide()

          self.resetearfrecuencias()
          self.inhibirresolverfrec = 0
          self.deshabilitar_buzzer = 1
          self.bloquear_animaciones = 1
          self.activarpemf()
          self.bloquear_animaciones = 1
          self.activarvacum()
          self.bloquear_animaciones = 1
          self.activarradiofrecuencia()
          self.bloquear_animaciones = 1
          self.activarlaser()
          self.inicializar()
          self.deshabilitar_buzzer = 0
       if self.guardarperfilnombre == 0:
           self.ui.texto_iniciorapidoencabezado_2.hide()
           self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 40, 196, 60))
           self.nombre = "casual"


   def cancelardetener(self):


    if self.cartelsecundario==0:
       self.vecespulsadasfinalizar += 1
       if self.vecespulsadasfinalizar==1:
          self.vecespulsadas=1
          self.ui.texto_iniciar.setText("pausar")
          self.ui.label_23.setStyleSheet("background-image: url(Icono Pausar.png);")
          self.ui.label_23.setGeometry(QtCore.QRect(1060, 727, 27, 41))
          self.bloqueoporcarteliniciorapido=1
          self.auxiliar=1
          self.desbloquearpotencia()
          self.comenzarsesion()
          self.animacioncabezalmultitec()
       if self.vecespulsadasfinalizar == 2:
           self.iniciarsesion=False
           self.vecespulsadasfinalizar = 0
           self.vecespulsadas = 0
           self.ui.texto_iniciar.setText("continuar")
           self.ui.label_23.setStyleSheet("background-image: url(Icono Iniciar.png);")
           self.ui.label_23.setGeometry(QtCore.QRect(1060, 727, 21, 41))
           self.bloqueoporcarteliniciorapido = 1
           self.ui.cartel.hide()
           self.ui.confirmar.hide()
           self.ui.cancelar.hide()
           self.ui.cancelar_2.hide()

           self.ui.textocartel.hide()

    if self.cartelsecundario == 1:
               self.cartelsecundario =0
               self.bloqueoporcarteliniciorapido = 1
               self.ui.cartel.hide()
               self.ui.confirmar.hide()
               self.ui.cancelar.hide()
               self.ui.cancelar_2.hide()
               self.ui.textocartel.hide()





           ########################### FUNCIONES PARA SELECCION DE FRECUENCIAS ####################################################


# esta funcion se ejecuta solo cuando se elige tratamiento y no inicio rapido. Tambien se ejecuta cuando se elige un perfil
   def setearfrecuencia(self, frecuenciaelegida):
       self.resetearfrecuencias()
       if frecuenciaelegida==8:
           self.setearfrecuenciaf1()
       if frecuenciaelegida==4:
           self.setearfrecuenciaf2()
       if frecuenciaelegida==2:
           self.setearfrecuenciaf3()
       if frecuenciaelegida==1:
           self.setearfrecuenciaf4()
       if frecuenciaelegida==12:
           self.setearfrecuenciaf1()
           self.setearfrecuenciaf2()
       if frecuenciaelegida==15:
           self.setearfrecuenciaf1()
           self.setearfrecuenciaf2()
           self.setearfrecuenciaf3()
           self.setearfrecuenciaf4()
       if frecuenciaelegida==14:
           self.setearfrecuenciaf1()
           self.setearfrecuenciaf2()
           self.setearfrecuenciaf3()
       if frecuenciaelegida==7:
           self.setearfrecuenciaf2()
           self.setearfrecuenciaf3()
           self.setearfrecuenciaf4()
       if frecuenciaelegida==3:
           self.setearfrecuenciaf3()
           self.setearfrecuenciaf4()
       if frecuenciaelegida == 6:
           self.setearfrecuenciaf2()
           self.setearfrecuenciaf3()
       self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
       self.inhibirresolverfrec = 0



# llama a la funcion setearfrecuencia
   def frecuencia1(self):
       self.setearfrecuenciaf1()
       if self.inhibirresolverfrec==0:
          self.resolverfrec()

   def frecuencia2(self):
       self.setearfrecuenciaf2()
       if self.inhibirresolverfrec == 0:
           self.resolverfrec()


   def frecuencia3(self):
       self.setearfrecuenciaf3()
       if self.inhibirresolverfrec == 0:
           self.resolverfrec()


   def frecuencia4(self):
       self.setearfrecuenciaf4()
       if self.inhibirresolverfrec == 0:
           self.resolverfrec()






# se encarga de la lógica de resolucion de frecuencias
   def resolverfrec(self):
       self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
       if self.sumafrec == 10 or self.sumafrec == 11 or self.sumafrec == 9:
           self.v2 = 4
           self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
           self.setearfrecuenciaf2()


       if self.sumafrec == 5 or self.sumafrec == 13 or self.sumafrec == 9:
           self.v3 = 2

           self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4
           self.setearfrecuenciaf3()
       if self.iniciarsesion == True: # and self.activarradio==1:
           self.prioridadenviodatossesion=1
           self.enviardatosdesesion()



# se ejecuta antes de ir a inicio rapido o al momento de aceptar un tratamiento, lo que hace es dejar la frecuencias reseteadas, todas en cero, para luego setear las que corresponda
   def resetearfrecuencias(self):
       self.inhibirresolverfrec = 1
       self.v5 = 1
       self.v6 = 1
       self.v7 = 1
       self.v8 = 1
       self.frecuencia1()
       self.frecuencia2()
       self.frecuencia3()
       self.frecuencia4()
       self.v1 = 0
       self.v2 = 0
       self.v3 = 0
       self.v4 = 0
       self.sumafrec = self.v1 + self.v2 + self.v3 + self.v4



   # setea las frecuencias
   def setearfrecuenciaf1(self):
       self.v1 = 8
       if self.v5 == 0:
           self.ui.f1.setStyleSheet("background-image: url(Boton frecuencia activo.png);")
       if self.v5 == 1 and self.sumafrec != 8:
           self.ui.f1.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.v1 = 0
       self.v5 = not self.v5

   def setearfrecuenciaf2(self):
       self.v2 = 4
       if self.v6 == 0:
           self.ui.f2.setStyleSheet("background-image: url(Boton frecuencia activo.png);")
       if self.v6 == 1 and self.sumafrec != 4:
           self.ui.f2.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.v2 = 0
       self.v6 = not self.v6

   def setearfrecuenciaf3(self):
       self.v3 = 2
       if self.v7 == 0:
           self.ui.f3.setStyleSheet("background-image: url(Boton frecuencia activo.png);")
       if self.v7 == 1 and self.sumafrec != 2:
           self.ui.f3.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.v3 = 0
       self.v7 = not self.v7

   def setearfrecuenciaf4(self):
       self.v4 = 1
       if self.v8 == 0:
           self.ui.f4.setStyleSheet("background-image: url(Boton frecuencia activo.png);")
       if self.v8 == 1 and self.sumafrec != 1:
           self.ui.f4.setStyleSheet("background-image: url(Boton frecuencia inactivo.png);")
           self.v4 = 0
       self.v8 = not self.v8






########################### FUNCIONES PARA SELECCION DE CABEZALES ####################################################

   def cabezal(self, cabezalseleccionado):
       self.cabezalactivo=cabezalseleccionado

       if self.iniciarsesion == True: # and self.activarradio==1:

           self.prioridadenviodatossesion = 1
           self.enviardatosdesesion()

       if self.cabezalactivo==1:
          self.cabezalelegido = "corporal multi tec"
          self.ui.cabezal1.setStyleSheet("border-image: url(Cabezal Grande.png);\n"
                                      "background-image: url(trasnp.png);")
          self.ui.cabezal2.setStyleSheet("border-image: url(6 - Trabajando cabezal 2 inactivo.png);\n"
                                        "background-image: url(trasnp.png);")
          self.ui.cabezal3.setStyleSheet("border-image: url(6 - Trabajando cabezal 3 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")
          self.ui.cabezal4.setStyleSheet("border-image: url(6 - Trabajando cabezal 4 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")

       if self.cabezalactivo==2:
          self.cabezalelegido = "corporal multi"
          self.ui.cabezal1.setStyleSheet("border-image: url(Cabezal Grande inactivo.png);\n"
                                      "background-image: url(trasnp.png);")
          self.ui.cabezal2.setStyleSheet("border-image: url(5 - Trabajando cabezal 2.png);\n"
                                         "background-image: url(trasnp.png);")

          self.ui.cabezal3.setStyleSheet("border-image: url(6 - Trabajando cabezal 3 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")
          self.ui.cabezal4.setStyleSheet("border-image: url(6 - Trabajando cabezal 4 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")

       if self.cabezalactivo == 3:
          self.cabezalelegido = "facial bipolar"
          self.ui.cabezal1.setStyleSheet("border-image: url(Cabezal Grande inactivo.png);\n"
                                        "background-image: url(trasnp.png);")
          self.ui.cabezal2.setStyleSheet("border-image: url(6 - Trabajando cabezal 2 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")

          self.ui.cabezal3.setStyleSheet("border-image: url(5 - Trabajando cabezal 3.png);\n"
                                         "background-image: url(trasnp.png);")
          self.ui.cabezal4.setStyleSheet("border-image: url(6 - Trabajando cabezal 4 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")





       if self.cabezalactivo == 4:

          self.cabezalelegido = "facial multi"
          self.ui.cabezal1.setStyleSheet("border-image: url(Cabezal Grande inactivo.png);\n"
                                         "background-image: url(trasnp.png);")
          self.ui.cabezal2.setStyleSheet("border-image: url(6 - Trabajando cabezal 2 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")

          self.ui.cabezal3.setStyleSheet("border-image: url(6 - Trabajando cabezal 3 inactivo.png);\n"
                                         "background-image: url(trasnp.png);")
          self.ui.cabezal4.setStyleSheet("border-image: url(5 - Trabajando cabezal 4.png);\n"
                                         "background-image: url(trasnp.png);")







########################### FUNCIONES PARA COMENZAR SESION ####################################################

   def comenzarsesion(self):
       self.pause = False
       self.pausarsesion=0

       #self.ui.detiene1.setStyleSheet("background-image: url(5 - Trabajando finalizar.png);")
       self.iniciarsesion = True
       self.seteosesion = False
       self.prioridadenviodatossesion = 1
       self.enviardatosdesesionpemf()
       sleep(0.1)
       self.enviardatosdesesion()

       if self.auxiliar == 1:
           self.ui.cartel.hide()
           self.ui.confirmar.hide()
           self.ui.cancelar.hide()
           self.ui.cancelar_2.hide()
           self.ui.textocartel.hide()

       self.auxiliar = 0

########################### FUNCION PARA FINALIZAR SESION ####################################################

   def detenervaciolaserpemf(self):
       packet9 = bytearray()
       packet9.append(5)
       packet9.append(0)
       packet9.append(0)
       packet9.append(0)
       packet9.append(0)
       puertoserie.write(packet9)
       sleep(0.1)
       puertoserie.write(packet9)


   def detenersesion(self):
       self.detenervaciolaserpemf()
       if self.auxiliar==1:
          self.frecuenciahistorial()
          self.agregarpersona()
          self.cargardatosentabla()
          self.resetearreloj()
          self.id = 0


          self.ui.pulssubetiempo.setStyleSheet("background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
          self.ui.pulsbajatiempo.setStyleSheet("background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
          self.ui.label_23.setGeometry(QtCore.QRect(1060, 727, 21, 41))
          self.ui.label_23.setStyleSheet("background-image: url(Icono Iniciar.png);")
          if self.guardarperfilnombre==0:
             self.ui.texto_iniciorapidoencabezado_2.hide()
             self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 40, 196, 60))
             self.nombre="casual"

          self.ui.pulsbajatiempo.setEnabled(True)
          self.ui.pulssubetiempo.setEnabled(True)
          self.seteosesion = True
          self.iniciarsesion=False
          self.ui.cartel.hide()
          self.ui.confirmar.hide()
          self.ui.cancelar.hide()
          self.ui.cancelar_2.hide()
          self.ui.textocartel.hide()

          self.ui.texto_iniciar.setText("iniciar")
          self.vecespulsadas=0
          #self.ui.label_23.setStyleSheet("background-image: url(Icono Iniciar.png);")
          #self.ui.texto_finalizar.setText('<font color="grey">finalizar<font>')
          #self.ui.label_24.setStyleSheet("background-image: url(Icono Finalizar instancia.png);")
       packet2 = bytearray()
       packet2.append(11)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       packet2.append(0)
       puertoserie.write(packet2)
       self.habilitarcontrol = False





########################### FUNCION PARA ENVIAR PARAMETROS DE SESION AL MICRO ####################################################

   def enviardatosdesesion(self):

       self.timerest1.stop()
       self.timerest2.stop()
       self.prioridadenviodatossesion = 1
       if self.pausarsesion==0:# and self.activarradio==1:
          self.seteosesion = False
          packet1 = bytearray()
          packet1.append(9)
          packet1.append(self.valorpotencia*self.activarradio)
          packet1.append(self.sumafrec*self.activarradio)
          packet1.append(self.cabezalactivo*self.activarradio)
          packet1.append(self.frio*self.activarradio)
          puertoserie.write(packet1)
          #print(self.sumafrec)
          #print(self.valorpotencia)
          #print(self.cabezalactivo)
          #print(self.frio)
          #print(packet1)
          #print(self.activarradio)
          self.prioridadenviodatossesion = 0
          self.limpiarbuffer()
          self.timerest1.start()
          self.timerest2.start()


   ########################### FUNCION PARA LIMPIAR EL BUFFER ####################################################

   def limpiarbuffer(self):
       puertoserie.flushInput()
       puertoserie.flushOutput()


   def frecuenciahistorial(self):
       if self.sumafrec == 8:
           self.frecuenciaelegida = "1.3mhz"
       if self.sumafrec == 4:
           self.frecuenciaelegida = "1.0mhz"
       if self.sumafrec == 2:
           self.frecuenciaelegida = "0.8mhz"
       if self.sumafrec == 1:
           self.frecuenciaelegida = "0.6mhz"
       if self.sumafrec == 12:
           self.frecuenciaelegida = "1.3mhz-1.0mhz"
       if self.sumafrec == 6:
           self.frecuenciaelegida = "1.0mhz-0.8mhz"
       if self.sumafrec == 3:
           self.frecuenciaelegida = "0.6mhz -0.8mhz"
       if self.sumafrec == 14:
           self.frecuenciaelegida = "1.3- 1.0 -0.8 mhz"
       if self.sumafrec == 7:
           self.frecuenciaelegida = "0.6 -0.8 -1.0 mhz"
       if self.sumafrec == 15:
           self.frecuenciaelegida = "todas"
       if self.activarradio==0:
           self.frecuenciaelegida = "desactivada"



   def animacioncabezalmultitec(self):
       if self.iniciarsesion == True:
         if self.cabezalactivo==2 or  self.cabezalactivo==3 or self.cabezalactivo==4:
           self.ui.cabezal1.setStyleSheet("border-image: url(Cabezal Grande 2 plano.png);\n"
                                          "background-image: url(trasnp.png);")
           self.timercab.timeout.connect(lambda: self.animarpulsadores(self.ui.cabezal1, 970, 540, 962, 532, 67, 148))
           self.timercab.stop()
           self.timercab.start(2000)

   ########################### FUNCIONES PARA INCREMENTAR Y DECREMENTAR RELOJ ####################################################

   def incrementarreloj(self):
       self.buzzer()
       self.aux1 = self.aux1 + 1
       if self.aux1 > 60:
           self.aux1 = 60
       self.minute = str(self.aux1)
       if self.aux1 < 10:
           self.ui.seteotiempo.setText('0' + self.minute + ':' + self.second)
       else:
           self.ui.seteotiempo.setText(self.minute + ':' + self.second)
       self.minuto = self.aux1
       self.animarpulsadores(self.ui.pulssubetiempo, 1045, 305, 1037, 297, 76, 57)
       self.animarlabel2(self.ui.seteotiempo, 30, 40)

   def decrementarreloj(self):
       self.buzzer()
       self.aux1 = self.aux1 - 1
       if self.aux1 < 2:
           self.aux1 = 1
       self.minute = str(self.aux1)
       if self.aux1 < 10:
           self.ui.seteotiempo.setText('0' + self.minute + ':' + self.second)
       else:
           self.ui.seteotiempo.setText(self.minute + ':' + self.second)
       self.minuto = self.aux1
       self.animarpulsadores(self.ui.pulsbajatiempo, 1145, 305, 1137, 297, 76, 57)
       self.animarlabel2(self.ui.seteotiempo, 30, 40)


   #### seleeciona entre tratamientos en la pantalla de inicio rapido durante la sesion

   def subetratamiento(self):
       self.buzzer()
       self.contadortratamiento = self.contadortratamiento + 1
       self.resetearfrecuencias()
       self.seleccionrapidatratamiento()
       self.animarpulsadores(self.ui.pulssubetratamiento, 1045, 175, 1037, 167, 76, 57)


   def bajatratamiento(self):
       self.buzzer()
       self.contadortratamiento = self.contadortratamiento - 1
       self.resetearfrecuencias()
       self.seleccionrapidatratamiento()
       self.animarpulsadores(self.ui.pulsbajatratamiento, 1145, 175,1137, 167, 76, 57)


#setea tiempo de sesion solo en el caso de seleccion de tratamiento

   def setearreloj(self,tiempodesesion):
     if self.iniciarsesion==False:
       self.aux1=tiempodesesion
       if self.aux1 > 60:
           self.aux1 = 60
       if self.aux1 < 0:
           self.aux1 = 0
       self.minute = str(self.aux1)
       if self.aux1 < 10:
           self.ui.seteotiempo.setText('0' + self.minute + ':' + self.second)
       else:
           self.ui.seteotiempo.setText(self.minute + ':' + self.second)
       self.minuto = self.aux1



#se encarga del manejo de las paginas
   def bloqueodepaginas(self, pagina):  #1: habilitada, 0: bloqueada
       for i in range(18):
           self.bloqueopaginas[i]=0
       self.bloqueopaginas[pagina]=1



#resetea el reloj a fin de dejarlo listo para una proxima sesion
   def resetearreloj(self):
           self.iniciarsesion = False
           self.segundo=60
           self.minutosesion='00'
           self.segundosesion='00'
           self.minuto=self.aux1
           text = self.minutosesion + ':' + self.segundosesion
           self.ui.tiemporeloj.setText(text)



   def adquirirfecha(self):
       self.now = datetime.now()
       self.current_time = self.now.strftime("%d-%m-%Y")

   def instanciawifi(self):

       self.ui.pushButtonwifi.setStyleSheet("background-image: url(4 - Boton configuracion instancia.png);\n"
                                            "border-image: url(trasnp.png);")


   def pantallawifi(self):
       self.buzzer()
       self.ui.pushButtonwifi.setStyleSheet("background-image: url(3 - Boton configuracion.png);\n"
                                         "border-image: url(trasnp.png);")


       sleep(0.1)
       self.ui.stackedWidget.setCurrentIndex(13)  # estoy en la pantalla de menu y voy a la de configuracion
       self.numpagina = 13
       self.bloqueodepaginas(self.numpagina)
       self.comprobarconexion()


########################################################## PANTALLA DE ACTIVIDAD #########################################################

   def agregarpersona(self):
       if self.activarvacio==0:
          self.vacio="desactivado"
       if self.habilitarpemf == 0:
           self.pemf = "desactivado"
       if self.habilitarlaser == 0:
           self.laser = "desactivado"
       if self.activarvacio == 1:
           self.vacio = self.ui.label_12.text()
       if self.habilitarpemf == 1:
           self.pemf = str(self.formaonda) +" - "+ self.ui.label_13.text()
           #self.pemf = "programa "+str(self.contadorpemf)
       if self.habilitarlaser == 1:
           self.laser = "activado"
       self.adquirirfecha()

       self.agregaractividad(self.nombre,self.genero,self.eleccion,self.tratamientoelegido, str(self.valorpotencia)+"%",self.frecuenciaelegida, self.cabezalelegido,self.vacio,self.laser,self.pemf,str(self.minuto)+"min",str(self.current_time))



   def agregaractividad(self, nombre, genero, zona, tratamiento, potencia, frecuencia, cabezal, niveldevacio,laser,pemf,duracion,fecha):
       connection = sql.connect('actividad.db')
       cur = connection.cursor()
       instruccion = '''INSERT INTO historial (nombre, genero, zona, tratamiento, potencia,frecuencia, cabezal,niveldevacio,laser,pemf,duracion,fecha) 
            VALUES('{}', '{}','{}', '{}','{}','{}', '{}','{}', '{}','{}', '{}','{}')'''.format(nombre, genero, zona, tratamiento,potencia, frecuencia, cabezal,niveldevacio,laser,pemf,duracion,fecha)
       cur.execute(instruccion)
       connection.commit()
       connection.close()

   def paginaatras(self,nombres):
       self.ui.pulsiguiente.setEnabled(True)
       self.pagina_actual -= 1
       self.pagina_anterior -= 1
       if self.pagina_actual<1:
           self.pagina_actual=1
       if self.pagina_anterior<0:
           self.pagina_anterior=0
       connection = sql.connect('actividad.db')
       cur = connection.cursor()
       if self.infoadicionalflag == 0:
           instruccion = f'SELECT * FROM historial ORDER BY id DESC'
       else:
           instruccion = "SELECT * FROM historial WHERE nombre = '{}'".format(nombres)
       cur.execute(instruccion)
       resultado = cur.fetchall()
       connection.commit()
       longitud = len(resultado)
       if longitud<200:
           self.paginastotales=1
       if longitud > 200 and longitud < 400:
           self.paginastotales = 2
       if longitud > 400:
           self.paginastotales = (longitud // 200) +1
       self.ui.paginaactual.setText("página " + str(self.pagina_actual) + " de " + str(self.paginastotales))

       if self.infoadicionalflag == 0:
           instruccion = f"SELECT * FROM historial ORDER BY id DESC LIMIT 200 OFFSET {self.pagina_anterior * 200}"
       else:
           instruccion = "SELECT * FROM historial WHERE nombre = '{}' ORDER BY id DESC LIMIT 200 OFFSET {}".format(nombres, self.pagina_anterior * 200)
       cur.execute(instruccion)
       resultado = cur.fetchall()


       connection.commit()
       connection.close()
       self.cargardatosentabla2(resultado)


   def paginasiguiente(self,nombres):
       self.pagina_actual+=1
       self.pagina_anterior+=1

       connection = sql.connect('actividad.db')
       cur = connection.cursor()
       if self.infoadicionalflag==0:
          instruccion = f'SELECT * FROM historial ORDER BY id DESC'
       else:
          instruccion = "SELECT * FROM historial WHERE nombre = '{}'".format(nombres)
       cur.execute(instruccion)
       resultado = cur.fetchall()
       connection.commit()
       longitud=len(resultado)
       if longitud<200:
           self.paginastotales=1
       if longitud>200 and longitud<400:
           self.paginastotales=2
       if longitud>400:
           self.paginastotales=(longitud//200) +1
       if self.pagina_actual>=self.paginastotales:
           self.pagina_actual=self.paginastotales
           self.ui.pulsiguiente.setEnabled(False)
       self.ui.paginaactual.setText("página " +str(self.pagina_actual) + " de " + str(self.paginastotales))
       if self.infoadicionalflag==0:
          instruccion = f"SELECT * FROM historial ORDER BY id DESC LIMIT 200 OFFSET {self.pagina_anterior*200}"
       else:
           instruccion = "SELECT * FROM historial WHERE nombre = '{}' ORDER BY id DESC LIMIT 200 OFFSET {}".format(nombres, self.pagina_anterior * 200)
       cur.execute(instruccion)
       resultado = cur.fetchall()
       connection.commit()
       connection.close()

       self.cargardatosentabla2(resultado)

   def cargardatosentabla2(self,datos):
       i = len(datos)
       self.ui.tableWidget.setRowCount(i)
       tablerow = 0
       for row in datos:
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[0])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 0, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[1])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 1, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[2])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 2, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[3])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 3, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[4])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 4, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[5])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 5, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[6])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 6, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[7])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 7, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[8])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 8, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[9])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 9, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[10])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 10, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[11])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 11, self.oneitem)

           tablerow += 1

   def cargardatosentabla(self):
       self.infoadicionalflag=0
       connection = sql.connect('actividad.db')
       cur = connection.cursor()

       instruccion = f'SELECT * FROM historial ORDER BY id DESC'
       cur.execute(instruccion)
       resultado = cur.fetchall()
       connection.commit()
       longitud = len(resultado)
       if longitud<200:
           self.paginastotales=1
       if longitud > 200 and longitud < 400:
           self.paginastotales = 2
       if longitud > 400:
           self.paginastotales = (longitud // 200) + 1
       self.ui.paginaactual.setText("página " + str(self.pagina_actual) + " de " + str(self.paginastotales))

       instruccion = f"SELECT * FROM historial ORDER BY id DESC LIMIT 200 OFFSET {self.pagina_anterior * 200}"
       #instruccion = f'SELECT * FROM historial ORDER BY id DESC'
       cur.execute(instruccion)
       datospersona = cur.fetchall()
       connection.commit()
       connection.close()
       i = len(datospersona)
       if i>199:
           #self.eliminar_historial()
           self.ui.pulsiguiente.setEnabled(True)
           self.ui.pulsatras.setEnabled(True)



       self.ui.tableWidget.setRowCount(i)
       tablerow = 0
       for row in datospersona:
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[0])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 0, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[1])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 1, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[2])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 2, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[3])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 3, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[4])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 4, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[5])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 5, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[6])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 6, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[7])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 7, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[8])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 8, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[9])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 9, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[10])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 10, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[11])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 11, self.oneitem)

           tablerow += 1

   def on_button_pressed(self):
       self.buzzer()
       self.counter = 0
       self.timerpulsador.start(1000)

   def on_button_released(self):
       self.timerpulsador.stop()
       self.counter = 0


   def on_timer_timeout(self):
       self.counter += 1
       if self.counter>3:
           self.counter = 0
           self.eliminar_historial2()





   def eliminar_historial2(self):

       try:

           connection = sql.connect('actividad.db')
           cur = connection.cursor()
           instruccion = "DELETE FROM historial WHERE 1"
           cur.execute(instruccion)
           resultado = cur.rowcount
           connection.commit()
           connection.close()
           self.cargardatosentabla()
       except:
           self.auxiliar10=1

   def eliminar_historial(self):

       try:
           connection = sql.connect('actividad.db')
           cur = connection.cursor()
           instruccion = "DELETE FROM historial WHERE rowid IN (SELECT rowid FROM historial LIMIT 50)"
           cur.execute(instruccion)
           resultado = cur.rowcount
           connection.commit()
           connection.close()

       except:
           self.auxiliar10=1

   def habilitarentradadedatos(self):

       self.ui.pushButtonagregar.setEnabled(True)
       self.ui.pushButtoninfo.setEnabled(False)
       self.ui.pushButtoneliminar.setEnabled(False)
       self.ui.pushButtonseleccionar.setEnabled(False)
       self.ui.deseleccionarperfil.setEnabled(False)
       self.ui.pushButtoncrear.setEnabled(False)

       self.deshabilitar_buzzer_perfil=1
       self.ui.tecladoencabezado.show()
       self.ui.numero0.show()
       self.ui.numero1.show()
       self.ui.numero2.show()
       self.ui.numero3.show()
       self.ui.numero4.show()
       self.ui.numero5.show()
       self.ui.numero6.show()
       self.ui.numero7.show()
       self.ui.numero8.show()
       self.ui.numero9.show()
       self.ui.arroba.show()
       self.ui.teclapunto.show()
       self.ui.letraw.show()
       self.ui.teclaborrar.show()
       self.ui.letram.show()
       self.ui.teclaescape.show()
       self.ui.letrah.show()
       self.ui.letraz.show()
       self.ui.letraa.show()
       self.ui.letrad.show()
       self.ui.letral.show()
       self.ui.letraq.show()
       self.ui.teclamayus.raise_()
       self.ui.teclamayus.show()
       self.ui.letraj.show()
       self.ui.teclaespacio.show()
       self.ui.letrac.show()
       self.ui.letrae.show()
       self.ui.letray.show()
       self.ui.letrar.show()
       self.ui.letras.show()
       self.ui.letrao.show()
       self.ui.letrai.show()
       self.ui.letrav.show()
       self.ui.letrax.show()
       self.ui.letrak.show()
       self.ui.letrap.show()
       self.ui.letran.show()
       self.ui.letrab.show()
       self.ui.letrau.show()
       self.ui.letraf.show()
       self.ui.letrag.show()
       self.ui.letrat.show()
       self.ui.tecladoencabezado.raise_()
       self.ui.numero0.raise_()
       self.ui.numero1.raise_()
       self.ui.numero2.raise_()
       self.ui.numero3.raise_()
       self.ui.numero4.raise_()
       self.ui.numero5.raise_()
       self.ui.numero6.raise_()
       self.ui.numero7.raise_()
       self.ui.numero8.raise_()
       self.ui.numero9.raise_()
       self.ui.arroba.raise_()
       self.ui.teclapunto.raise_()
       self.ui.letraw.raise_()
       self.ui.teclaborrar.raise_()
       self.ui.letram.raise_()
       self.ui.teclaescape.raise_()
       self.ui.letrah.raise_()
       self.ui.letraz.raise_()
       self.ui.letraa.raise_()
       self.ui.letrad.raise_()
       self.ui.letral.raise_()
       self.ui.letraq.raise_()
       self.ui.letraj.raise_()
       self.ui.teclaespacio.raise_()
       self.ui.letrac.raise_()
       self.ui.letrae.raise_()
       self.ui.letray.raise_()
       self.ui.letrar.raise_()
       self.ui.letras.raise_()
       self.ui.letrao.raise_()
       self.ui.letrai.raise_()
       self.ui.letrav.raise_()
       self.ui.letrax.raise_()
       self.ui.letrak.raise_()
       self.ui.letrap.raise_()
       self.ui.letran.raise_()
       self.ui.letrab.raise_()
       self.ui.letrau.raise_()
       self.ui.letraf.raise_()
       self.ui.letrag.raise_()
       self.ui.letrat.raise_()
       self.ui.teclamayus.raise_()
       self.ui.shift.raise_()
       self.ui.teclamayus.show()

       self.ui.shift.show()
       self.ui.lineEditnombre.setEnabled(True)
       self.ui.lineEditdireccion.setEnabled(True)
       self.ui.lineEditdni.setEnabled(True)
       self.ui.lineEditcorreo.setEnabled(True)




       self.ui.lineEditnombre.setText("pulse y escriba para modificar")
       self.ui.lineEditdni.setText("pulse y escriba para modificar")
       self.ui.lineEditdireccion.setText("pulse y escriba para modificar")
       self.ui.lineEditcorreo.setText("pulse y escriba para modificar")
       self.ui.lineEditnombre.setFocus()
       self.ui.pushButtoncrear.setEnabled(False)
       self.deshabilitar_buzzer_perfil=0
       self.cursor_buzzer=1

   def habilitarentradadedatos2(self):

       self.ui.tecladoencabezado_2.show()
       self.ui.numero0_2.show()
       self.ui.numero1_2.show()
       self.ui.numero2_2.show()
       self.ui.numero3_2.show()
       self.ui.numero4_2.show()
       self.ui.numero5_2.show()
       self.ui.numero6_2.show()
       self.ui.numero7_2.show()
       self.ui.numero8_2.show()
       self.ui.numero9_2.show()
       self.ui.arroba_2.show()
       self.ui.teclapunto_2.show()
       self.ui.letraw_2.show()
       self.ui.teclaborrar_2.show()
       self.ui.letram_2.show()
       self.ui.teclaescape_2.show()
       self.ui.letrah_2.show()
       self.ui.letraz_2.show()
       self.ui.letraa_2.show()
       self.ui.letrad_2.show()
       self.ui.letral_2.show()
       self.ui.letraq_2.show()
       self.ui.teclamayus_2.raise_()

       self.ui.teclamayus_2.show()
       self.ui.letraj_2.show()
       self.ui.teclaespacio_2.show()
       self.ui.letrac_2.show()
       self.ui.letrae_2.show()
       self.ui.letray_2.show()
       self.ui.letrar_2.show()
       self.ui.letras_2.show()
       self.ui.letrao_2.show()
       self.ui.letrai_2.show()
       self.ui.letrav_2.show()
       self.ui.letrax_2.show()
       self.ui.letrak_2.show()
       self.ui.letrap_2.show()
       self.ui.letran_2.show()
       self.ui.letrab_2.show()
       self.ui.letrau_2.show()
       self.ui.letraf_2.show()
       self.ui.letrag_2.show()
       self.ui.letrat_2.show()
       self.ui.tecladoencabezado_2.raise_()
       self.ui.numero0_2.raise_()
       self.ui.numero1_2.raise_()
       self.ui.numero2_2.raise_()
       self.ui.numero3_2.raise_()
       self.ui.numero4_2.raise_()
       self.ui.numero5_2.raise_()
       self.ui.numero6_2.raise_()
       self.ui.numero7_2.raise_()
       self.ui.numero8_2.raise_()
       self.ui.numero9_2.raise_()
       self.ui.arroba_2.raise_()
       self.ui.teclapunto_2.raise_()
       self.ui.letraw_2.raise_()
       self.ui.teclaborrar_2.raise_()
       self.ui.letram_2.raise_()
       self.ui.teclaescape_2.raise_()
       self.ui.letrah_2.raise_()
       self.ui.letraz_2.raise_()
       self.ui.letraa_2.raise_()
       self.ui.letrad_2.raise_()
       self.ui.letral_2.raise_()
       self.ui.letraq_2.raise_()
       self.ui.letraj_2.raise_()
       self.ui.teclaespacio_2.raise_()
       self.ui.letrac_2.raise_()
       self.ui.letrae_2.raise_()
       self.ui.letray_2.raise_()
       self.ui.letrar_2.raise_()
       self.ui.letras_2.raise_()
       self.ui.letrao_2.raise_()
       self.ui.letrai_2.raise_()
       self.ui.letrav_2.raise_()
       self.ui.letrax_2.raise_()
       self.ui.letrak_2.raise_()
       self.ui.letrap_2.raise_()
       self.ui.letran_2.raise_()
       self.ui.letrab_2.raise_()
       self.ui.letrau_2.raise_()
       self.ui.letraf_2.raise_()
       self.ui.letrag_2.raise_()
       self.ui.letrat_2.raise_()
       self.ui.teclamayus_2.raise_()
       self.ui.teclamayus_2.show()
       self.ui.tecla_shift.raise_()
       self.ui.tecla_shift.show()
       self.cursor_buzzer = 1

   def adddatosperfil(self):
     self.cursor_buzzer=0

     self.buzzer()
     self.nombreperfil = self.ui.lineEditnombre.text()
     self.dni = self.ui.lineEditdni.text()
     if (self.nombreperfil != "pulse y escriba para modificar" and self.dni != "pulse y escriba para modificar"):
       self.ui.pushButtoncrear.setEnabled(True)
       self.ui.pushButtonagregar.setEnabled(False)
       self.ui.lineEditnombre.setEnabled(False)
       self.ui.lineEditdireccion.setEnabled(False)
       self.ui.lineEditdni.setEnabled(False)
       self.ui.lineEditcorreo.setEnabled(False)

       self.ui.lineEditnombre.setText("            ")
       self.ui.lineEditnombre.setFocus()


       self.ui.lineEditdni.setText("           ")
       self.ui.lineEditdni.setFocus()

       self.direccion = self.ui.lineEditdireccion.text()
       self.ui.lineEditdireccion.setText("          ")
       self.ui.lineEditdireccion.setFocus()

       self.correo = self.ui.lineEditcorreo.text()
       self.ui.lineEditcorreo.setText("           ")
       self.ui.lineEditcorreo.setFocus()

       self.guardarperfil(str(self.nombreperfil), str(self.dni), str(self.direccion), str(self.correo))
       self.ui.pushButtonagregar.setEnabled(False)
       self.resetarentradadatos()
       self.ui.pushButtonagregar.setEnabled(False)
     else:
           #self.ui.pushButtonagregar.setEnabled(False)
           #self.quitarteclado()
           self.cartelerrorcampos()



   def cartelerrorcampos(self):
       msgBox12 = QMessageBox()
       msgBox12.setIcon(QMessageBox.Critical)
       msgBox12.setWindowFlags(Qt.FramelessWindowHint)
       msgBox12.setStyleSheet("QPushButton{ width:75px; font-size: 18px; }")
       msgBox12.setStyleSheet("background-image: url(fondoactividad.png);" )
       msgBox12.setFont(QtGui.QFont('Myriad Pro Cond', 15))
       msgBox12.setText("Los campos nombre y dni son obligatorios")
       msgBox12.setWindowTitle("ERROR:")
       msgBox12.setStandardButtons(QMessageBox.Ok)
       returnValue = msgBox12.exec()
       #if returnValue == QMessageBox.Ok:
           #self.reconocererror()





   def guardarperfil(self, nombre, dni, direccion, correo):
       connection = sql.connect('perfilesvr.db')
       cur = connection.cursor()
       instruccion = '''INSERT INTO perfiles (nombre, dni, direccion, correo) 
         VALUES('{}', '{}','{}', '{}')'''.format(nombre, dni, direccion, correo)
       cur.execute(instruccion)
       connection.commit()
       connection.close()
       self.cargardatosenlista()


   def cargardatosenlista(self):
       try:
           self.ui.listWidget.clear()
           connection = sql.connect('perfilesvr.db')
           cur = connection.cursor()
           instruccion = f'SELECT * FROM perfiles ORDER BY nombre DESC'
           tablerow = 0
           results = cur.execute(instruccion)
           for row in results:
               self.ui.listWidget.addItem(str(row[0]))
       except:
           self.variable1 = 0


   def informacionadicional(self):
       self.infoadicional=1
       self.buzzer()

       try:
           self.nombre = str(self.ui.listWidget.currentItem().text())
           self.busca_persona(self.nombre)

       except:
           self.variable1 = 0


   def seleccionarnombreperfil(self):
        self.buzzer()
        try:

            self.nombre = str(self.ui.listWidget.currentItem().text())
            self.sehabilitoperfil=1
            self.guardarperfilnombre=1
            self.ui.texto_iniciorapidoencabezado_2.raise_()
            self.ui.texto_iniciorapidoencabezado_2.show()
            self.ui.texto_iniciorapidoencabezado.setGeometry(QtCore.QRect(245, 20, 196, 60))
            self.ui.texto_iniciorapidoencabezado_2.setGeometry(QtCore.QRect(245, 65, 196, 60))
            self.ui.texto_iniciorapidoencabezado_2.setText("perfil: "+self.nombre)
            self.animarpulsadorestransicion(self.ui.pushButtonseleccionar, 285, 295, 280, 290, 221, 57,1)


        except:
            self.variable1 = 0

   def deseleccionarnombreperfil(self):
       self.buzzer()
       try:
           self.nombre = "casual"
           self.sehabilitoperfil = 0
           self.guardarperfilnombre = 0



       except:
           self.variable1 = 0


   def busca_persona(self, nombres):
       self.pagina_actual=1
       self.pagina_anterior=0
       self.infoadicionalflag=1
       connection = sql.connect('actividad.db')
       cur = connection.cursor()
       instruccion = "SELECT * FROM historial WHERE nombre = '{}'".format(nombres)
       cur.execute(instruccion)
       datospersona = cur.fetchall()
       connection.commit()
       #connection.close()
       longitud = len(datospersona)
       if longitud<200:
           self.paginastotales=1
       if longitud > 200 and longitud < 400:
           self.paginastotales = 2
       if longitud > 400:
           self.paginastotales = (longitud // 200) + 1
       self.ui.paginaactual.setText("página " + str(self.pagina_actual) + " de " + str(self.paginastotales))


       instruccion = "SELECT * FROM historial WHERE nombre = '{}' ORDER BY id DESC LIMIT 200 OFFSET {}".format(nombres, self.pagina_anterior * 200)
       cur.execute(instruccion)
       datospersona = cur.fetchall()
       connection.commit()
       connection.close()
       i = len(datospersona)
       if i > 199:
           # self.eliminar_historial()
           self.ui.pulsiguiente.setEnabled(True)
           self.ui.pulsatras.setEnabled(True)


       self.ui.tableWidget.setRowCount(i)
       tablerow = 0

       for row in datospersona:
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[0])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 0, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[1])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 1, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[2])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 2, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[3])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 3, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[4])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 4, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[5])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 5, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[6])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 6, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[7])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 7, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[8])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 8, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[9])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 9, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[10])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 10, self.oneitem)

           self.oneitem = QTableWidgetItem(QTableWidgetItem(str(row[11])))
           self.oneitem.setTextAlignment(QtCore.Qt.AlignCenter)
           self.oneitem.setForeground(brush)
           self.ui.tableWidget.setItem(tablerow, 11, self.oneitem)

           tablerow += 1


   def eliminarperfil(self):
       self.buzzer()
       try:
           self.personaaeliminar = str(self.ui.listWidget.currentItem().text())
           self.eliminar_persona(self.personaaeliminar)
       except:
           self.variable1 = 1

   def eliminar_persona(self, nombres):
       try:
           connection = sql.connect('perfilesvr.db')
           cur = connection.cursor()
           instruccion = "DELETE FROM perfiles WHERE nombre = '{}'".format(nombres)
           cur.execute(instruccion)
           resultado = cur.rowcount
           connection.commit()
           connection.close()
           # if resp == None:
           # self.ui.borrar_ok.setText("NO EXISTE")
           # elif resp == 0:
           # self.ui.borrar_ok.setText("NO EXISTE")

           # else:
           # self.ui.borrar_ok.setText("SE ELIMINO")
           self.cargardatosenlista()

           self.ui.pushButtoneliminar.setEnabled(False)
           self.ui.pushButtonseleccionar.setEnabled(False)
           self.ui.pushButtoninfo.setEnabled(False)
           self.ui.deseleccionarperfil.setEnabled(False)

       except:
           self.auxiliar10=1



   #teclado

   def resetarentradadatos(self):
       self.datos1 = ""
       self.datos2 = ""
       self.datos3 = ""
       self.datos4 = ""
       self.datos5 = ""
       self.datos6 = ""
       self.ui.lineEditnombre.clear()
       self.ui.lineEditdni.clear()
       self.ui.lineEditdireccion.clear()
       self.ui.lineEditcorreo.clear()
       self.ui.lineEditpass_2.clear()
       self.ui.lineEditnombre.setText("                                   ")
       self.ui.lineEditdni.setText("                                   ")
       self.ui.lineEditdireccion.setText("                                   ")
       self.ui.lineEditcorreo.setText("                                   ")
       self.ui.lineEditpass_2.setText("                                   ")
       self.quitarteclado()



   def quitarteclado2(self):
       self.bitshift=0
       self.ui.tecladoencabezado_2.setStyleSheet("background-image: url(teclado_minuscula.png);")
       self.ui.tecla_shift.hide()
       self.ui.letraw_2.hide()
       self.ui.teclaborrar_2.hide()
       self.ui.letram_2.hide()
       self.ui.letrah_2.hide()
       self.ui.letraz_2.hide()
       self.ui.letraa_2.hide()
       self.ui.letrad_2.hide()
       self.ui.letral_2.hide()
       self.ui.letraq_2.hide()
       self.ui.teclamayus_2.hide()
       self.ui.letraj_2.hide()
       self.ui.teclaespacio_2.hide()
       self.ui.letrac_2.hide()
       self.ui.letrae_2.hide()
       self.ui.letray_2.hide()
       self.ui.letrar_2.hide()
       self.ui.letras_2.hide()
       self.ui.letrao_2.hide()
       self.ui.letras_2.hide()
       self.ui.letrav_2.hide()
       self.ui.letrax_2.hide()
       self.ui.letrak_2.hide()
       self.ui.letrap_2.hide()
       self.ui.letran_2.hide()
       self.ui.letrab_2.hide()
       self.ui.letrau_2.hide()
       self.ui.letraf_2.hide()
       self.ui.letrag_2.hide()
       self.ui.letrat_2.hide()
       self.ui.numero0_2.hide()
       self.ui.numero1_2.hide()
       self.ui.numero2_2.hide()
       self.ui.numero3_2.hide()
       self.ui.numero4_2.hide()
       self.ui.numero5_2.hide()
       self.ui.numero6_2.hide()
       self.ui.numero7_2.hide()
       self.ui.numero8_2.hide()
       self.ui.numero9_2.hide()
       self.ui.letrai_2.hide()
       self.ui.arroba_2.hide()
       self.ui.teclapunto_2.hide()
       self.ui.teclaescape_2.hide()
       self.ui.tecladoencabezado_2.hide()

   def quitarteclado(self):
       self.ui.tecladoencabezado.setStyleSheet("background-image: url(teclado_minuscula.png);")
       self.bitshift=0
       self.datos1 = ""
       self.datos2 = ""
       self.datos3 = ""
       self.datos4 = ""
       self.ui.pushButtoncrear.setEnabled(True)
       self.ui.lineEditnombre.setEnabled(False)
       self.ui.lineEditdireccion.setEnabled(False)
       self.ui.lineEditdni.setEnabled(False)
       self.ui.lineEditcorreo.setEnabled(False)
       self.ui.pushButtonagregar.setEnabled(False)
       self.ui.letraw.hide()
       self.ui.teclaborrar.hide()
       self.ui.shift.hide()
       self.ui.letram.hide()
       self.ui.letrah.hide()
       self.ui.letraz.hide()
       self.ui.letraa.hide()
       self.ui.letrad.hide()
       self.ui.letral.hide()
       self.ui.letraq.hide()
       self.ui.teclamayus.hide()
       self.ui.letraj.hide()
       self.ui.teclaespacio.hide()
       self.ui.letrac.hide()
       self.ui.letrae.hide()
       self.ui.letray.hide()
       self.ui.letrar.hide()
       self.ui.letras.hide()
       self.ui.letrao.hide()
       self.ui.letrai.hide()
       self.ui.letrav.hide()
       self.ui.letrax.hide()
       self.ui.letrak.hide()
       self.ui.letrap.hide()
       self.ui.letran.hide()
       self.ui.letrab.hide()
       self.ui.letrau.hide()
       self.ui.letraf.hide()
       self.ui.letrag.hide()
       self.ui.letrat.hide()
       self.ui.numero0.hide()
       self.ui.numero1.hide()
       self.ui.numero2.hide()
       self.ui.numero3.hide()
       self.ui.numero4.hide()
       self.ui.numero5.hide()
       self.ui.numero6.hide()
       self.ui.numero7.hide()
       self.ui.numero8.hide()
       self.ui.numero9.hide()
       self.ui.arroba.hide()
       self.ui.teclapunto.hide()
       self.ui.teclaescape.hide()
       self.ui.tecladoencabezado.hide()

   def habilitarentradadedatosintermedio(self):

       self.habilitarentradadedatos()
       self.habilitar_linea5()


   def habilitarentradadedatosintermedio2(self):
       self.habilitarentradadedatos2()
       self.habilitar_linea6()


   def borrarentrada(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.habilitar1 == 1:
           self.ui.lineEditnombre.backspace()
           self.datos1 = self.ui.lineEditnombre.text()
           self.ui.lineEditnombre.setText(self.datos1)
           #self.ui.lineEditnombre.clear()
           #self.ui.lineEditnombre.setText("                                   ")
           #self.datos1 = ""

       if self.habilitar2 == 1:
           self.ui.lineEditdni.backspace()
           self.datos2 = self.ui.lineEditdni.text()
           self.ui.lineEditdni.setText(self.datos2)
           #self.ui.lineEditdni.clear()
           #self.ui.lineEditdni.setText("                                   ")
           #self.datos2 = ""

       if self.habilitar3 == 1:
           self.ui.lineEditdireccion.backspace()
           self.datos3 = self.ui.lineEditdireccion.text()
           self.ui.lineEditdireccion.setText(self.datos3)
           #self.ui.lineEditdireccion.clear()
           #self.ui.lineEditdireccion.setText("                                   ")
           #self.datos3 = ""

       if self.habilitar4 == 1:
           self.ui.lineEditcorreo.backspace()
           self.datos4 = self.ui.lineEditcorreo.text()
           self.ui.lineEditcorreo.setText(self.datos4)
           #self.ui.lineEditcorreo.clear()
           #self.ui.lineEditcorreo.setText("                                   ")
           #self.datos4 = ""



       if self.habilitar6 == 1:
           self.ui.lineEditpass_2.backspace()
           self.datos6 = self.ui.lineEditpass_2.text()
           self.ui.lineEditpass_2.setText(self.datos6)
           #self.ui.lineEditpass_2.clear()
           #self.ui.lineEditpass_2.setText("                                   ")
           #self.datos6 = ""

   def habilitar_linea1(self):

       #if self.deshabilitar_buzzer_perfil==0:
           #self.buzzer()

       #self.ui.lineEditnombre.setStyleSheet("background-image: url(blanco.png); color: white;")
       self.habilitar1 = 1
       self.habilitar2 = 0
       self.habilitar3 = 0
       self.habilitar4 = 0


   def habilitar_linea2(self):
       #if self.deshabilitar_buzzer_perfil==0:
           #self.buzzer()

       self.habilitar1 = 0
       self.habilitar2 = 1
       self.habilitar3 = 0
       self.habilitar4 = 0

   def habilitar_linea3(self):
       #if self.deshabilitar_buzzer_perfil==0:
           #self.buzzer()

       self.habilitar1 = 0
       self.habilitar2 = 0
       self.habilitar3 = 1
       self.habilitar4 = 0

   def habilitar_linea4(self):
       #if self.deshabilitar_buzzer_perfil==0:
          # self.buzzer()

       self.habilitar1 = 0
       self.habilitar2 = 0
       self.habilitar3 = 0
       self.habilitar4 = 1

   def habilitar_linea5(self):

       self.habilitar5 = 1
       self.habilitar6=0


   def habilitar_linea6(self):

       self.habilitar5 = 0
       self.habilitar6 = 1



   def funcionshift1(self,tecla):
     self.buzzer()
     self.fondotecla(tecla)
     self.bitshift= not self.bitshift
     if self.bitshift==1:
        self.ui.tecladoencabezado.setStyleSheet("background-image: url(teclado_minuscula2.png);")
     else:
        self.ui.tecladoencabezado.setStyleSheet("background-image: url(teclado_minuscula.png);")



   def funcionshift2(self,tecla):
     self.buzzer()
     self.fondotecla(tecla)
     self.bitshift= not self.bitshift
     if self.bitshift==1:
        self.ui.tecladoencabezado_2.setStyleSheet("background-image: url(teclado_minuscula2.png);")
     else:
        self.ui.tecladoencabezado_2.setStyleSheet("background-image: url(teclado_minuscula.png);")


   def mayuscula(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift==0:
          self.cambiominuscula=not self.cambiominuscula

          if self.cambiominuscula==0:
              #self.ui.teclamayus_2.setStyleSheet("background-image: url(trasnp.png);\n"
                                           #   "border-image: url(trasnp.png);")
              #self.ui.teclamayus.setStyleSheet("background-image: url(trasnp.png);\n"
                                               #  "border-image: url(trasnp.png);")
              self.ui.tecladoencabezado_2.setStyleSheet("background-image: url(teclado_minuscula.png);")
              self.ui.tecladoencabezado.setStyleSheet("background-image: url(teclado_minuscula.png);")


          if self.cambiominuscula==1:
             # self.ui.teclamayus_2.setStyleSheet("background-image: url(Teclado icono mayuscula infactivo.png);\n"
                                            #  "border-image: url(Teclado icono mayuscula inactivo.png);")
             # self.ui.teclamayus.setStyleSheet("background-image: url(Teclado icono mayusfcula inactivo.png);\n"
                                               #  "border-image: url(Teclado icono mayuscula inactivo.png);")
              self.ui.tecladoencabezado_2.setStyleSheet("background-image: url(teclado_mayuscula.png);")
              self.ui.tecladoencabezado.setStyleSheet("background-image: url(teclado_mayuscula.png);")
       else:
           self.dato = ".com"
           self.agregarletra()




   def teclaespaciadora(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = " "
       self.agregarletra()

   def letraQ(self,tecla):

       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift==0:
          self.dato = "q"
       else:
          self.dato = "!"
       self.agregarletra()

   def letraW(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "w"
       else:
           self.dato = '"'
       self.agregarletra()


   def letraE(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "e"
       else:
           self.dato = "#"
       self.agregarletra()

   def letraR(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "r"
       else:
           self.dato = "$"
       self.agregarletra()

   def letraT(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "t"
       else:
           self.dato = "%"
       self.agregarletra()

   def letraY(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "y"
       else:
           self.dato = "&"
       self.agregarletra()


   def letraU(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "u"
       else:
           self.dato = "'"
       self.agregarletra()

   def letraI(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "i"
       else:
           self.dato = "("
       self.agregarletra()

   def letraO(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "o"
       else:
           self.dato = ")"
       self.agregarletra()

   def letraP(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "p"
       else:
           self.dato = "*"
       self.agregarletra()

   def letraA(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "a"
       else:
           self.dato = "+"
       self.agregarletra()

   def letraS(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "s"
       else:
           self.dato = ","
       self.agregarletra()

   def letraD(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "d"
       else:
           self.dato = "-"
       self.agregarletra()

   def letraF(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "f"
       else:
           self.dato = "_"
       self.agregarletra()

   def letraG(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "g"
       else:
           self.dato = "/"
       self.agregarletra()

   def letraH(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "h"
       else:
           self.dato = ":"
       self.agregarletra()

   def letraJ(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "j"
       else:
           self.dato = ":"
       self.agregarletra()

   def letraK(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "k"
       else:
           self.dato = "<"
       self.agregarletra()

   def letraL(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "l"
       else:
           self.dato = ">"
       self.agregarletra()

   def letraZ(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "z"
       else:
           self.dato = "?"
       self.agregarletra()

   def letraX(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "x"
       else:
           self.dato = "="
       self.agregarletra()

   def letraC(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "c"
       else:
           self.dato = "["
       self.agregarletra()

   def letraV(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "v"
       else:
           self.dato = "]"
       self.agregarletra()

   def letraB(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "b"
       else:
           self.dato = "{"
       self.agregarletra()

   def letraN(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "n"
       else:
           self.dato = "}"
       self.agregarletra()

   def letraM(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       if self.bitshift == 0:
           self.dato = "m"
       else:
           self.dato = "E"
       self.agregarletra()


   def fondotecla(self,tecla):
     if tecla==self.ui.teclaespacio_2 or tecla==self.ui.teclaespacio:
         tecla.setStyleSheet("background-image: url(Teclado tecla grande.png);\n"
                             "border-image: url(Teclado tecla grande.png);")
         tecla.setStyleSheet("background-image: url(Teclado tecla grande.png);\n"
                             "border-image: url(Teclado tecla grande.png);")
     else:

         tecla.setStyleSheet("background-image: url(Teclado tecla chica.png);\n"
                                     "border-image: url(Teclado tecla chica.png);")
         tecla.setStyleSheet("background-image: url(Teclado tecla chica.png);\n"
                                       "border-image: url(Teclado tecla chica.png);")

   def num0(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "0"
       self.agregarletra()

   def num1(self,tecla):

       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "1"
       self.agregarletra()

   def num2(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "2"
       self.agregarletra()

   def num3(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "3"
       self.agregarletra()

   def num4(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "4"
       self.agregarletra()

   def num5(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "5"
       self.agregarletra()

   def num6(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "6"
       self.agregarletra()

   def num7(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "7"
       self.agregarletra()

   def num8(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "8"
       self.agregarletra()

   def num9(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "9"
       self.agregarletra()

   def arroba(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "@"
       self.agregarletra()

   def punto(self,tecla):
       self.buzzer()
       self.fondotecla(tecla)
       self.dato = "."
       self.agregarletra()

   def agregarletra(self):
     self.cursor_buzzer=0
     self.deshabilitar_buzzer_perfil=1


     if self.activarperfil==1:
       if self.habilitar1 == 1:

           self.ui.pushButtoncrear.setEnabled(False)
           if self.cambiominuscula==1:
              self.datos1 += self.dato.upper()
           else:
              self.datos1 += self.dato

           self.ui.lineEditnombre.setText(self.datos1)
           self.texto1 = self.ui.lineEditnombre.text()
           self.ui.lineEditnombre.setCursorPosition(0)

           #self.verificarcamposcompletos()


       if self.habilitar2 == 1:
           self.ui.pushButtoncrear.setEnabled(False)
           if self.cambiominuscula == 1:
               self.datos2 += self.dato.upper()
           else:
               self.datos2 += self.dato
           self.ui.lineEditdni.setText(self.datos2)
           self.texto2 = self.ui.lineEditdni.text()
           self.ui.lineEditdni.setCursorPosition(0)
          # self.verificarcamposcompletos()

       if self.habilitar3 == 1:
           self.ui.pushButtoncrear.setEnabled(False)
           if self.cambiominuscula == 1:
               self.datos3 += self.dato.upper()
           else:
               self.datos3 += self.dato
           self.ui.lineEditdireccion.setText(self.datos3)
           self.texto3 = self.ui.lineEditdireccion.text()
           self.ui.lineEditdireccion.setCursorPosition(0)
           #self.verificarcamposcompletos()

       if self.habilitar4 == 1:
           self.ui.pushButtoncrear.setEnabled(False)
           if self.cambiominuscula == 1:
               self.datos4 += self.dato.upper()
           else:
               self.datos4 += self.dato
           self.ui.lineEditcorreo.setText(self.datos4)
           self.texto4 = self.ui.lineEditcorreo.text()
           self.ui.lineEditcorreo.setCursorPosition(0)
           #self.verificarcamposcompletos()

     if self.activarconfig==1:
         if self.habilitar5 == 1:
             if self.cambiominuscula == 1:
                 self.datos5 += self.dato.upper()
             else:
                 self.datos5 += self.dato



         if self.habilitar6 == 1:
             if self.cambiominuscula == 1:
                 self.datos6 += self.dato.upper()
             else:
                 self.datos6 += self.dato
             self.ui.lineEditpass_2.setText(self.datos6)
             self.ui.lineEditpass_2.setCursorPosition(0)
     self.deshabilitar_buzzer_perfil=0
     self.cursor_buzzer=1




   def escape(self):
       self.buzzer()
       self.quitarteclado()

   def escape2(self):
       self.buzzer()
       self.quitarteclado2()

   def verificarcamposcompletos(self):
       if self.texto1 != "" and self.texto2 != "" and self.texto3 != "" and self.texto4 != "":
           self.ui.pushButtonagregar.setEnabled(True)
       else:
           self.ui.pushButtonagregar.setEnabled(False)


   def iraselecciondesexo(self):
       self.animarpulsadores(self.ui.pushButtonseleccionar, 285, 295, 280, 290, 221, 57)
       self.ui.stackedWidget.setCurrentIndex(3)
       self.numpagina = 3
       self.bloqueodepaginas(self.numpagina)


   def actualizarredes(self):
       try:
           self.buzzer()
           self.ui.label_32.setText("buscando redes disponibles..")
           self.ui.stackedWidget.setCurrentIndex(12)  # estoy en la pantalla de menu y voy a la de configuracion
           self.numpagina = 12
           self.bloqueodepaginas(self.numpagina)
           self.timerwifi2.start(4000)

       except:
           self.auxiliar10 = 0


   def tomardatoswifi(self):
      self.buzzer()
      try:
        self.ui.label_32.setText("configurando red, aguarde un instante...")
        self.nombredered = self.ui.listWidget_2.currentItem().text()
        self.nombredered= self.nombredered[6:]
        self.contrasena = self.ui.lineEditpass_2.text()
        #self.ui.iconowifi.hide()
        #self.ui.iconowifi2.hide()
        #self.ui.mensajeestadowifi.setText("conectando...")
        self.ui.stackedWidget.setCurrentIndex(12)  # estoy en la pantalla de menu y voy a la de configuracion
        self.numpagina = 12
        self.bloqueodepaginas(self.numpagina)
        self.timerwifi.start(1000)
        #if self.nombredered != "" and self.contrasena != "":
        #else:
            #QMessageBox.information(self, "AVISO", "ingrese usuario y contraseña")
      except:
          self.auxiliar10=0
          #QMessageBox.information(self, "AVISO", "ingrese usuario y contraseña")
      #self.resetarentradadatos()

   def comprobarconexion(self):
        try:

            host = socket.gethostbyname("www.google.com")
            socket.create_connection((host, 80), 2)
            self.ui.iconowifi.raise_()
            self.ui.iconowifi.show()
            self.ui.iconowifi.setStyleSheet("background-image: url(WIFI tilde azul.png);\n"
                                         "border-image: url(WIFI tilde azul.png);")
            self.ui.iconowifi2.setStyleSheet("background-image: url(WIFI logo.png);\n"
            "border-image: url(WIFI logo.png);")
            self.ui.mensajeestadowifi.setText("conectado")
            self.wifiactivado=True
            result = subprocess.check_output(['iwgetid', '-r'])
            ssid = result.decode('utf-8').strip()
            self.ui.texto_dni_2.setText(str(ssid))
            self.ui.stackedWidget.setCurrentIndex(13)  # estoy en la pantalla de menu y voy a la de configuracion
            self.numpagina = 13
            self.bloqueodepaginas(self.numpagina)
        except:
            cm = "sudo sed -i '5s/.*/                         /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
            os.system(cm)
            cm = "sudo sed -i '6s/.*/                         /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
            os.system(cm)
            cm = "sudo sed -i '7s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
            os.system(cm)
            cm = "sudo sed -i '8s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
            os.system(cm)
            cm = "sudo sed -i '9s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
            os.system(cm)
            cm = "sudo systemctl restart networking.service"
            os.system(cm)

            self.ui.stackedWidget.setCurrentIndex(13)
            self.numpagina = 13
            self.bloqueodepaginas(self.numpagina)
            self.ui.mensajeestadowifi.setText("desconectado")
            self.ui.iconowifi2.setStyleSheet("background-image: url(WIFI no conectado.png);\n"
                                          "border-image: url(WIFI no conectado.png);")
            self.ui.iconowifi.setStyleSheet("background-image: url(WIFI tilde azul inactivo.png);\n"
                                            "border-image: url(WIFI tilde azul inactivo.png);")


   def cartelreiniciar(self):
       msgBox15 = QMessageBox()
       msgBox15.setIcon(QMessageBox.Critical)
       msgBox15.setWindowFlags(Qt.FramelessWindowHint)
       msgBox15.setStyleSheet("QPushButton{ width:75px; font-size: 18px; }")
       msgBox15.setStyleSheet("background-image: url(fondoactividad.png);")
       msgBox15.setFont(QtGui.QFont('Myriad Pro Cond', 15))
       msgBox15.setText("el equipo se reiniciará para terminar de configurarse")
       msgBox15.setWindowTitle("AVISO:")
       msgBox15.setStandardButtons(QMessageBox.Ok)
       #returnValue = msgBox15.exec()
       #if returnValue == QMessageBox.Ok:
          #self.comprobarconexion()
       msgBox15.exec()

   def limpiarcampowifi(self):
       self.buzzer()
       self.ui.lineEditpass_2.clear()
       self.ui.lineEditpass_2.setText("pulse y escriba para  modificar")
       self.datos6=""
       self.quitarteclado2()





   def conectarwifi(self):
      self.timerwifi.stop()
      variable=0
      try:
       # "" important in wpa.conf or it would not work
       goal_ssid = '"' + str(self.nombredered) + '"'
       goal_pw = '"' + str(self.contrasena) + '"'

       #cm = "sudo sed -i '5s/.*/                         /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       #os.system(cm)
       cm = "sudo sed -i '6s/.*/                         /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)
       cm = "sudo sed -i '7s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)
       #cm = "sudo sed -i '8s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       #os.system(cm)
       #cm = "sudo sed -i '9s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       #os.system(cm)
       # Reconfigure goal wifi and key in line 6 and 7 of  wpa_supplicant.conf
       #cm = "sudo sed -i '6s/.*/        ssid=" + goal_ssid + "/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       #os.system(cm)
       #cm = "sudo sed -i '7s/.*/        psk=" + goal_pw + "/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       #os.system(cm)
       cm = "sudo wpa_cli -i wlan0 reconfigure"
       os.system(cm)
       #cm="sudo ifconfig wlan0 down"
       #os.system(cm)
       #cm="sudo ifconfig wlan0 up"
       #os.system(cm)
       #sleep(5)

       cm = "sudo sed -i '5s/.*/network={/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)

       cm = "sudo sed -i '6s/.*/        ssid=" + goal_ssid + "/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)
       cm = "sudo sed -i '7s/.*/        psk=" + goal_pw + "/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)

       cm = "sudo sed -i '8s/.*/        key_mgmt=WPA-PSK/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)
       cm = "sudo sed -i '9s/.*/ }/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
       os.system(cm)

       cm = "sudo wpa_cli -i wlan0 reconfigure"
       os.system(cm)

       sleep(15)
       self.comprobarconexion()
       #self.cartelreiniciar()
       #output=subprocess.check_output("iwconfig wlan0",shell=True).decode()
       #if "Not-Associated" in output:
         #  print("no")
      # else:
        #   print("si")
      except:
          cm = "sudo sed -i '5s/.*/                         /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          os.system(cm)
          cm = "sudo sed -i '6s/.*/                         /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          os.system(cm)
          cm = "sudo sed -i '7s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          os.system(cm)
          cm = "sudo sed -i '8s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          os.system(cm)
          cm = "sudo sed -i '9s/.*/                        /' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          os.system(cm)
          # Reconfigure goal wifi and key in line 6 and 7 of  wpa_supplicant.conf
          #cm = "sudo sed -i '6s/.*/        ssid=" + goal_ssid + "/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          #os.system(cm)
          #cm = "sudo sed -i '7s/.*/        psk=" + goal_pw + "/' /etc/wpa_supplicant/wpa_supplicant.conf"  # using % does not work with all the "" being important in the wpa.conf
          #os.system(cm)
          cm = "sudo wpa_cli -i wlan0 reconfigure"
          os.system(cm)
          #cm="sudo ifconfig wlan0 down"
          #os.system(cm)
          #cm="sudo ifconfig wlan0 up"
          #os.system(cm)
          #sleep(5)


          self.ui.stackedWidget.setCurrentIndex(13)  # estoy en la pantalla de menu y voy a la de configuracion
          self.numpagina = 13
          self.bloqueodepaginas(self.numpagina)
          self.auxiliar10=0
          self.ui.mensajeestadowifi.setText("desconectado")
          self.ui.iconowifi2.setStyleSheet("background-image: url(WIFI no conectado.png);\n"
                                           "border-image: url(WIFI no conectado.png);")
          self.ui.iconowifi.setStyleSheet("background-image: url(WIFI tilde azul inactivo.png);\n"
                                          "border-image: url(WIFI tilde azul inactivo.png);")


   def activarradiofrecuencia(self):

       self.ui.pushButtonenablevacio.setGeometry(QtCore.QRect(35, 430, 50, 50))
       self.ui.pushButtonenablepemf.setGeometry(QtCore.QRect(35, 580, 50, 50))
       self.ui.pushButtonenablelaser.setGeometry(QtCore.QRect(35, 721, 50, 50))
       if self.bloquear_animaciones == 0 and self.deshabilitar_buzzer == 0:
          self.buzzer()
       self.activarradio = not self.activarradio

       if self.activarradio == 1 and self.iniciarsesion == False:
           self.ui.pushButtonenablefrec.setStyleSheet("background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.ui.pulssubepotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsbajapotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           self.ui.pulssubepotencia.setEnabled(True)
           self.ui.pulsbajapotencia.setEnabled(True)
           self.habilitacioneleccionfrecuencias()


       if self.activarradio == 0 and self.iniciarsesion == False:
           self.ui.pushButtonenablefrec.setStyleSheet("background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.ui.pulssubepotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsbajapotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulssubepotencia.setEnabled(False)
           self.ui.pulsbajapotencia.setEnabled(False)
           self.bloqueoeleccionfrecuencias()

       if self.activarradio==0 and self.iniciarsesion==True:
           packet2 = bytearray()
           packet2.append(9)
           packet2.append(0)
           packet2.append(self.sumafrec * self.activarradio)
           packet2.append(self.cabezalactivo * self.activarradio)
           packet2.append(0)
           puertoserie.write(packet2)
           self.ui.pushButtonenablefrec.setStyleSheet("background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.bloqueoeleccionfrecuencias()
           self.ui.pulssubepotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsbajapotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulssubepotencia.setEnabled(False)
           self.ui.pulsbajapotencia.setEnabled(False)




       if self.activarradio==1 and self.iniciarsesion==True:

           packet1 = bytearray()
           packet1.append(9)
           packet1.append(self.valorpotencia*self.activarradio)
           packet1.append(self.sumafrec*self.activarradio)
           packet1.append(self.cabezalactivo*self.activarradio)
           packet1.append(self.frio*self.activarradio)
           puertoserie.write(packet1)
           #print(packet1)
           self.ui.pushButtonenablefrec.setStyleSheet("background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.habilitacioneleccionfrecuencias()
           self.ui.pulssubepotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsbajapotencia.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           self.ui.pulssubepotencia.setEnabled(True)
           self.ui.pulsbajapotencia.setEnabled(True)
       if  self.bloquear_animaciones==0:
          self.animarpulsadores(self.ui.pushButtonenablefrec, 35, 175, 27, 167, 50, 50)
       self.bloquear_animaciones = 0
       #if self.iniciarsesion==True:
          #self.enviardatosdesesionpemf()
       if self.iniciarsesion==False:
           self.bloquearpotencia()


   def animarpulsadores(self,pulsador,x1,y1,x2,y2, ancho, alto):

           self.anim_group = QSequentialAnimationGroup()
           self.animacionespulsadores4 = QPropertyAnimation(pulsador, b"geometry")
           self.animacionespulsadores4.setDuration(100)
           self.animacionespulsadores4.setEasingCurve(QtCore.QEasingCurve.InCubic)
           self.animacionespulsadores4.setEndValue(QtCore.QRect(x2, y2, ancho+10, alto+10))

           self.animacionespulsadores5 = QPropertyAnimation(pulsador, b"geometry")
           self.animacionespulsadores5.setDuration(100)
           self.animacionespulsadores5.setEasingCurve(QtCore.QEasingCurve.InCubic)
           self.animacionespulsadores5.setEndValue(QtCore.QRect(x1, y1, ancho, alto))
           self.anim_group.addAnimation(self.animacionespulsadores4)
           self.anim_group.addAnimation(self.animacionespulsadores5)
           self.anim_group.start()

   def animarpulsadorestransicion(self,pulsador,x1,y1,x2,y2, ancho, alto,seleccion):

           self.anim_group2 = QSequentialAnimationGroup()
           self.animacionespulsadores20 = QPropertyAnimation(pulsador, b"geometry")
           self.animacionespulsadores20.setDuration(100)
           self.animacionespulsadores20.setEasingCurve(QtCore.QEasingCurve.InCubic)
           self.animacionespulsadores20.setEndValue(QtCore.QRect(x2, y2, ancho+10, alto+10))

           self.animacionespulsadores21 = QPropertyAnimation(pulsador, b"geometry")
           self.animacionespulsadores21.setDuration(100)
           self.animacionespulsadores21.setEasingCurve(QtCore.QEasingCurve.InCubic)
           self.animacionespulsadores21.setEndValue(QtCore.QRect(x1, y1, ancho, alto))
           self.anim_group2.addAnimation(self.animacionespulsadores20)
           self.anim_group2.addAnimation(self.animacionespulsadores21)
           self.anim_group2.start()
           self.anim_group2.finished.connect(lambda : self.funciondeterminada(seleccion))

   def funciondeterminada(self,pulsadorpresionado):
       if pulsadorpresionado==1:
           self.iraselecciondesexo()
       if pulsadorpresionado==2:
           self.informacionadicional()
           self.ui.stackedWidget.setCurrentIndex(10)
       if pulsadorpresionado==3:
           self.tomardatoswifi()
       if pulsadorpresionado==4:
           self.actualizarredes()
       if pulsadorpresionado==5:
           self.ui.stackedWidget.setCurrentIndex(15)
           self.numpagina = 15
           self.bloqueodepaginas(self.numpagina)


   def animarlabel(self, etiqueta,inicio,fin):
       self.anim_group1 = QSequentialAnimationGroup()
       self.labelFont=etiqueta.font()
       self.ani = QtCore.QVariantAnimation()
       self.ani.setEasingCurve(QtCore.QEasingCurve.InQuad)
       self.ani.setStartValue(inicio)
       self.ani.setEndValue(fin)
       self.ani.setDuration(100)
       self.ani.valueChanged.connect(self.updateLabelFont)

       self.ani1 = QtCore.QVariantAnimation()
       self.ani1.setEasingCurve(QtCore.QEasingCurve.InQuad)
       self.ani1.setStartValue(fin)
       self.ani1.setEndValue(inicio)
       self.ani1.setDuration(100)
       self.ani1.valueChanged.connect(self.updateLabelFont)

       self.anim_group1.addAnimation(self.ani)
       self.anim_group1.addAnimation(self.ani1)
       self.anim_group1.start()


   def updateLabelFont(self, value):
       self.labelFont.setPointSize(value)
       self.ui.potencia.setFont(self.labelFont)



   def animarlabel2(self, etiqueta,inicio,fin):
       self.anim_group1 = QSequentialAnimationGroup()
       self.labelFont=etiqueta.font()
       self.objeto=etiqueta
       self.ani = QtCore.QVariantAnimation()
       self.ani.setEasingCurve(QtCore.QEasingCurve.InQuad)

       self.ani.setStartValue(inicio)
       self.ani.setEndValue(fin)
       self.ani.setDuration(200)
       self.ani.valueChanged.connect(self.updateLabelFont2)
       self.ani1 = QtCore.QVariantAnimation()
       self.ani1.setEasingCurve(QtCore.QEasingCurve.InQuad)
       self.ani1.setStartValue(fin)
       self.ani1.setEndValue(inicio)
       self.ani1.setDuration(200)
       self.ani1.valueChanged.connect(self.updateLabelFont2)
       self.anim_group1.addAnimation(self.ani)
       self.anim_group1.addAnimation(self.ani1)
       self.anim_group1.start()


   def updateLabelFont2(self, value):
       self.labelFont.setPointSize(value)
       self.objeto.setFont(self.labelFont)




   def animarlabel3(self):
       #self.ui.selecciontrat.setGeometry(QtCore.QRect(694, 170,0, 0))
       #self.animacionespulsadores43 = QPropertyAnimation(self.ui.selecciontrat, b"geometry")
       #self.animacionespulsadores43.setDuration(2000)
       #self.animacionespulsadores43.setEasingCurve(QtCore.QEasingCurve.InCubic)
       #self.animacionespulsadores43.setEndValue(QtCore.QRect(694, 170, 311, 70))
       #self.animacionespulsadores43.start()

       self.ui.selecciontrat.setGeometry(QtCore.QRect(694, 175, 311, 0))
       self.animacion = QPropertyAnimation(self.ui.selecciontrat, b"size")
       self.animacion.setDuration(100)
       self.animacion.setEndValue(QtCore.QSize(311, 70))
       self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
       self.animacion.start()

   def animarlabel4(self, etiqueta, inicio, fin,seleccion):
       self.buzzer()
       self.anim_group11 = QSequentialAnimationGroup()
       self.labelFont = etiqueta.font()
       self.objeto = etiqueta
       self.ani11 = QtCore.QVariantAnimation()
       self.ani11.setEasingCurve(QtCore.QEasingCurve.InQuad)

       self.ani11.setStartValue(inicio)
       self.ani11.setEndValue(fin)
       self.ani11.setDuration(200)
       self.ani11.valueChanged.connect(self.updateLabelFont4)
       self.ani12 = QtCore.QVariantAnimation()
       self.ani12.setEasingCurve(QtCore.QEasingCurve.InQuad)
       self.ani12.setStartValue(fin)
       self.ani12.setEndValue(inicio)
       self.ani12.setDuration(200)
       self.ani12.valueChanged.connect(self.updateLabelFont4)
       self.anim_group11.addAnimation(self.ani11)
       self.anim_group11.addAnimation(self.ani12)
       self.anim_group11.start()
       self.anim_group11.finished.connect(lambda: self.funciondeterminada2(seleccion))


   def updateLabelFont4(self, value):
       self.labelFont.setPointSize(value)
       self.objeto.setFont(self.labelFont)

   def funciondeterminada2(self,opcion):
       if opcion==1:
           self.cancelardetener()
       if opcion==2:
           self.confirmardetener()
       if opcion==3:
           self.confirmardetener2()

   def animaropcioneszonas(self,mujer):
       self.ui.subescapulares.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.brazospoteriores.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.flancos.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.gluteos.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.trocanteriana.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.muslospos.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.rostro.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.cuello.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.escote.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.abdomen.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.muslosanteriores.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.muslosinternos.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.brazosanteriores.setGeometry(QtCore.QRect(700, 400, 0, 0))

       self.ui.subescapulares_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.brazospoteriores_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.flancos_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.gluteos_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.trocanteriana_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.muslospos_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.rostro_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.cuello_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.escote_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.abdomen_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.muslosanteriores_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.muslosinternos_2.setGeometry(QtCore.QRect(700, 400, 0, 0))
       self.ui.brazosanteriores_2.setGeometry(QtCore.QRect(700, 400, 0, 0))

       if mujer==1:
           self.animacionespulsadores1 = QPropertyAnimation(self.ui.subescapulares, b"geometry")
           self.animacionespulsadores3 = QPropertyAnimation(self.ui.brazospoteriores, b"geometry")
           self.animacionespulsadores4 = QPropertyAnimation(self.ui.flancos, b"geometry")
           self.animacionespulsadores5 = QPropertyAnimation(self.ui.gluteos, b"geometry")
           self.animacionespulsadores6 = QPropertyAnimation(self.ui.trocanteriana, b"geometry")
           self.animacionespulsadores7 = QPropertyAnimation(self.ui.muslospos, b"geometry")
           self.animacionespulsadores8 = QPropertyAnimation(self.ui.rostro, b"geometry")
           self.animacionespulsadores9 = QPropertyAnimation(self.ui.cuello, b"geometry")
           self.animacionespulsadores10 = QPropertyAnimation(self.ui.escote, b"geometry")
           self.animacionespulsadores11 = QPropertyAnimation(self.ui.brazosanteriores, b"geometry")
           self.animacionespulsadores12 = QPropertyAnimation(self.ui.abdomen, b"geometry")
           self.animacionespulsadores13 = QPropertyAnimation(self.ui.muslosanteriores, b"geometry")
           self.animacionespulsadores14 = QPropertyAnimation(self.ui.muslosinternos, b"geometry")
       else:
           self.animacionespulsadores1 = QPropertyAnimation(self.ui.subescapulares_2, b"geometry")
           self.animacionespulsadores3 = QPropertyAnimation(self.ui.brazospoteriores_2, b"geometry")
           self.animacionespulsadores4 = QPropertyAnimation(self.ui.flancos_2, b"geometry")
           self.animacionespulsadores5 = QPropertyAnimation(self.ui.gluteos_2, b"geometry")
           self.animacionespulsadores6 = QPropertyAnimation(self.ui.trocanteriana_2, b"geometry")
           self.animacionespulsadores7 = QPropertyAnimation(self.ui.muslospos_2, b"geometry")
           self.animacionespulsadores8 = QPropertyAnimation(self.ui.rostro_2, b"geometry")
           self.animacionespulsadores9 = QPropertyAnimation(self.ui.cuello_2, b"geometry")
           self.animacionespulsadores10 = QPropertyAnimation(self.ui.escote_2, b"geometry")
           self.animacionespulsadores11 = QPropertyAnimation(self.ui.brazosanteriores_2, b"geometry")
           self.animacionespulsadores12 = QPropertyAnimation(self.ui.abdomen_2, b"geometry")
           self.animacionespulsadores13 = QPropertyAnimation(self.ui.muslosanteriores_2, b"geometry")
           self.animacionespulsadores14 = QPropertyAnimation(self.ui.muslosinternos_2, b"geometry")


       self.animacionespulsadores1.setDuration(500)
       self.animacionespulsadores1.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores1.setEndValue(QtCore.QRect(35, 225, 146, 40))



       self.animacionespulsadores3.setDuration(500)
       self.animacionespulsadores3.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores3.setEndValue(QtCore.QRect(35, 325, 161, 40))



       self.animacionespulsadores4.setDuration(500)
       self.animacionespulsadores4.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores4.setEndValue(QtCore.QRect(35, 440, 66, 40))



       self.animacionespulsadores5.setDuration(500)
       self.animacionespulsadores5.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores5.setEndValue(QtCore.QRect(35, 550, 71, 40))



       self.animacionespulsadores6.setDuration(500)
       self.animacionespulsadores6.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores6.setEndValue(QtCore.QRect(35, 637, 181, 40))



       self.animacionespulsadores7.setDuration(500)
       self.animacionespulsadores7.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores7.setEndValue(QtCore.QRect(35, 715, 161, 40))



       self.animacionespulsadores8.setDuration(500)
       self.animacionespulsadores8.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores8.setEndValue(QtCore.QRect(1090, 180, 146, 40))



       self.animacionespulsadores9.setDuration(500)
       self.animacionespulsadores9.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores9.setEndValue(QtCore.QRect(1154, 280, 91, 40))



       self.animacionespulsadores10.setDuration(500)
       self.animacionespulsadores10.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores10.setEndValue(QtCore.QRect(1143, 370, 116, 40))



       self.animacionespulsadores11.setDuration(500)
       self.animacionespulsadores11.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores11.setEndValue(QtCore.QRect(1074, 458, 171, 40))



       self.animacionespulsadores12.setDuration(500)
       self.animacionespulsadores12.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores12.setEndValue(QtCore.QRect(1133, 560, 116, 40))



       self.animacionespulsadores13.setDuration(500)
       self.animacionespulsadores13.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores13.setEndValue(QtCore.QRect(1075, 655, 171, 40))



       self.animacionespulsadores14.setDuration(500)
       self.animacionespulsadores14.setEasingCurve(QtCore.QEasingCurve.Linear)
       self.animacionespulsadores14.setEndValue(QtCore.QRect(1080, 720, 171, 40))

       self.grupoanimado = QParallelAnimationGroup(self)
       self.grupoanimado.setDirection(self.grupoanimado.Forward)
       # self.grupoanimado.addAnimation(self.animacion2)
       # self.grupoanimado.addAnimation(self.animacion)
       self.grupoanimado.addAnimation(self.animacionespulsadores1)
       self.grupoanimado.addAnimation(self.animacionespulsadores3)
       self.grupoanimado.addAnimation(self.animacionespulsadores4)
       self.grupoanimado.addAnimation(self.animacionespulsadores5)
       self.grupoanimado.addAnimation(self.animacionespulsadores6)
       self.grupoanimado.addAnimation(self.animacionespulsadores7)
       self.grupoanimado.addAnimation(self.animacionespulsadores8)
       self.grupoanimado.addAnimation(self.animacionespulsadores9)
       self.grupoanimado.addAnimation(self.animacionespulsadores10)
       self.grupoanimado.addAnimation(self.animacionespulsadores11)
       self.grupoanimado.addAnimation(self.animacionespulsadores12)
       self.grupoanimado.addAnimation(self.animacionespulsadores13)
       self.grupoanimado.addAnimation(self.animacionespulsadores14)

       self.grupoanimado.start()


   def vaciocontrolcontadores(self):
       if self.contadorvacio == 1:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("4Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(4Hz.png);")
              self.programavacio = 1
           if self.nivelvacio=="alto":
              self.ui.programasvacio.setStyleSheet("background-image: url(4Hz.png);")
              self.ui.label_12.setText("4Hz-vacio alto")
              self.programavacio = 2

       if self.contadorvacio == 2:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("3.5Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(3,5Hz.png);")
              self.programavacio = 3
           if self.nivelvacio=="alto":
              self.ui.label_12.setText("3.5Hz-vacio alto")
              self.ui.programasvacio.setStyleSheet("background-image: url(3,5Hz.png);")
              self.programavacio = 4

       if self.contadorvacio == 3:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("3Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(3Hz.png);")
              self.programavacio = 5
           if self.nivelvacio=="alto":
              self.ui.label_12.setText("3Hz-vacio alto")
              self.ui.programasvacio.setStyleSheet("background-image: url(3Hz.png);")
              self.programavacio = 6

       if self.contadorvacio == 4:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("2.5Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(2,5Hz.png);")
              self.programavacio = 7
           if self.nivelvacio=="alto":
              self.ui.label_12.setText("2.5Hz-vacio alto")
              self.ui.programasvacio.setStyleSheet("background-image: url(2,5Hz.png);")
              self.programavacio = 8

       if self.contadorvacio == 5:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("2Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(2Hz.png);")
              self.programavacio = 9
           if self.nivelvacio=="alto":
              self.ui.label_12.setText("2Hz-vacio alto")
              self.ui.programasvacio.setStyleSheet("background-image: url(2Hz.png);")
              self.programavacio = 10

       if self.contadorvacio == 6:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("1.5Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(1,5Hz.png);")
              self.programavacio = 11
           if self.nivelvacio=="alto":
              self.ui.label_12.setText("1.5Hz-vacio alto")
              self.ui.programasvacio.setStyleSheet("background-image: url(1,5Hz.png);")
              self.programavacio = 12

       if self.contadorvacio == 7:
           if self.nivelvacio=="medio":
              self.ui.label_12.setText("1Hz-vacio medio")
              self.ui.programasvacio.setStyleSheet("background-image: url(1Hz.png);")
              self.programavacio = 13
           if self.nivelvacio=="alto":
              self.ui.label_12.setText("1Hz-vacio alto")
              self.ui.programasvacio.setStyleSheet("background-image: url(1Hz.png);")
              self.programavacio = 14


   def bajarvacio(self):
       self.buzzer()
       #self.ui.pulsbajafrio.setGeometry(QtCore.QRect(507, 292, 102, 74))
       #self.ui.pulsbajafrio.setStyleSheet( "background-image: url(7 - Trabajando boton abajo instancia.png);\n" "border-image: url(7 - Trabajando boton abajo instancia.png);")
       self.contadorvacio = self.contadorvacio - 1
       if self.contadorvacio < 1:
           self.contadorvacio = 1
       self.vaciocontrolcontadores()



       self.animarlabel2(self.ui.label_12, 20, 25)
       if self.iniciarsesion == True and self.activarvacio==1:
          # print(self.programavacio)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()
       self.animarpulsadores(self.ui.pulsabajovacum, 510,440, 502, 432,76,57)



   def setvaciomedio(self):
       if self.deshabilitar_buzzer == 0:
           self.buzzer()
       self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                     "border-image: url(Boton chico activo.png);")
       self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                    "border-image: url(Boton chico inactivo.png);")
       self.nivelvacio = "medio"
       self.vaciocontrolcontadores()
       if self.iniciarsesion == True and self.activarvacio == 1:
           # print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()



   def setvacioalto(self):
       if self.deshabilitar_buzzer == 0:
           self.buzzer()
       self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                        "border-image: url(Boton chico inactivo.png);")
       self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                    "border-image: url(Boton chico activo.png);")
       self.nivelvacio = "alto"
       self.vaciocontrolcontadores()
       if self.iniciarsesion == True and self.activarvacio == 1:
           # print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()




   def activarvacum(self):

       self.ui.pushButtonenablefrec.setGeometry(QtCore.QRect(35, 175, 50, 50))
       self.ui.pushButtonenablepemf.setGeometry(QtCore.QRect(35, 580, 50, 50))
       self.ui.pushButtonenablelaser.setGeometry(QtCore.QRect(35, 721, 50, 50))
       if self.bloquear_animaciones == 0 and self.deshabilitar_buzzer==0:
           self.buzzer()
       self.activarvacio = not self.activarvacio

       if self.activarvacio == 1 and self.iniciarsesion == False:
           self.ui.pushButtonenablevacio.setStyleSheet(
               "background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.vacio="activado"
           self.ui.vaciomedio.setEnabled(True)
           self.ui.vacioalto.setEnabled(True)
           self.ui.textof3_2.setText('<font color="black">medio<font>')
           self.ui.textof3_3.setText('<font color="black">alto<font>')
           if self.nivelvacio == "medio":
               self.deshabilitar_buzzer = 1
               self.setvaciomedio()
               self.deshabilitar_buzzer = 0
           if self.nivelvacio == "alto":
               self.deshabilitar_buzzer = 1
               self.setvacioalto()
               self.deshabilitar_buzzer = 0
           self.ui.pulsarribavacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsabajovacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           self.ui.pulsarribavacum.setEnabled(True)
           self.ui.pulsabajovacum.setEnabled(True)


       if self.activarvacio == 0 and self.iniciarsesion == False:

           self.ui.pushButtonenablevacio.setStyleSheet(
               "background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")

           self.vacio = "desactivado"
           self.ui.vaciomedio.setEnabled(False)
           self.ui.vacioalto.setEnabled(False)
           self.ui.textof3_2.setText('<font color="grey">medio<font>')
           self.ui.textof3_3.setText('<font color="grey">alto<font>')
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                         "border-image: url(Boton chico inactivo.png);")
           self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")
           self.ui.pulsarribavacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsabajovacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulsarribavacum.setEnabled(False)
           self.ui.pulsabajovacum.setEnabled(False)





       if self.activarvacio == 0 and self.iniciarsesion == True:
           packet9 = bytearray()
           packet9.append(5)
           packet9.append(0)
           packet9.append(self.programapemf*self.habilitarpemf)
           packet9.append(self.programalaser*self.habilitarlaser)
           packet9.append(0)
           puertoserie.write(packet9)
           sleep(0.1)
           puertoserie.write(packet9)
           #print(packet9)
           self.ui.pushButtonenablevacio.setStyleSheet(
               "background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.vacio="desactivado"
           self.ui.vaciomedio.setEnabled(False)
           self.ui.vacioalto.setEnabled(False)
           self.ui.textof3_2.setText('<font color="grey">medio<font>')
           self.ui.textof3_3.setText('<font color="grey">alto<font>')
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")
           self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                           "border-image: url(Boton chico inactivo.png);")
           self.ui.pulsarribavacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsabajovacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulsarribavacum.setEnabled(False)
           self.ui.pulsabajovacum.setEnabled(False)
           if self.activarvacio==0 and self.habilitarlaser==0 and self.habilitarpemf==0:
               self.timercab.stop()


       if self.activarvacio == 1 and self.iniciarsesion == True:
           packet8 = bytearray()
           packet8.append(5)
           packet8.append(self.programavacio*self.activarvacio)
           packet8.append(self.programapemf*self.habilitarpemf)
           packet8.append(self.programalaser*self.habilitarlaser)
           packet8.append(0)
           puertoserie.write(packet8)
           #print(packet8)
           self.ui.pushButtonenablevacio.setStyleSheet("background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.vacio="activado"
           self.ui.vaciomedio.setEnabled(True)
           self.ui.vacioalto.setEnabled(True)
           self.ui.textof3_2.setText('<font color="black">medio<font>')
           self.ui.textof3_3.setText('<font color="black">alto<font>')
           if self.nivelvacio == "medio":
               self.deshabilitar_buzzer = 1
               self.setvaciomedio()
               self.deshabilitar_buzzer = 0
           if self.nivelvacio == "alto":
               self.deshabilitar_buzzer = 1
               self.setvacioalto()
               self.deshabilitar_buzzer = 0
           #print("progr vacio" + str(self.programavacio))
           #print("nivel de vacio" + str(self.nivelvacio))

           #print("progr pemf" + str(self.programapemf))
           #print("forma" + self.formaonda)
           self.ui.pulsarribavacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsabajovacum.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           self.ui.pulsarribavacum.setEnabled(True)
           self.ui.pulsabajovacum.setEnabled(True)
           if (self.cabezalactivo==2 or self.cabezalactivo==3 or self.cabezalactivo==4) and (self.activarvacio==1 or self.habilitarpemf==1 or self.habilitarlaser==1):
             self.animacioncabezalmultitec()
       if self.bloquear_animaciones==0:
          self.animarpulsadores(self.ui.pushButtonenablevacio, 35, 430, 27, 422,50,50)
       self.bloquear_animaciones = 0

   def modificar_vacio_durantetratamiento(self, contadorvacio,nivelv):

       if contadorvacio == 0:
           #self.ui.label_12.setText("desactivado")
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")

       if contadorvacio == 1:
           if nivelv==1:
              self.ui.label_12.setText("4Hz-vacio medio")
              self.programavacio = 1
           if nivelv==2:
              self.ui.label_12.setText("4Hz-vacio alto")
              self.programavacio = 2

       if contadorvacio == 2:
           if nivelv==1:
              self.ui.label_12.setText("3.5Hz-vacio medio")
              self.programavacio = 3
           if nivelv==2:
              self.ui.label_12.setText("3.5Hz-vacio alto")
              self.programavacio = 4

       if contadorvacio == 3:
           if nivelv==1:
              self.ui.label_12.setText("3Hz-vacio medio")
              self.programavacio = 5
           if nivelv==2:
              self.ui.label_12.setText("3Hz-vacio alto")
              self.programavacio = 6

       if contadorvacio == 4:
           if nivelv==1:
              self.ui.label_12.setText("2.5Hz-vacio medio")
              self.programavacio = 7
           if nivelv==2:
              self.ui.label_12.setText("2.5Hz-vacio alto")
              self.programavacio = 8

       if contadorvacio == 5:
           if nivelv==1:
              self.ui.label_12.setText("2Hz-vacio medio")
              self.programavacio = 9
           if nivelv==2:
              self.ui.label_12.setText("2Hz-vacio alto")
              self.programavacio = 10

       if contadorvacio == 6:
           if nivelv==1:
              self.ui.label_12.setText("1.5Hz-vacio medio")
              self.programavacio = 11
           if nivelv==2:
              self.ui.label_12.setText("1.5Hz-vacio alto")
              self.programavacio = 12

       if contadorvacio == 7:
           if nivelv==1:
              self.ui.label_12.setText("1Hz-vacio medio")
              self.programavacio = 13
           if nivelv==2:
              self.ui.label_12.setText("1Hz-vacio alto")
              self.programavacio = 14

       if nivelv==1 and self.contadorvacio!=0:
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                            "border-image: url(Boton chico activo.png);")
           self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                           "border-image: url(Boton chico inactivo.png);")
       if nivelv==2 and self.contadorvacio!=0:
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")
           self.ui.vacioalto.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                           "border-image: url(Boton chico activo.png);")
       if self.activarvacio == 0:
           #self.ui.label_12.setText("desactivado")
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")
           self.ui.vaciomedio.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                            "border-image: url(Boton chico inactivo.png);")


       if self.iniciarsesion == True and self.activarvacio == 1:
           # print(self.programavacio)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()



   def subirvacio(self):
       self.buzzer()
       #self.ui.pulsarribavacum.setGeometry(QtCore.QRect(392, 292, 102, 74))
       #self.ui.pulsarribavacum.setStyleSheet("background-image: url(7 - Trabajando boton arriba instancia.png);\n" "border-image: url(7 - Trabajando boton arriba instancia.png);")
       self.contadorvacio = 1 + self.contadorvacio
       if self.contadorvacio > 7:
           self.contadorvacio = 7

       self.vaciocontrolcontadores()

       self.animarlabel2(self.ui.label_12, 20, 25)


       if self.iniciarsesion == True and self.activarvacio==1:
           #print(self.programavacio)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()
       self.animarpulsadores(self.ui.pulsarribavacum, 410, 440, 402, 432,76,57)


   def activarlaser(self):
       self.ui.pushButtonenablevacio.setGeometry(QtCore.QRect(35, 430, 50, 50))
       self.ui.pushButtonenablepemf.setGeometry(QtCore.QRect(35, 580, 50, 50))
       self.ui.pushButtonenablefrec.setGeometry(QtCore.QRect(35, 175, 50, 50))
       if self.bloquear_animaciones == 0 and self.deshabilitar_buzzer==0 :
           self.buzzer()
       self.habilitarlaser = not self.habilitarlaser
       if self.habilitarlaser == 1 and self.iniciarsesion == False:
           self.ui.pushButtonenablelaser.setStyleSheet(
               "background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.ui.label_11.setStyleSheet("background-image: url(lipolisis laser.png);")
           self.laser = "activado"

       if self.habilitarlaser == 0 and self.iniciarsesion == False:
           self.ui.pushButtonenablelaser.setStyleSheet(
               "background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.ui.label_11.setStyleSheet("background-image: url(lipolisis laser instancia.png);")
           self.laser = "desactivado"

       if self.habilitarlaser == 0 and self.iniciarsesion == True:

           packet9 = bytearray()
           packet9.append(5)
           packet9.append(self.programavacio*self.activarvacio)
           packet9.append(self.programapemf*self.habilitarpemf)
           packet9.append(0)
           packet9.append(0)
           puertoserie.write(packet9)
           sleep(0.1)
           puertoserie.write(packet9)
           #print(packet9)
           self.ui.pushButtonenablelaser.setStyleSheet(
               "background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.ui.label_11.setStyleSheet("background-image: url(lipolisis laser instancia.png);")
           self.laser="desactivado"
           if self.activarvacio==0 and self.habilitarlaser==0 and self.habilitarpemf==0:
               self.timercab.stop()

       if self.habilitarlaser== 1 and self.iniciarsesion == True:
           packet8 = bytearray()
           packet8.append(5)
           packet8.append(self.programavacio*self.activarvacio)
           packet8.append(self.programapemf*self.habilitarpemf)
           packet8.append(self.programalaser*self.habilitarlaser)
           packet8.append(0)
           puertoserie.write(packet8)
           #print(packet8)
           self.ui.pushButtonenablelaser.setStyleSheet("background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.ui.label_11.setStyleSheet("background-image: url(lipolisis laser.png);")
           self.laser="activado"
           if (self.cabezalactivo==2 or self.cabezalactivo==3 or self.cabezalactivo==4) and (self.activarvacio==1 or self.habilitarpemf==1 or self.habilitarlaser==1):
             self.animacioncabezalmultitec()
       if self.bloquear_animaciones==0:
          self.animarpulsadores(self.ui.pushButtonenablelaser,35, 721, 27, 713, 50, 50)
       self.bloquear_animaciones = 0


   def bajarlaser(self):
       self.buzzer()
       #self.ui.pulsbajafrio.setGeometry(QtCore.QRect(507, 292, 102, 74))
       #self.ui.pulsbajafrio.setStyleSheet( "background-image: url(7 - Trabajando boton abajo instancia.png);\n" "border-image: url(7 - Trabajando boton abajo instancia.png);")
       self.contadorlaser = self.contadorlaser - 1
       if self.contadorlaser < 1:
           self.contadorlaser = 6
       if self.contadorlaser == 4:
           self.ui.label_14.setText("programa 4")
           # self.niveldefrioelegido="nivel bajo"
           self.programalaser = 1
       if self.contadorlaser == 5:
           self.ui.label_14.setText("programa 5")
           # self.niveldefrioelegido="nivel medio"
           self.programalaser = 1
       if self.contadorlaser == 6:
           self.ui.label_14.setText("programa 6")
           # self.niveldefrioelegido="nivel alto"
           self.programalaser = 1
       if self.contadorlaser == 3: # or self.contadorlaser == -1:
           self.programalaser = 1
           self.ui.label_14.setText("programa 3")
           #self.niveldefrioelegido = "nivel alto"
       if self.contadorlaser == 2:
           self.ui.label_14.setText("programa 2")
           #self.niveldefrioelegido = "nivel medio"
           self.programalaser = 1
       if self.contadorlaser == 1:
           self.ui.label_14.setText("programa 1")
           #self.niveldefrioelegido = "nivel bajo"
           self.programalaser= 1
       #if self.contadorlaser == 0:
           #self.ui.programaslaser.setText("desactivado")
           #self.niveldefrioelegido = "desactivado"
           #self.programalaser = 0
       self.animarlabel2(self.ui.label_14, 20, 25)
       if self.iniciarsesion == True and self.habilitarlaser==1:
           #print(self.programalaser)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()
       self.animarpulsadores(self.ui.pulsbajalaser, 510, 688, 502, 680,93,73)

   def subirlaser(self):

       self.buzzer()
       #self.ui.pulsarribavacum.setGeometry(QtCore.QRect(392, 292, 102, 74))
       #self.ui.pulsarribavacum.setStyleSheet("background-image: url(7 - Trabajando boton arriba instancia.png);\n" "border-image: url(7 - Trabajando boton arriba instancia.png);")
       self.contadorlaser = 1 + self.contadorlaser
       if self.contadorlaser > 6:
           self.contadorlaser = 1
      # if self.contadorlaser == 0 or self.contadorlaser==4:

           #self.programalaser = 0
           #self.ui.programaslaser.setText("desactivado")
           #self.niveldefrioelegido="desactivado"
       if self.contadorlaser == 1:
           self.ui.label_14.setText("programa 1")
          # self.niveldefrioelegido="nivel bajo"
           self.programalaser = 1
       if self.contadorlaser == 2:
           self.ui.label_14.setText("programa 2")
          # self.niveldefrioelegido="nivel medio"
           self.programalaser = 1
       if self.contadorlaser == 3:
           self.ui.label_14.setText("programa 3")
          # self.niveldefrioelegido="nivel alto"
           self.programalaser = 1
       if self.contadorlaser == 4:
           self.ui.label_14.setText("programa 4")
           # self.niveldefrioelegido="nivel bajo"
           self.programalaser = 1
       if self.contadorlaser == 5:
           self.ui.label_14.setText("programa 5")
           # self.niveldefrioelegido="nivel medio"
           self.programalaser = 1
       if self.contadorlaser == 6:
           self.ui.label_14.setText("programa 6")
           # self.niveldefrioelegido="nivel alto"
           self.programalaser = 1
       self.animarlabel2(self.ui.label_14, 15, 20)

       if self.iniciarsesion == True and self.habilitarlaser==1:
           #print(self.programalaser)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()
       self.animarpulsadores(self.ui.pulssubetlaser, 409, 688, 401, 680,93,73)

   def modificar_laser_durantetratamiento(self, contadorlaser):
       if contadorlaser == 1:
           self.ui.label_14.setText("programa 1")
           # self.niveldefrioelegido="nivel bajo"
           self.programalaser = 1
       if contadorlaser == 2:
           self.ui.label_14.setText("programa 2")
           # self.niveldefrioelegido="nivel medio"
           self.programalaser = 1
       if contadorlaser == 3:
           self.ui.label_14.setText("programa 3")
           # self.niveldefrioelegido="nivel alto"
           self.programalaser = 1
       if contadorlaser == 4:
           self.ui.label_14.setText("programa 4")
           # self.niveldefrioelegido="nivel bajo"
           self.programalaser = 1
       if contadorlaser == 5:
           self.ui.label_14.setText("programa 5")
           # self.niveldefrioelegido="nivel medio"
           self.programalaser = 1
       if contadorlaser == 6:
           self.ui.label_14.setText("programa 6")
           # self.niveldefrioelegido="nivel alto"
           self.programalaser = 1




       if self.iniciarsesion == True and self.habilitarlaser == 1:
           # print(self.programalaser)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()


   def settriangular(self):
       if self.deshabilitar_buzzer==0:
        self.buzzer()
       self.formaonda="triangular"
       self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
       self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                        "border-image: url(Boton chico activo.png);")
       self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                       "border-image: url(Boton chico inactivo.png);")
       self.contadorcontrolpemf(self.formaonda)
       if self.iniciarsesion == True and self.habilitarpemf == 1:
           # print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()



   def setcuadrada(self):
       if self.deshabilitar_buzzer == 0:
           self.buzzer()
       self.formaonda="cuadrada"
       self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
       self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico activo.png);\n"
                                        "border-image: url(Boton chico activo.png);")
       self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                       "border-image: url(Boton chico inactivo.png);")
       self.contadorcontrolpemf(self.formaonda)
       if self.iniciarsesion == True and self.habilitarpemf == 1:
           # print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()



   def contadorcontrolpemf(self,formadeonda):
       if self.contadorpemf == 1:
           #self.ui.label_15.setText("programa 1")
           self.ui.label_13.setText("5 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 1
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 11

       if self.contadorpemf == 2:
           #self.ui.label_15.setText("programa 2")
           self.ui.label_13.setText("10 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 2
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 12

       if self.contadorpemf == 3:
           #self.ui.label_15.setText("programa 3")
           self.ui.label_13.setText("15 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 3
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 13

       if self.contadorpemf == 4:
           #self.ui.label_15.setText("programa 4")
           self.ui.label_13.setText("20 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 4
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 14

       if self.contadorpemf == 5:
           #self.ui.label_15.setText("programa 5")
           self.ui.label_13.setText("25 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 5
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 15

       if self.contadorpemf == 6:
           #self.ui.label_15.setText("programa 6")
           self.ui.label_13.setText("30 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 6
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 16

       if self.contadorpemf == 7:
           #self.ui.label_15.setText("programa 7")
           self.ui.label_13.setText("35 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 7
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 17

       if self.contadorpemf == 8:
           #self.ui.label_15.setText("programa 8")
           self.ui.label_13.setText("40 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 8
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 18

       if self.contadorpemf == 9:
           #self.ui.label_15.setText("programa 9")
           self.ui.label_13.setText("45 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 9
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 19


       if self.contadorpemf == 10:
           #self.ui.label_15.setText("programa 10")
           self.ui.label_13.setText("50 hz")
           if formadeonda=="triangular":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
              self.programapemf = 10
           if formadeonda=="cuadrada":
              self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
              self.programapemf = 20


   def activarpemf(self):

       self.ui.pushButtonenablevacio.setGeometry(QtCore.QRect(35, 430, 50, 50))
       self.ui.pushButtonenablefrec.setGeometry(QtCore.QRect(35, 175, 50, 50))
       self.ui.pushButtonenablelaser.setGeometry(QtCore.QRect(35, 721, 50, 50))
       if self.bloquear_animaciones==0 and self.deshabilitar_buzzer==0:
          self.buzzer()
       self.habilitarpemf = not self.habilitarpemf
       if self.habilitarpemf == 1 and self.iniciarsesion == False:
           self.ui.pushButtonenablepemf.setStyleSheet(
               "background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.pemf = "activado"
           self.ui.pemftriangular.setEnabled(True)
           self.ui.pemfcuadrado.setEnabled(True)

           self.ui.textof3_4.setText('<font color="black">triangular<font>')
           self.ui.textof3_5.setText('<font color="black">cuadrada<font>')
           if self.formaonda=="triangular":
               self.deshabilitar_buzzer=1
               self.settriangular()
               self.deshabilitar_buzzer = 0
           if self.formaonda=="cuadrada":
               self.deshabilitar_buzzer = 1
               self.setcuadrada()
               self.deshabilitar_buzzer = 0
           self.ui.pulssubepemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsbajapemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           self.ui.pulssubepemf.setEnabled(True)
           self.ui.pulsbajapemf.setEnabled(True)


       if self.habilitarpemf == 0 and self.iniciarsesion == False:
           self.ui.pushButtonenablepemf.setStyleSheet(
               "background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.pemf = "desactivado"

           self.ui.pemftriangular.setEnabled(False)
           self.ui.pemfcuadrado.setEnabled(False)
           self.ui.textof3_4.setText('<font color="grey">triangular<font>')
           self.ui.textof3_5.setText('<font color="grey">cuadrada<font>')
           self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                             "border-image: url(Boton chico inactivo.png);")
           self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                             "border-image: url(Boton chico inactivo.png);")
           self.ui.pulssubepemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsbajapemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulssubepemf.setEnabled(False)
           self.ui.pulsbajapemf.setEnabled(False)

       if self.habilitarpemf == 0 and self.iniciarsesion == True:

           packet9 = bytearray()
           packet9.append(5)
           packet9.append(self.programavacio*self.activarvacio)
           packet9.append(0)
           packet9.append(self.programalaser*self.habilitarlaser)
           packet9.append(0)
           puertoserie.write(packet9)
           sleep(0.1)
           puertoserie.write(packet9)
           #print(packet9)
           self.ui.pushButtonenablepemf.setStyleSheet(
               "background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
           self.pemf="desactivado"
           self.ui.pemfcuadrado.setEnabled(False)
           self.ui.pemftriangular.setEnabled(False)
           self.ui.textof3_4.setText('<font color="grey">triangular<font>')
           self.ui.textof3_5.setText('<font color="grey">cuadrada<font>')
           self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                                "border-image: url(Boton chico inactivo.png);")
           self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                              "border-image: url(Boton chico inactivo.png);")
           self.ui.pulssubepemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
           self.ui.pulsbajapemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
           self.ui.pulssubepemf.setEnabled(False)
           self.ui.pulsbajapemf.setEnabled(False)
           if self.activarvacio==0 and self.habilitarlaser==0 and self.habilitarpemf==0:
               self.timercab.stop()


       if self.habilitarpemf== 1 and self.iniciarsesion == True:
           packet8 = bytearray()
           packet8.append(5)
           packet8.append(self.programavacio*self.activarvacio)
           packet8.append(self.programapemf*self.habilitarpemf)
           packet8.append(self.programalaser*self.habilitarlaser)
           packet8.append(0)
           puertoserie.write(packet8)
           #print(packet8)
           self.ui.pushButtonenablepemf.setStyleSheet("background-image: url(Boton tilde activo.png);\n" "border-image: url(Boton tilde activo.png);")
           self.pemf="activado"
           self.ui.pemfcuadrado.setEnabled(True)
           self.ui.pemftriangular.setEnabled(True)
           self.ui.textof3_4.setText('<font color="black">triangular<font>')
           self.ui.textof3_5.setText('<font color="black">cuadrada<font>')
           if self.formaonda == "triangular":
               self.deshabilitar_buzzer = 1
               self.settriangular()
               self.deshabilitar_buzzer = 0
           if self.formaonda == "cuadrada":
               self.deshabilitar_buzzer = 1
               self.setcuadrada()
               self.deshabilitar_buzzer = 0
           self.ui.pulssubepemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton arriba.png);")
           self.ui.pulsbajapemf.setStyleSheet(
               "background-image: url(trasnp.png);\n""border-image: url(Boton abajo.png);")
           self.ui.pulssubepemf.setEnabled(True)
           self.ui.pulsbajapemf.setEnabled(True)
           if (self.cabezalactivo==2 or self.cabezalactivo==3 or self.cabezalactivo==4) and (self.activarvacio==1 or self.habilitarpemf==1 or self.habilitarlaser==1):
             self.animacioncabezalmultitec()
       if self.bloquear_animaciones==0:
          self.animarpulsadores(self.ui.pushButtonenablepemf,35, 580, 27, 572, 50, 50)
       self.bloquear_animaciones = 0


   def bajarpemf(self,formadeonda):
       self.buzzer()
       # self.ui.pulsbajafrio.setGeometry(QtCore.QRect(507, 292, 102, 74))
       # self.ui.pulsbajafrio.setStyleSheet( "background-image: url(7 - Trabajando boton abajo instancia.png);\n" "border-image: url(7 - Trabajando boton abajo instancia.png);")
       self.contadorpemf = self.contadorpemf - 2
       if self.contadorpemf < 1:
           self.contadorpemf = 10

       self.contadorcontrolpemf(self.formaonda)
       #if self.contadorpemf == 0:
           #self.ui.programaspemf.setText("desactivado")
           # self.niveldefrioelegido = "desactivado"
           #self.programapemf = 0
       self.animarlabel2(self.ui.label_13, 20, 25)
       if self.iniciarsesion == True and self.habilitarpemf==1:
           #print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()
       self.animarpulsadores(self.ui.pulsbajapemf,510, 590, 502, 582,76,57)


   def modificar_pemf_durantetratamiento(self,contadorpemf):

       if contadorpemf == 0:
           #self.ui.label_13.setText("desactivado")
           self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                                "border-image: url(Boton chico inactivo.png);")
           self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                              "border-image: url(Boton chico inactivo.png);")


       if contadorpemf == 1:
           #self.ui.label_15.setText("programa 1")
           self.ui.label_13.setText("5 hz")
           if self.formaonda== "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 1
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 11

       if contadorpemf == 2:
           #self.ui.label_15.setText("programa 2")
           self.ui.label_13.setText("10 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 2
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 12

       if contadorpemf == 3:
           #self.ui.label_15.setText("programa 3")
           self.ui.label_13.setText("15 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 3
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 13

       if contadorpemf == 4:
           #self.ui.label_15.setText("programa 4")
           self.ui.label_13.setText("20 hz")
           if self.formaonda== "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 4
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 14

       if contadorpemf == 5:
           #self.ui.label_15.setText("programa 5")
           self.ui.label_13.setText("25 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 5
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 15

       if contadorpemf == 6:
           #self.ui.label_15.setText("programa 6")
           self.ui.label_13.setText("30 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 6
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 16

       if contadorpemf == 7:
           #self.ui.label_15.setText("programa 7")
           self.ui.label_13.setText("35 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 7
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 17

       if contadorpemf == 8:
           #self.ui.label_15.setText("programa 8")
           self.ui.label_13.setText("40 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 8
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 18

       if contadorpemf == 9:
           #self.ui.label_15.setText("programa 9")
           self.ui.label_13.setText("45 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 9
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 19

       if contadorpemf == 10:
           #self.ui.label_15.setText("programa 10")
           self.ui.label_13.setText("50 hz")
           if self.formaonda == "triangular":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 02.png);")
               self.programapemf = 10
           if self.formaonda == "cuadrada":
               self.ui.programaspemf.setStyleSheet("background-image: url(Ondas 03.png);")
               self.programapemf = 20

       if self.habilitarpemf == 0:
           #self.ui.label_13.setText("desactivado")
           self.ui.pemftriangular.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                                "border-image: url(Boton chico inactivo.png);")
           self.ui.pemfcuadrado.setStyleSheet("background-image: url(Boton chico inactivo.png);\n"
                                              "border-image: url(Boton chico inactivo.png);")

       # if self.contadorpemf == 0:
           #self.ui.label_13.setText("desactivado")
           #self.niveldefrioelegido = "desactivado"
       # self.programapemf = 0
       if self.iniciarsesion == True and self.habilitarpemf == 1:
           # print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()




   def subirpemf(self,formadeonda):

       self.buzzer()
       # self.ui.pulsarribavacum.setGeometry(QtCore.QRect(392, 292, 102, 74))
       # self.ui.pulsarribavacum.setStyleSheet("background-image: url(7 - Trabajando boton arriba instancia.png);\n" "border-image: url(7 - Trabajando boton arriba instancia.png);")
       self.contadorpemf = 2 + self.contadorpemf
       if self.contadorpemf > 10:
           self.contadorpemf = 2
       self.contadorcontrolpemf(self.formaonda)

       self.animarlabel2(self.ui.label_13, 20, 25)
       if self.iniciarsesion == True and self.habilitarpemf==1:
           #print(self.programapemf)
           self.prioridadenviodatossesion = 1
           self.enviardatosdesesionpemf()
       self.animarpulsadores(self.ui.pulssubepemf, 410, 590, 402, 582,76,57)

   def enviardatosdesesionpemf(self):
       self.timerest1.stop()
       self.timerest2.stop()
       self.prioridadenviodatossesion = 1
       if self.pausarsesion == 0 and (self.activarvacio == 1 or self.habilitarlaser==1 or self.habilitarpemf==1):
           self.seteosesion = False
           packet8 = bytearray()
           packet8.append(5)
           packet8.append(self.programavacio*self.activarvacio)
           packet8.append(self.programapemf*self.habilitarpemf)
           packet8.append(self.programalaser*self.habilitarlaser)
           packet8.append(0)
           puertoserie.write(packet8)
           sleep(0.1)
           puertoserie.write(packet8)
           #print(self.programavacio)
           # print(self.programapemf)
           # print(self.programalaser)
           #print(packet8)
           #print("progr vacio" + str(self.programavacio))
           #print("nivel de vacio" +str(self.nivelvacio))

           #print("progr pemf" + str(self.programapemf))
           #print("forma"+self.formaonda)

           #print(self.programavacio)
           self.prioridadenviodatossesion = 0
           self.limpiarbuffer()
           self.timerest1.start()
           self.timerest2.start()



   def potenciacero(self):
      if self.iniciarsesion==True:
       packet2 = bytearray()
       packet2.append(9)
       packet2.append(0)
       packet2.append(self.sumafrec * self.activarradio)
       packet2.append(self.cabezalactivo * self.activarradio)
       packet2.append(0)
       puertoserie.write(packet2)

       #self.ui.pushButtonenablefrec.setStyleSheet(
           #"background-image: url(Boton tilde inactivo.png);\n" "border-image: url(Boton tilde inactivo.png);")
       #self.bloqueoeleccionfrecuencias()
       #self.ui.pulssubepotencia.setStyleSheet(
           #"background-image: url(trasnp.png);\n""border-image: url(Boton arriba inactivo.png);")
       #self.ui.pulsbajapotencia.setStyleSheet(
          # "background-image: url(trasnp.png);\n""border-image: url(Boton abajo inactivo.png);")
       #self.ui.pulssubepotencia.setEnabled(False)
       #self.ui.pulsbajapotencia.setEnabled(False)


if __name__ == "__main__":
     app = QApplication(sys.argv)
     w = MyForm()
     w.show()
     sys.exit(app.exec_())


