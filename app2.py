from urllib.request import urlopen
import urllib.request
from random import choice
import time
import requests
import json

link = "http://suggestqueries.google.com/complete/search?hl=es&q=cepillo+de+dientes+bambu+recomendado+lov'yc"
query = "cepillo de dientes bambu recomendado lovyc"
lang = "es"
lst = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']

def CargaLinea( nombre ):
   fichero = nombre + ".txt"
   cliente = nombre.lower()
   lines = open( fichero ).read().splitlines()
   return choice( lines ), cliente

numero = 0
while True:
   try:
    time.sleep( 1 )
    agente, cliente = CargaLinea( choice( lst ) )
    URL="http://suggestqueries.google.com/complete/search"
    PARAMS = {"client": "firefox",
              "hl":lang,
              "q":query}
    headers = {'User-agent':agente}
    numero += 1
    if numero > 1000:
         numero = 1
    
    try:
      response = requests.get(URL, params=PARAMS, headers=headers)
      if response.status_code == 200:
          suggestedSearches = json.loads(response.content.decode('utf-8'))[1]
          print( numero )
      else:
          print("ERR1")
    except:
      print("ERR2")
   
   except urllib.error.URLError as e:
      print(e.reason)