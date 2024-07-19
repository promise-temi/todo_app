import mysql.connector


def create_account(NewUser):
    mydb = mysql.connector.connect(
        host="localhost",
        user="promise",
        password="Promise2003@",
        database="todo_app"  
    )

    global AddUser
    AddUser = {
        "name" : NewUser['name'],
        "surname" : NewUser['surname'],
        "email" : NewUser['email'],
        "password" : NewUser['password'],
    }

    mycursor = mydb.cursor()

    sql = "INSERT INTO members (name, surname, email, password) VALUES (%s, %s, %s, %s)"
    val = (AddUser['name'], AddUser['surname'], AddUser['email'], AddUser['password'])
    mycursor.execute(sql, val)

    
    print(AddUser)   
    
    mydb.commit()

    print(mycursor.rowcount, "données insérées.")

    mycursor.close()