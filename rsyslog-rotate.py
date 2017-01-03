#!/usr/bin/env python

'''Script para rotar los logs, ya que estos logs son especificos y cambian
el formato del nombre de fichero'''

# Necesitamos el modulo os para pocer utilizar el walk

import os, gzip, shutil, glob, datetime

today=datetime.date.today()
yesterday=today - datetime.timedelta(days=1)
formatted=yesterday.strftime("%Y-%m-%d")

# El directorio donde se almacenanlogs

dir="/var/remotelog"

# Definimos la funcion de rotado

def Rotacion(fichero):
  with open(fichero, 'rb') as f_in, gzip.open(fichero+'.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

for root,files,dir in os.walk(dir):
  os.chdir(root)
  for log in  glob.glob("*"+formatted):
    Rotacion(log)
