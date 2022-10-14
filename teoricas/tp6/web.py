import requests

r_prendas = requests.get('https://macowins-server.herokuapp.com/prendas')
prendas = r_prendas.json()
r_ventas = requests.get('https://macowins-server.herokuapp.com/ventas')
ventas = r_ventas.json()
print(prendas)
print("\n",len(ventas))
print("\n",r_prendas.headers)
#pantalones porfa
print("\n",requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon').json())
#pantalon talle 42
print("\n",requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=42').json())

"""
OPTIONS: consultar meta-datos o configuraciones de HTTP
GET: consultar un contenido sin efecto
POST: crear un contenido
PUT: actualizar de forma total un contenido
PATCH: actualizar de forma parcial un contenido
DELETE: eliminar un contenido
"""
url = "https://macowins-server.herokuapp.com/prendas"
data = {"id":45, "tipo": "gorro","talle":"12"}
# print("\n",requests.post(url, data=data))