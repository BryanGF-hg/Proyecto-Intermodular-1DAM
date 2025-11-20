# Abre una terminal e instala flask:
#pip install flask
# Flask es un microservidor web que nos permite generar HTML desde Python

from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
 ######################## ESTE ES UN BLOQUE
 cadena = '''
  <!DOCTYPE html>
<html lang="es">
 <head>
  <title>BRYANblog</title>
  <meta charset="UTF-8">
  <style>
   body{background:steelblue;color:steelblue;font-family:sans-serif;}
   header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
   header,footer{text-align:center;}
   main{color:black;} 
  </style>
 </head>
 
 <body>
  <header><h1>BRYANblog</h1></header>
  <main>
  '''
  
  ######################## ESTe BLOQUE se repite
 archivo = open("blog.json",'r')
 contenido = json.load(archivo)
 for linea in contenido:
  cadena += '''
   <article>
    <h3>'''+linea['titulo']+'''</h3>
    <time>'''+str(linea['fecha'])+'''</time>
    <p>'''+linea['autor']+'''</p>
    <p>'''+linea['contenido']+'''</p>
   </article>
   '''
   
   ######################## OTRO BLOQUE
 cadena += '''
  </main>
  <footer>Bryan Glot Fong 2025</footer>
 </body>
</html>
 '''
 ######################## NO OS OLVIDEIS DE RETURN
 return cadena
 
if __name__ == "__main__":
 aplicacion.run(debug=True)
