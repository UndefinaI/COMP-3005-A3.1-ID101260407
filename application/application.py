import psycopg

#code flow: connect to postgre, then define functions, then use mainloop, then disconnect



USERNAME = "postgres"
PASSWORD = "17GIGSofcat"
PORT = "5432"










try:
    conn = psycopg.connect(
        f"dbname=A3_students user={USERNAME}"
        f" password={PASSWORD} host=localhost port={PORT}"
    )

except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)


cursor = conn.cursor()







def getAllStudents():
    try: 
        cursor.execute("SELECT * FROM students;")
        rows = cursor.fetchall()
        print("STUDENTS: ")
        for row in rows:
            print(row)
            
    except psycopg.DatabaseError as e:

        conn.rollback()
        print("ERROR IN SQL: ", e)
        



def addStudent(first_name, last_name, email, enrollment_date):
    try: 
        cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');")
        print("INSERTION SUCCESSFUL")
        conn.commit()
            
    except psycopg.DatabaseError as e:

        conn.rollback()
        print("ERROR IN SQL: ", e)    



def updateStudentEmail(student_id, new_email):
    try: 
        cursor.execute(f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};")
        print("UPDATE SUCCESSFUL")
        conn.commit()
            
    except psycopg.DatabaseError as e:

        conn.rollback()
        print("ERROR IN SQL: ", e)    



def deleteStudent(student_id):
    try: 
        cursor.execute(f"DELETE FROM students WHERE student_id = {student_id};")
        print("DELETE SUCCESSFUL")
        conn.commit()
            
    except psycopg.DatabaseError as e:

        conn.rollback()
        print("ERROR IN SQL: ", e) 









#MAINLOOP
choice = -1

while (choice != "0"):
    print("1: show students \n2: add student\n3: update email\n4: delete student\n0: quit\n")
    choice = input("Enter choice: ")
    print("")

    if(choice=="1"):
        getAllStudents()
    elif(choice=="2"):
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        email = input("Enter email: ")
        date = input("Enter enrollment date: ")
        addStudent(fname,lname,email,date)
    elif(choice=="3"):
        sid = input("Enter id: ")
        email = input("Enter email: ")
        updateStudentEmail(sid,email)
    elif(choice=="4"):
        sid = input("Enter id: ")
        deleteStudent(sid)

    print("")


#addStudent("Reggie", "Hyuga", "Reggie@email.com", "2022-09-01")
#updateStudentEmail(5,"new@email.com")
#deleteStudent(5)
#getAllStudents()


        







cursor.close()
conn.close()
