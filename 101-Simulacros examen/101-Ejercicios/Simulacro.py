1.-Introducción:
Debemos crear un sitio web local que nos permita mostrar mediante Python la base de datos y que muestre al menos un artículo que corresponda a la tabla que hemos creado

2.-Desarrollo:
Importamos las librerias que nos permite conectar a base de datos y la libreria que nos permita crear un servidor web local:
```
import mysql.connector
from flask import Flask
```

Me conecto a la base de datos:
```
conexion = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Contrasena123$",
    database="portafolio_simulacro"
)   
```

Creo un cursor que nos permita conectarnos a la base de datos y también creamos una aplicación Flask que veremos en la web:
```
cursor = conexion.cursor()
app = Flask(__name__)
```

Atrapamos la ruta raiz, definimos una función donde luego devolveremos todo el contenido definido:
```
@app.route("/")
def html():                             
```

Ejecutamos el contenido que veremos:
```
 cursor.execute(''' SELECT * FROM vista_piezacategoria; ''')
```

Hacemos una variable que guarda la vista en una lista:
```
 filas = cursor.fetchall()
```

Definimos la primera cadena donde introducimos el código HTML que hemos hecho anteriormente siguiendo la estructura sintáctica correspondiente y estilo CSS interno hasta el inicio del main:
```
 cadena = '''
  <!DOCTYPE HTML>
<html lang="es">
<head>
 <title>Curriculum Simulacro</title>
 <meta charset="utf-8">
 
 <style>
  html,body{background:grey;font-family:sans-serif;}
  header,main,footer{
   background:LightCyan;
   padding:20px;
   width:820px;
   margin:auto;
   text-align:center;
  }
  main{
   display:grid;
   grid-template-columns:auto auto auto;
   gap:20px;
  }
  img{
   width:200px;
  }
 </style>
</head>

<body>
 <header>
  <h1>Bryan Glot Fong</h1>
  <h2>bryan@gmail.com</h2>
 </header>
 <main>
 '''
```

Para cada elemento de la lista, mostraremos la información de la vista a la que nos hemos conectado:
```
 for fila in filas: 
  cadena += '''
   <article>
    <h3>'''+str(fila[0])+'''</h3>
    <p>'''+str(fila[1])+'''</p>
    <p>'''+str(fila[3])+'''</p>
    <img src="'''+str(fila[2])+'''">
    <p>'''+str(fila[4])+'''</p>
    <p>'''+str(fila[5])+'''</p>
    <p>'''+str(fila[6])+'''</p>
   </article>  
  '''
```

Para la tercera cadena, colocamos el cierre de las etiquetas;
```
  cadena += '''
  </main>
  <footer>
   (c) 2025 Bryan Glot Fong
  </footer>
 </body>
 </html>
  '''
```

Devolvemos la cadena como HTML para mostrarla en un navegador web:
```
 return cadena
```

Si este es el archivo principal, se ejecuta en la web:
```
if __name__ == "__main__":
 app.run(debug=True)
```

3.-Aplicación:
Podemos aplicar el caso de crear un sitio web conectado a Python para que haga de medio entre el desarrollo web y la base de datos para crear sitios de almacenamiento de datos.

4.-Conclusión:
El propósito principal es crear una página web que presenta datos de forma estructurada con HTML y visual con CSS. Al conectarse a la base de datos, extrae los datos registrados y construimos el HTML con ellos que mediante Python que sirve de medio, se logra una solución para mostrar contenido sin necesidad de modificar manualmente el código cada vez que cambian los datos. Este programa permite integrar backend y frontend de forma sencilla, facilitando la creación de aplicaciones interactivas y escalables.

Código:
```
import mysql.connector                      # Importo el conector a base de datos
from flask import Flask

conexion = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Contrasena123$",
    database="portafolio_simulacro"
)                                                           # Me conecto a la base de datos

cursor = conexion.cursor()                                  # Creo un cursor
app = Flask(__name__)                                       # Creo una aplicacion Flask (web)

@app.route("/")                                              # Atrapo la ruta raiz (/)
def html():                                                  #Defino una función
 cursor.execute(''' SELECT * FROM vista_piezacategoria; ''') # Pido el contenido de la vista

 filas = cursor.fetchall()                                   # Lo guardo en una lista
 
 
 ########## AQUI PONGO EL INICIO HASTA EL MAIN
 cadena = '''
  <!DOCTYPE HTML>
<html lang="es">
<head>
 <title>Curriculum Simulacro</title>
 <meta charset="utf-8">
 
 <style>
  html,body{background:grey;font-family:sans-serif;}
  header,main,footer{
   background:LightCyan;
   padding:20px;
   width:820px;
   margin:auto;
   text-align:center;
  }
  main{
   display:grid;
   grid-template-columns:auto auto auto;
   gap:20px;
  }
  img{
   width:200px;
  }
 </style>
</head>

<body>
 <header>
  <h1>Bryan Glot Fong</h1>
  <h2>bryan@gmail.com</h2>
 </header>
 <main>
 '''
 
 ########## AQUI PONGO LO QUE SE REPITE
 for fila in filas:                                          # Para cada elemento de la lista
  cadena += '''
   <article>
    <h3>'''+str(fila[0])+'''</h3>
    <p>'''+str(fila[1])+'''</p>
    <p>'''+str(fila[3])+'''</p>
    <img src="'''+str(fila[2])+'''">
    <p>'''+str(fila[4])+'''</p>
    <p>'''+str(fila[5])+'''</p>
    <p>'''+str(fila[6])+'''</p>
   </article>  
  '''

  
 ########## AQUI PONGO EL FINAL
  cadena += '''
  </main>
  <footer>
   (c) 2025 Bryan Glot Fong
  </footer>
 </body>
 </html>
  '''
 return cadena                                               #Devuelvo la cadena como HTML en la web
 
if __name__ == "__main__":                                  #Si este es el archivo principal
 app.run(debug=True)                                        #Ejecuta la web
```
