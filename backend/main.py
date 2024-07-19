from flask import Flask, request, jsonify, session, render_template, url_for
from flask_cors import CORS
from flask_session import Session
import mysql.connector
import json
import datetime
import locale
import bcrypt
from dateutil import parser
from datetime import datetime, timedelta
import base64
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import os
from dotenv import load_dotenv




locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

CORS(app)  
# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les valeurs des variables d'environnement
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')


#session config
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
Session(app)

# mail config
app.config['MAIL_SERVER'] = 'in-v3.mailjet.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'd2e9b392540a962f1328c0033c4a2325'
app.config['MAIL_PASSWORD'] = '91b5245358083039ce4a3c88d7fa9d94'
app.config['MAIL_DEFAULT_SENDER'] = 'promise.john37170@gmail.com'


mail = Mail(app)
s = URLSafeTimedSerializer(app.secret_key)


def send_confirmation_email(email):
    try:

        html = render_template('activate.html')
        subject = "Bienvenue sur TodoApp"

        msg = Message(subject, sender='promise.john37170@gmail.com', recipients=[email], html=html)
        mail.send(msg)
        print(f"Confirmation email sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")






class User:
    def __init__(self, email, name, surname, id, profile_picture, connected):
        self.email = email
        self.name = name
        self.surname = surname
        self.id = id
        self.profile_picture = profile_picture
        self.connected = connected
        

p1 = User("", "", "", "", "", False)
      

# RECCUPERER LES DONNEES DE L'UTILISATEUR ACTUELEMENT CONNECTE (SESSION.STORAGE DANS LE FRONTEND)

@app.route('/api/session/', methods=['GET'])
def session_status():
    # global p1
    # CurrentUser = request.json
    # p1 = User(CurrentUser['email'], CurrentUser['name'], CurrentUser['surname'], CurrentUser['id'], CurrentUser['profile_picture'], True)
    # print(p1.email, p1.name, p1.surname, p1.id, p1.profile_picture, p1.connected)
    
    if p1.connected == True:
        return jsonify({"status": "success", "message": "User is connected"}), 201
    else:
        return jsonify({"status": "error", "message": "User is not connected"}), 401

# AJOUTER UNE TACHE

@app.route('/api/todos/', methods=['POST'])
def add_todo():
    global p1
    if p1.connected == True:

        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        
        NewTodo = request.json  # Capture les données JSON envoyées par Axios
        global AddTodo
        
        AddTodo = {
            "title" : NewTodo['titre'],
            "description" : NewTodo['desc'],
            "importance" : NewTodo['importance'],
            "categorie" : NewTodo['categorie'],
            "created_at" : datetime.now(),
            'id': p1.id,
            "time": NewTodo['time'],
            "date": NewTodo['date']
        }
        if AddTodo['time'] == '':
            AddTodo['time'] = None
        if NewTodo['date'] == '':
            AddTodo['date'] = None
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO tasks (title, description, importance, category,  done, expired, creation_date, member_id, due_time, due_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (AddTodo['title'], AddTodo['description'], AddTodo['importance'], AddTodo['categorie'], 0, 0, AddTodo['created_at'], AddTodo['id'], AddTodo['time'], AddTodo['date'])
        mycursor.execute(sql, val)
        
        
        print(AddTodo)   
        
        mydb.commit()

        print(mycursor.rowcount, "données insérées.")

        mycursor.close()
        
        send_json()

        return jsonify({"status": "success", "message": "Todo Added Successfully"}), 201



# RENVOYER LES TACHES AU FRONTEND

@app.route('/api/send_todo_back', methods=['GET'])
def send_json():
    global p1
    if p1.connected == True:
    
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM tasks WHERE member_id = %s", (p1.id,))
 
        myresult = mycursor.fetchall()
        data = []
        for x in myresult:
            time = x[10]
            if time == None:
                converted_time = None
            else:
                converted_time = str(time)

            new_table = {'id':x[0], 'title':x[1], 'description':x[2], 'importance':x[3], 'category':x[4], 'due_date':x[5], 'creation_date':x[6], 'done':x[7], 'expired':x[8], 'due_time':converted_time}
            data.append(new_table)
            # print(new_table)


        print(data)
        # Convertit le dictionnaire en JSON et le renvoie comme réponse
        data.reverse()
        mycursor.close()
        return jsonify(data)
    


    
# CREER UN COMPTE

@app.route('/api/create_account', methods=['POST'])
def create_account():
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    if not mydb:
        return jsonify({"error": "Could not connect to database"}), 500

    NewUser = request.json
    AddUser = {
        "name": NewUser['name'],
        "surname": NewUser['surname'],
        "email": NewUser['email'],
        "password": bcrypt.hashpw(NewUser['password'].encode('utf-8'), bcrypt.gensalt()),
        "creation_date": 
        
        datetime.now(),
    }

    mycursor = mydb.cursor()
    try:
        sql = "INSERT INTO members (name, surname, email, password, creation_date) VALUES (%s, %s, %s, %s, %s)"
        val = (AddUser['name'], AddUser['surname'], AddUser['email'], AddUser['password'], AddUser['creation_date'])
        mycursor.execute(sql, val)
        mydb.commit()

 # envoyer un email de confirmation
        

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        mycursor.close()
        mydb.close()

    send_confirmation_email(AddUser['email'])
    return jsonify({"status": "success", "message": "Account Created Successfully"}), 201


#SE CONNECTER

@app.route('/api/login', methods=['POST'])
def login():
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    if not mydb:
        return jsonify({"error": "Could not connect to database"}), 500
    
    loginData = request.json
    email = loginData.get('email')
    password = loginData.get('password')
    
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM members WHERE email = %s", (email,))
    userresult = mycursor.fetchone()
    
    if not userresult or not bcrypt.checkpw(password.encode('utf-8'), userresult['password'].encode('utf-8')):
        return jsonify({"status": "error", "message": "Invalid Email or Password"}), 401
    
    profile_picture_base64 = None
    if userresult['profile_picture']:
        profile_picture_base64 = base64.b64encode(userresult['profile_picture']).decode('utf-8')
    
    user_data_vue = [{
        'id': userresult['id'],
        'name': userresult['name'],
        'surname': userresult['surname'],
        'email': userresult['email'],
        'profile_picture': profile_picture_base64,
       
    }]

    user_data = user_data_vue[0]
    

    session.permanent = True
    
    session['user'] = user_data['id']
    session['connected'] = True
    session['email'] = user_data['email']
    session['name'] =  user_data['name']
    session['surname'] = user_data['surname']
    session['profile_picture'] = user_data['profile_picture']
    global p1
    p1 = User(session['email'], session['name'], session['surname'], session['user'], session['profile_picture'], session['connected'])
    print(p1.email, p1.name, p1.surname, p1.id, p1.profile_picture, p1.connected)


    

    mycursor.close()
    mydb.close()
    return jsonify(user_data_vue)



# SUPPRIMER UNE TACHE


@app.route('/api/delete_todo', methods=['POST'])
def delete_todo():
        
    global p1
    if p1.connected == True:
    
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        
        DeleteTodo = request.json
        infos = {
            "id": DeleteTodo['id']
        }
        print(infos)
        print(infos['id'])
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM tasks WHERE id = %s", (infos['id'],))
        mydb.commit()
        mycursor.close()
        return jsonify({"status": "success", "message": "Todo Deleted Successfully"}), 201



# MARQUER UNE TACHE COMME FAITE OU NON FAITE ET METTRE A JOUR LA BASE DE DONNEES

@app.route('/api/isdone', methods=['PUT'])
def isdone():
    global p1
    if p1.connected == True:
    
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        
        DoneTodo = request.json
        infos = {
            "id": DoneTodo['id'],
            "done": DoneTodo['done']
        }
    
        print(infos)
        print(infos['id'])
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE tasks SET done = %s WHERE id = %s", (infos['done'], infos['id']))
        mydb.commit()
        mycursor.close()
        return jsonify({"status": "success", "message": "Todo Done Successfully"}), 201
    

# MODIFIER UNE TACHE

@app.route('/api/editTodo', methods=['PUT'])
def editTodo():
    def convert_due_date(date_str):
        """
        Convert a date string to a datetime object.
        """
        if date_str is None:
            return None
        try:
            return parser.parse(date_str)
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None

    def format_due_date_for_db(date_obj):
        """
        Format a datetime object to the desired string format for the database.
        """
        if date_obj:
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")  # Example format
        return None
    

    global p1
    if p1.connected == True:
    
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        
        EditTodo = request.json
        infos = {
            "id": EditTodo['id'],
            "title": EditTodo['titre'],
            "description": EditTodo['desc'],
            "importance": EditTodo['importance'],
            "category": EditTodo['categorie'],
            "due_date": EditTodo['date'],
            "due_time": EditTodo['time']
        }
        if infos['due_time'] == '':
            infos['due_time'] = None
        if infos['due_date'] == '':
            infos['due_date'] = None
        else:
           
            due_date_obj = convert_due_date(infos['due_date'])

            # Formatter la date pour la base de données
            infos['due_date'] = format_due_date_for_db(due_date_obj)
        
    
        print(infos)
        print(infos['id'])
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE tasks SET title = %s, description = %s, importance = %s, category = %s, due_date = %s, due_time = %s WHERE id = %s", (infos['title'], infos['description'], infos['importance'], infos['category'], infos['due_date'], infos['due_time'], infos['id']))
        mydb.commit()
        mycursor.close()
        return jsonify({"status": "success", "message": "Todo Edited Successfully"}), 201
    

# ENVOYER LES DONNEES AU DASHBOARD (NOMBRE DE TACHES, TACHES FAITES, TACHES NON FAITES)

@app.route('/api/dash-data', methods=['GET'])
def dash_data():
    global p1
    if p1.connected == True:
    
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM tasks WHERE member_id = %s", (p1.id,))
        myresult = mycursor.fetchall()
        totalTasks = myresult
        totalDoneTasks = []
        totalNotDoneTasks = []
        for x in myresult:
            if x[7] == 1:
                totalDoneTasks.append(x)
            if x[7] == 0:
                totalNotDoneTasks.append(x)
        data = {
            'totalTasks' : len(totalTasks),
            'totalDoneTasks' : len(totalDoneTasks),
            'totalNotDoneTasks' : len(totalNotDoneTasks)
            }
        
        mycursor.close()
        
        return jsonify(data)
    

@app.route('/api/update-user', methods=['PUT'])
def update_user():
    global p1
    if p1.connected:
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        profile_picture = request.files.get('profile_picture')

        if profile_picture:
            profile_picture_data = profile_picture.read()
        else:
            profile_picture_data = None

        mycursor = mydb.cursor()
        if profile_picture_data:
            mycursor.execute(
                "UPDATE members SET name = %s, surname = %s, email = %s, profile_picture = %s WHERE id = %s",
                (name, surname, email, profile_picture_data, p1.id)
            )
        else:
            mycursor.execute(
                "UPDATE members SET name = %s, surname = %s, email = %s WHERE id = %s",
                (name, surname, email, p1.id)
            )
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        return jsonify({"status": "success", "message": "User Edited Successfully"}), 201
    else:
        return jsonify({"status": "error", "message": "Not connected"}), 403
    



# @app.route('/api/update-password', methods=['POST'])
# def update_password():
#     global p1
#     if p1.connected:
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="promise",
#             password="Promise2003@",
#             database="todo_app"
#         )

#         old_password = request.form.get('old_password')
#         new_password = request.form.get('new_password')

#         mycursor = mydb.cursor(dictionary=True)
#         mycursor.execute("SELECT * FROM members WHERE id = %s", (p1.id,))
#         userresult = mycursor.fetchone()

#         if not bcrypt.checkpw(old_password.encode('utf-8'), userresult['password'].encode('utf-8')):
#             return jsonify({"status": "error", "message": "Invalid Password"}), 401

#         hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
#         mycursor.execute("UPDATE members SET password = %s WHERE id = %s", (hashed_new_password, p1.id))
#         mydb.commit()
#         mycursor.close()
#         mydb.close()
#         return jsonify({"status": "success", "message": "Password Changed Successfully"}), 201
#     else:
#         return jsonify({"status": "error", "message": "Not connected"}), 403


@app.route('/api/logout', methods=['POST'])
def logout():
    global p1
    p1 = User("", "", "", "", "", False)
    session.clear()
    return jsonify({"status": "success", "message": "User logged out"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)




