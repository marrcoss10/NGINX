import requests
from bs4 import BeautifulSoup

metodo='GET'
uri="http://servidor-nginx"
cabecera={'Host':'servidor-nginx'}
respuesta=requests.request(metodo,uri,headers=cabecera,allow_redirects=True)

cuerpo=respuesta.content
documento=BeautifulSoup(cuerpo,"html.parser")
titulos=documento.find_all('p',{'class','coger'})

div1=str(titulos[0]).split(">")
div2=str(titulos[1]).split(">")

div_num1=str(div1[1]).split("<")
div_num2=str(div2[1]).split("<")

n1=div_num1[0]
n2=div_num2[0]

print("A continuación se sumarán los números recogidos de la web: ")
print("Numero 1: " + n1)
print("Numero 2: " + n2)
suma=int(n1)+int(n2)
print(n1 + " + " + n2 + " = " + str(suma))
