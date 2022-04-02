from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
from smtplib import SMTP
from email.message import EmailMessage
import bcrypt
import re

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'baselogin'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/entrar',methods=["GET","POST"])
def entrar():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("inicio.html")
            else:
                return "correo o contraseña invalidos"
        else:
            return "usuario no encontrado porfavor registrese y vuelva a intentarlo"
    else:
        return render_template("entrada.html")

@app.route('/cerrar', methods=["GET", "POST"])
def cerrar():
    session.clear()
    return render_template("inicio.html")

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    if request.method == 'GET':
        return render_template("registros.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        imagen = request.form['imagen']
        celular = request.form['celular']
        direccion = request.form['direccion']
        descripcion = request.form['descripcion']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, imagen, celular, direccion, descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,email,hash_password,imagen,celular,direccion,descripcion,))
        
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']

        msg = EmailMessage()
        msg.set_content('Señor usuario bienvenido',)

        msg['Subject'] = 'confirmcion correo'
        msg['From'] = "brayanbotina2020@itp.edu.co"
        msg['To'] = email = request.form['email']

        # Reemplaza estos valores con tus credenciales de Google Mail
        username = 'brayanbotina2020@itp.edu.co'
        password = '1006947880'

        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

        server.quit()
        return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.secret_key = "kamata16angulo"
    app.run(debug=True)