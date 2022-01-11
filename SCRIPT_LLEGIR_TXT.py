########  SCRIPT LLEGIR ARXIU TXT By Andrés Manso  #############################

from io import open  # IMPORTO modul IO i metode "OPEN" ( permet obrir un arxiu extern)

arxiu_texte=open("names.txt","r")  # Nom de l' arxiu i mode de obertura , en aquest cas LECTURA (READ)

linea=arxiu_texte.readlines() # emmagatzema en una llista amb el nom "linea"

arxiu_texte.close()  # Tanco arxiu després de manipulació

for i in linea:  # BLUCLE FOR per recorrer la llista i imprimir per pantalla
	print(i)


#print(linea)
