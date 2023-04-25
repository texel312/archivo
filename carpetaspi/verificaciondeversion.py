import git
import shutil
import os
import sqlite3 as sql
import ftplib
variableauxiliar=0

def cargarversionactual():
  try:

      # Clonar el repositorio de GitHub
      repo = git.Repo.clone_from("https://github.com/texel312/archivo.git", "/home/texel/temporal")
      # Copiar la carpeta del repositorio clonado en la Raspberry Pi a /home/mi_carpeta
      shutil.copytree("/home/texel/temporal/nuevaversion", "/home/texel/qdial2")

      # Eliminar el repositorio clonado
      shutil.rmtree("/home/texel/temporal")
      os.system("sudo cp -R /home/texel/qdial2/* /home/texel/")
      shutil.rmtree("/home/texel/qdial2")
      os.system("sudo chmod -R 777 /home/texel")



  except:
    os.system("sudo cp -R /home/texel/backup/* /home/texel/")
    os.system("sudo chmod -R 777 /home/texel")
    os.system("reboot")
  finally:
    os.system("sudo chmod 777 -R /home/texel")
    os.system("sudo python3 /home/texel/mainVR.py")


cargarversionactual()


