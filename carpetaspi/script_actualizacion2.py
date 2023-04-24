
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer, QTime, Qt
from gui_script_actualizar import *
from time import sleep
import os
import gdown
import zipfile
class miwidget(QDialog):

 def __init__(self):
    super().__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setMouseTracking(True)
    self.setCursor(Qt.BlankCursor)
    self.ui.label.setText("<span style=\" font-size:20pt; color:#f1f1f1;\">presione  para iniciar .<span>")
    self.ui.pushButton.pressed.connect(self.cartelactualizar)
    self.ui.pushButton.released.connect(self.download_data_gdown)
    self.estadoactualizacion=""
    #self.show()

 def cartelactualizar(self):
     self.ui.label.setText("<span style=\" font-size:20pt; font-weight:600; color:#464646;\">Actualizando.. <span><span style=\" font-size:20pt; color:#f1f1f1;\">aguarde un instante por favor. Una vez finalizado el proceso, el sistema se reiniciará.<span> <span style=\" font-size:20pt; font-weight:600; color:red;\">NO APAGUE EL EQUIPO <span>")


 def download_data_gdown(self):
    #file_id = "1wd4YyxDHTb6Y22tSfzUYmDcGE8fj3kbo"
    url = f"https:drive.google.comuc?id={file_id}"
    #data_zip = os.path.join("hometexel", "data.zip")
    #gdown.download(url, data_zip, quiet=False)

    with zipfile.ZipFile(data_zip, "r") as zip_ref:
        zip_ref.extractall("hometexel")
    os.system("reboot")
    return




if __name__ == "__main__":
     app = QApplication(sys.argv)
     w1 = miwidget()
     w1.show()
     sys.exit(app.exec_())