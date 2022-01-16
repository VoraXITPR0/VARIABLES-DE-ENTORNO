########  SCRIPT LLEGIR ARXIU TXT UTILITZO VARIABLE ENTORN crear HASH MD5,SHA1,SHA256,SHA512 iSHA3-512 By Andrés Manso  #############################

from io import open  # IMPORTO modul IO i metode "OPEN" ( permet obrir un arxiu extern)
import hashlib       # IMPORTO LLIBRERIA HASHLIB
import os       # IMPORTO  LLIBRERIA  
from sys import argv
import sys




argumento =str(sys.argv)
print("Print str :",str(sys.argv))
argumento =str(sys.argv[1])
print("Print argumento: ",argumento)

#print("Print str :",str(sys.argv))
#argumento =str(sys.argv[1])
#print("Print argumento: ",argumento)
#os.environ['VE'] = "/data/names.txt"    # VARIABLE DE ENTORNO VE asignamos  el nom de l' arxiu names.txt en DOCKER  "/data/names.txt"
argumento="/data/"+argumento
os.environ['VE'] =argumento # "names.txt"

#arxiu_texte = open(os.environ.get('VE'))
os.environ.get('VE')



arxiu_texte = open(os.environ.get('VE'))
#arxiu_texte=open("/data/names.txt","r")  # Nom de l' arxiu i mode de obertura , en aquest cas LECTURA (READ)

lineas = arxiu_texte.readlines()    #  LLEGIR LINEAS ARXIU 

h = hashlib.new('md5')    # Es  crea  objecte de clase hash amb HASH MD5, SHA1, SHA256, SHA512, SH3-512
j = hashlib.new('sha1')
k = hashlib.new('sha256')
l = hashlib.new('sha512')
m = hashlib.new('sha3-512')
for linea in lineas:
  i=linea
  linea = str.encode(linea)  # Es converteix el string en un byte string
  print("El resultat en hexadecimal es del hash  MD5: "+ i +" es: " + str(h.hexdigest()))   # IMPRESSIÓ HASH en HEXADECIMAL
  print("El resultat en hexadecimal es del hash  SHA-1: "+ i +" es: " + str(j.hexdigest()))
  print("El resultat en hexadecimal es del hash  SHA-256: "+ i +" es: " + str(k.hexdigest()))
  print("El resultat en hexadecimal es del hash  SHA-512: "+ i +" es: " + str(l.hexdigest()))
  print("El resultat en hexadecimal es del hash  SHA3-512: "+ i +" es: " + str(m.hexdigest()))
  h.update(linea)               # S'  agregan les  linea de l' arxiu  a l' objecte hash  
  j.update(linea)
  k.update(linea)
  l.update(linea)
  m.update(linea)

arxiu_texte.close() # Tanco arxiu després de manipulació



######################################################################################################




