from flask import Flask, render_template, request # Tomo parametros de la url

app =Flask(__name__)

@app.route("/")
def inicio():
 return render_template("index.html")

@app.route("/envio")
def envio():
 nombre = request.args.get("nombre")
 apellidos = request.args.get("apellidos")
 print(nombre,apellidos)
 return "nombre:"+nombre+" - apellidos:"+apellidos
 
if __name__ == "__main__":
 app.run(debug=True)
 
# http:127.0.0.1:5000/?nombre=Bryan%20Glot%20Fong
# %20 = espacio (en url)
