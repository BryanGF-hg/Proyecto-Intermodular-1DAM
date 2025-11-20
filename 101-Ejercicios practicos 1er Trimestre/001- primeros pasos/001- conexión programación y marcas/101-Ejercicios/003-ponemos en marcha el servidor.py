#sudo apt install python3-pip - si no tenéis PIP en Ubuntu
#pip install flask - Windows
#pip3 install flask --bre(a)k-system-packages - Linux o MacOS

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():



if __name__ == "__main__":
 aplicacion.run(debug=True)
