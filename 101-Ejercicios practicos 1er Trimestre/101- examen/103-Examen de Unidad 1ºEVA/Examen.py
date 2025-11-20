1.-Introducción:
 Este sitio web desarrollado con Flask y MySQL nos ayudará a mostrar una vista integrada de la tablas piezas y categorías almacenadas en una base de datos que hemos trabajado anteriormente, lo cual nos facilita la comprensión de la relación entre ambos elementos.

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
    user="Usuario-portafolio",
    password="Contrasena123$",
    database="portafolioexamen"
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
 cursor.execute(''' SELECT * FROM piezas_categorias; ''')
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
   <title>Portafolio</title>
   <meta charset="utf-8">
   <style>
    body{background:LightSkyBlue;}
    main{width:1020px;background:white;margin:auto;padding:25px;display:flex;}
    header{text-align:center;}
    footer{padding:3px;text-align:center;background:CornflowerBlue;}

   	#izquierda{background:LightCyan;padding:20px;color:black;width:200px;}
    #derecha{padding:20px;width:500px;display:flex;justify-content:flex-start;align-items: center;}
	  #derecha article{display:grid;grid-template-columns: auto auto auto auto auto;gap:20px;background:RoyalBlue;}

  </style>
 </head>
<body>
 <header>
  <h1>Bryan Glot Fong</h1>
  <h2>Estudiante en CEAC FP</h2>
 </header>
 <main>
  <section id="izquierda">
  <h3>Propiedades de las tablas:</h3>
    <article>
	 <h3>Tabla Piezas</h3>
	 <ul>
	  <li>Identificador</li>
	  <li>Título</li>
	  <li>Descripción</li>
	  <li>Fecha</li>
	  <li>id_categoria</li>
	 </ul>
    </article>
    <article>
	 <h3>Tabla Categorias</h3>
	 <ul>
	  <li>Identificador</li>
	  <li>Nombre</li>
	 </ul>
    </article>
  </section>    
  <section id="derecha">
   <div id="contenedorderecha">
 '''
```

Para cada elemento de la lista, mostraremos la información de la vista cruzada a la que nos hemos conectado:
```
 for fila in filas: 
  cadena += '''
      <article>
       <ul>Titulo:'''+str(fila[0])+'''</ul>
       <ul>Descripción:'''+str(fila[1])+'''</ul>
       <ul>Fecha:'''+str(fila[2])+'''</ul>
       <ul>Nombre de Categoria:'''+str(fila[3])+'''</ul>
      </article>
  '''
```

Para la tercera cadena, colocamos el cierre de las etiquetas;
```
  cadena += '''
    </div>
  </section>
 </main>
 <footer>
	<a href="https://facebook.com/****">Facebook</a>
	<a href="https://github.com/****">GitHub</a>
	<a href="https://linkeldn.com/****">Linkeldn</a>	
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
Podemos aplicar este tipo de sitio web que integra HTML,CSS y Python en sistemas de gestión de portafolio, proyectos de diseño de base de datos para un sistema de inventario, una app móvil para consultar tablas hechas en bases de datos usando GitHub Pages, un menú con submenus interactivos para análisis de datos de un portafolio.

4.-Conclusión:
Al hacer este ejercicio, nos permite integrar una base de datos relacional con una interfaz web utilizando Python, Flask y MySQL.
La visualización de datos cruzados nos ayudan a ver una mejor organización y presentación de la información. Poco a poco, vamos a automatizar el proceso de conectar el backend con el frontend en sitios web.

Código:
```
import mysql.connector
from flask import Flask

conexion = mysql.connector.connect(
    host="localhost",
    user="Usuario-portafolio",
    password="Contrasena123$",
    database="portafolioexamen"
)

cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")
def html():
 #Ejecutamos la vista de la petición cruzada hecha con las dos tablas, piezas y categorias:
 cursor.execute(''' SELECT * FROM piezas_categorias; ''')
 filas = cursor.fetchall() 

 cadena = '''
<!DOCTYPE HTML>
<html lang="es">
 <head>
   <title>Portafolio</title>
   <meta charset="utf-8">
   <style>
    body{background:LightSkyBlue;}
    main{width:1020px;background:white;margin:auto;padding:25px;display:flex;}
    header{text-align:center;}
    footer{padding:3px;text-align:center;background:CornflowerBlue;}

   	#izquierda{background:LightCyan;padding:20px;color:black;width:200px;}
    #derecha{padding:20px;width:500px;display:flex;justify-content:flex-start;align-items: center;}
	  #derecha article{display:grid;grid-template-columns: auto auto auto auto auto;gap:20px;background:RoyalBlue;}

  </style>
 </head>
<body>
 <header>
  <h1>Bryan Glot Fong</h1>
  <h2>Estudiante en CEAC FP</h2>
 </header>
 <main>
  <section id="izquierda">
  <h3>Propiedades de las tablas:</h3>
    <article>
	 <h3>Tabla Piezas</h3>
	 <ul>
	  <li>Identificador</li>
	  <li>Título</li>
	  <li>Descripción</li>
	  <li>Fecha</li>
	  <li>id_categoria</li>
	 </ul>
    </article>
    <article>
	 <h3>Tabla Categorias</h3>
	 <ul>
	  <li>Identificador</li>
	  <li>Nombre</li>
	 </ul>
    </article>
  </section>    
  <section id="derecha">
   <div id="contenedorderecha">
 '''
 for fila in filas: 
  cadena += '''
      <article>
       <ul>Titulo:'''+str(fila[0])+'''</ul>
       <ul>Descripción:'''+str(fila[1])+'''</ul>
       <ul>Fecha:'''+str(fila[2])+'''</ul>
       <ul>Nombre de Categoria:'''+str(fila[3])+'''</ul>
      </article>
  '''

 cadena += '''
    </div>
  </section>
 </main>
 <footer>
	<a href="https://facebook.com/****">Facebook</a>
	<a href="https://github.com/****">GitHub</a>
	<a href="https://linkeldn.com/****">Linkeldn</a>	
 </footer>
</body>
</html>
 '''  
 return cadena
 
if __name__ == "__main__":
 app.run(debug=True) 
``` 
