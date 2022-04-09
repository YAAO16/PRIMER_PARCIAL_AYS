from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL,MySQLdb
from smtplib import SMTP
from email.message import EmailMessage
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import bcrypt
import re
import hashlib


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
    if request.method == 'GET':
        return render_template("entrada.html")
    
    else:
        email = request.form.get('correo')
        password = request.form.get('password')
        password = hashlib.sha1(password.encode()).hexdigest()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s and password=%s and estado='1'", (
            email,
            password,
            ))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario:
            if password == usuario["password"]:
                session['email']=usuario['email']
                session['password']=usuario['password']
                return render_template("entrar.html")
            else:
                flash("correo o contraeña incorrectos")
                return render_template("usuario o contraseña incorrectos")
        
        else:
            flash("alguno de los campos son incorretos")
            return render_template("entrar.html")
    
        

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
        password_encri = bcrypt.hashpw(password, bcrypt.gensalt())
        imagen = request.form['imagen']
        celular = request.form['celular']
        direccion = request.form['direccion']
        descripcion = request.form['descripcion']

        is_valid = True
    
        if name =="":
            flash("es requerido el nombre")
            is_valid= False
        
        if email =="":
            flash("es requerido el email")
            is_valid= False
        
        if password =="":
            flash("es requerido la contraseña")
            is_valid= False
    
        if imagen =="":
            is_valid= False

        if celular =="":
            flash("es requerido el telefono")
            is_valid= False 

        if direccion =="":
            flash("es requerido la direccion")
            is_valid= False  
        
        if descripcion =="":
            flash("es requerida la descripcion")
            is_valid= False

        if is_valid == False:
            print("los datos no son validos")
            return render_template("registros.html")

        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, imagen, celular, direccion, descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,email,password_encri,imagen,celular,direccion,descripcion,))
        
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']

        msg = EmailMessage()
        msg.set_content('Señor usuario bienvenido',)

        msg['Subject'] = 'confirmcion correo'
        msg['From'] = ""
        msg['To'] = email

        # Reemplaza estos valores con tus credenciales de Google Mail
        username = ''
        password = ''

        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

        server.quit()

        return redirect(url_for('inicio'))

@app.route("/entrar/confirmar/<token>")
def confirmarEmail(token):
    try:
        email=s.loads(token, salt='emcof', max_age=60)
        cur = mysql.connection.cursor()()
        cur.execute("UPDATE users SET estado='1' WHERE email='"+email+"'")
        cur.close()
    except SignatureExpired:
        cur = db.cursor()
        cur.execute("DELETE FROM users WHERE email='"+email+"' AND estado='0'")
        cur.close()
        return "<h1>EXPIRO EL TIEMPO VUELVA A INTERNTARLO</h1>"
    return "<h1>"+email+"  CONFIRMADO BIENVENIDO</h1>"

if __name__ == '__main__':
    app.secret_key = "kamata16angulo"
    app.run(debug=True)