import mysql.connector
#definim en una variable de tipus dict, la clau serà el nom i el valor serà el email
#posem els noms i els correus electrònics de la classe
#CONSTANTS pel resultat de les fucions


class ConexionDB:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=programa
        )


NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"

# funció getmaildict rep el nom com paràmetre i retorna el mail
# si no el troba retorna un string "NOTROBAT"
def conectdb():
      mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="programa"
            )
      return mydb

# funció getmaildict rep el nom com paràmetre i retorna el mail
# si no el troba retorna un string "NOTROBAT"
def getmaildic(Nombre):
      mydb = conectdb()
      if request.method == 'POST':
            user = request.form['Nombre']
            mycursos = mydb.cursor()
            mycursos.execute("SELECT Correo FROM alumnos WHERE Nombre = %s",(user,))
            myresult = mycursos.fetchall()
            if myresult:
                  for x in myresult:
                        mail=x
                        return render_template('resultadogettmail.html',mail=mail,user=user)
            else:
                  return NOTROBAT
      else:
            return render_template('formulario.html')

# addmaildict rep el nom i el email com paràmetres, i els afegeix al diccionari
# si ja existeix retorna un string "JAEXISTEIX"
# quan va bé retorna string "AFEGIT"
# si el paràmetre modif es True, quan ja existeix però és diferent, el modifica i retorna string "MODIFICAT"
def addmaildict(nom,correu,modif=False):
      oldcorreu = getmaildict(nom)
      if oldcorreu == NOTROBAT:
        diccionari[nom]=correu
        return AFEGIT
      elif (oldcorreu != correu and modif):
        diccionari[nom]=correu
        return MODIFICAT
        return JAEXISTEIX
   