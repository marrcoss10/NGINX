import requests
from bs4 import BeautifulSoup

metodo='GET'
uri="http://servidor-nginx"
cabecera={'Host':'servidor-nginx'}
respuesta=requests.request(metodo,uri,headers=cabecera,allow_redirects=True)

cuerpo=respuesta.content
documento=BeautifulSoup(cuerpo,"html.parser")
titulos=documento.find_all('p',{'class','coger'})

print(titulos)
