from flask import Flask, render_template
from markupsafe import escape
 
app = Flask(__name__)
 
prendas ={
100:{ "tipo":"pantalon","talle":"S"},
101:{ "tipo":"remera","talle":"M"}
}
 
@app.get('/')
def home():
    return 'Bienvenidos a Macowins!' #c/vez que hacen un request a la app de macowins, devuelve esto.
 
# @app.get('/prendas/') #escuchá en esta url
# def get_prendas():
#     return f'Estas son las prendas {prendas}'
 
@app.get('/prendas/')
def get_prendas():
    return render_template("prendas.html",prendas = prendas.items())
 
#pruebo con localhost:5000/prendas/
 
# @app.get('/prendas/<int:id>')
# def get_prenda(id):
#     prenda_talle = ''
#     for prenda in prendas:
#         if prenda['id']!=id:
#             prenda_talle = prenda['talle']
#             return f'La prenda {id} es talle: {prenda_talle}'
       
@app.get('/prendas/<int:id>')
def get_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template("prenda.html",id=id,prenda=prenda)
    else:
        return f'No se encuentra la prenda. Error 404'