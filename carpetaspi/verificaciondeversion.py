
import os
import sqlite3 as sql
import ftplib
variableauxiliar=0

def cargarversionactual():
  try:
      os.system("sudo chmod 777 -R /home/texel")
      os.system("sudo python3 /home/texel/mainVR.py")
      #connection = sql.connect('versionactual.db')
      #cur = connection.cursor()
      #instruccion = 'SELECT version FROM codigo'
      #cur.execute(instruccion)
      #version = cur.fetchone()
      #connection.commit()
      #connection.close()

      #connection = sql.connect('versionnueva.db')
      #cur = connection.cursor()
      #instruccion = 'SELECT version FROM codigonuevo'
      #cur.execute(instruccion)
      #versionnueva = cur.fetchone()
      #connection.commit()
      #connection.close()

      #if version[0] != versionnueva[0]:
        #os.system("sudo python3 /home/texel/script_actualizacion.py")
  except:
    os.system("sudo cp -R /home/texel/backup/* /home/texel/")
    os.system("sudo chmod -R 777 /home/texel")
    os.system("reboot")
  #finally:
  # os.system("sudo chmod 777 -R /home/texel")
    #os.system("sudo python3 /home/texel/mainVR.py")


cargarversionactual()


