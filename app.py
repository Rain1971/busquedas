from urllib.request import urlopen
import urllib.request
from random import choice
import time

link = "https://www.google.com/search?hl=es&q=cepillo+de+dientes+bambu+recomendado+lov'yc"
lst = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']

def CargaLinea( nombre ):
   fichero = nombre + ".txt"
   lines = open( fichero ).read().splitlines()
   return choice( lines )

numero = 0
while True:
   try:
      agente = CargaLinea( choice( lst ) )
      req = urllib.request.Request(
         link, 
         data=None, 
         headers={
            'User-Agent': agente
         }
      )
      numero += 1
      with urllib.request.urlopen( req ) as f:
         print( "OK -> " + str(numero) )
         if numero > 1000:
            numero = 0
      time.sleep( 20 )
   except urllib.error.URLError as e:
      print(e.reason)
