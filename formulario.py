from flask import Flask
from flask import render_template
from flask import request
import sys
from flask import Flask, redirect, url_for, request
import mysql.connector
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

class ConexionDB:
    def __init__(self, host, user, password, database):
      self.connection = mysql.connector.connect(
         host=host,
         user=user,
         password=password,
         database=database
      )


 def agregar_usuario(self):
        cursor = self.conexion.obtener_cursor()
        nombre = str(input("Ingresa el nombre del nuevo usuario: "))
        correo = str(input("Ingresa el correo del nuevo usuario: "))
        cursor.execute("INSERT INTO alumnos (Nombre, Correo) VALUES (%s, %s)", (nombre, correo))
        self.conexion.connection.commit()
        print("Usuario agregado correctamente.")

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

@app.route('/agregar',methods = ['ADD'])
agregar_usuario


if __name__ == '__main__':
   app.run(debug = True)