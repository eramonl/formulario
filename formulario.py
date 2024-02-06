from flask import Flask
from flask import render_template
from flask import request
import sys
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


lista = {
"Mercedes":"mcast386@xtec.cat",
"Rayane":"rayane@rayane.sa",
"Mohamed":"moha@gmail.com",
"Jad":"jad@gmail.com",
"Oriol":"joam@gmail.com",
"Elias":"hola123@gmail.com",
"Armau":"arnau@gmail.com",
"Asdrúbal":"asdrubal@gmail.com",
"Adrian":"pedrosanchez@asix2.com",
"Eric":"eric@gmail.com",
"Emma":"pacosanz@gmail.com",
"nishwan":"nishwan@gmail.com",
"Javi":"javi@gmail.com",
"Novel":"novelferreras49@gmail.com",
"Bruno":"elcigala@gmail.com",
"David":"argentino@gmail.com",
"Judit":"judit@gmail.com",
"Joao":"joao@gmail.com",
"Laura":"laura@gmail.com",
"enrico":"123@gmail.com",
"Joel":"joelcobre@gmail.com",
"Aaron":"aaron@gmail.com",
"Moad":"moad@gmail.com"
}

def getmaillista(nom):
    if nom in lista:
        return lista[nom]
    else:
        return "No esta"

@app.route('/getmail',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      email = getmaillista(user)# Inicializar la variable de email a None

      return render_template('resultado.html', username=user, title="hola", email=email)
   else:
      #user = request.args.get('name') si es
      return render_template('formulario.html')

if __name__ == '__main__':
   app.run(debug = True)