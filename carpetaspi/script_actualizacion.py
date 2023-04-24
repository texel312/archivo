#import git
#import shutil
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer, QTime, Qt
from gui_script_actualizar import *
from time import sleep
import os
import sqlite3 as sql




class miwidget(QDialog):

 def __init__(self):
    super().__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setMouseTracking(True)
    self.setCursor(Qt.BlankCursor)
    self.ui.label.setText("<span style=\" font-size:20pt; color:#f1f1f1;\">pulse actualizar para comenzar el proceso.<span>")
    self.ui.pushButton.pressed.connect(self.cartelactualizar)
    self.ui.pushButton.released.connect(self.descargar_de_gihub)
    self.estadoactualizacion=""
    #self.show()

 def cartelactualizar(self):
     self.ui.label.setText("<span style=\" font-size:20pt; font-weight:600; color:green;\">Actualizando.. <span><span style=\" font-size:20pt; color:#f1f1f1;\">aguarde un instante por favor. Una vez finalizado el proceso, el sistema se reiniciará.<span> <span style=\" font-size:20pt; font-weight:600; color:red;\">NO APAGUE EL EQUIPO <span>")


 def descargar_de_gihub(self):
    try:
     #Clonar el repositorio de GitHub
     repo = git.Repo.clone_from("https://github.com/texel312/archivo.git", "/home/texel/temporal")
     # Copiar la carpeta del repositorio clonado en la Raspberry Pi a /home/mi_carpeta
     shutil.copytree("/home/texel/temporal/carpetaspi", "/home/texel/qdial2")

     # Eliminar el repositorio clonado
     shutil.rmtree("/home/texel/temporal")
     os.system("sudo cp -R /home/texel/qdial2/* /home/texel/")
     shutil.rmtree("/home/texel/qdial2")
     os.system("sudo chmod -R 777 /home/texel")

     connection = sql.connect('versionnueva.db')
     cur = connection.cursor()
     instruccion = 'SELECT version FROM codigonuevo'
     cur.execute(instruccion)
     versionnueva = cur.fetchone()
     connection.commit()
     connection.close()

     conn = sql.connect('versionactual.db')
     c = conn.cursor()
     c.execute("UPDATE codigo SET version= ?", (versionnueva[0],))
     conn.commit()
     conn.close()
     #os.system("reboot")
    except:
      os.system("sudo cp -R /home/texel/backup/* /home/texel/")
      os.system("sudo chmod -R 777 /home/texel")
      os.system("reboot")
    finally:
      os.system("reboot")





if __name__ == "__main__":
     app = QApplication(sys.argv)
     w1 = miwidget()
     w1.show()
     sys.exit(app.exec_())