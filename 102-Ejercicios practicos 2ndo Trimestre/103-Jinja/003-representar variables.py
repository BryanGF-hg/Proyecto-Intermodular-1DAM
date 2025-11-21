from flask import Flask, render_template

app =Flask(__name__)

@app.route("/")
def inicio():
 #mi_noombre es la variable que está en Python
 mi_nombre = "Bryan Glot Fong"
 # nombre es la variable que lanzo a la plantilla
 return render_template("variable.html",nombre=mi_nombre)
 
if __name__ == "__main__":
 app.run(debug=True)
