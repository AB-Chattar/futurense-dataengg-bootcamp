import mysql.connector #Importing Connector package   
mysqldb=mysql.connector.connect(host="localhost",user="root",password="root")#established connection   
mycursor=mysqldb.cursor()#cursor() method create a cursor object  
mycursor.execute("create database if not exists dbpython_app")#Execute SQL Query to create a database  
mysqldb.close()#Connection Close  

mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="dbpython_app")#established connection between your database   
mycursor=mysqldb.cursor()#cursor() method create a cursor object  
create_table_query=  """create table if not exists person_tab(
    person_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255), 
    phone_number numeric(10,0),
    gender varchar(20), 
    address VARCHAR(100))"""
mycursor.execute(create_table_query)
create_table_query1=  """create table if not exists patient_tab(
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    tratment_id INT ,
    person_id INT,
    dob date)"""
mycursor.execute(create_table_query1)
mysqldb.close()

class Get_data:
    def __init__(self, name,person_id):
        self.name = name
        self.person_id=person_id

    def get_person_details(self):
        cur = None
        mysqldb = None
        try:
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="dbpython_app")
            cur = mysqldb.cursor()
            select_query = """SELECT * FROM person_tab WHERE name = %s AND person_id = %s"""
            user_input = self.name,self.person_id
            cur.execute(select_query, user_input)
            r_rows = cur.fetchall()
            if len(r_rows) < 1:
                print("No person found")
                return False
            else:
                for record in r_rows:
                    print(record)
                return True
        except Exception as e:
            print(e)
        finally:
            if cur is not None:
                cur.close()
            if mysqldb is not None:
                mysqldb.close()

    def get_patient_details(self):
        cur = None
        mysqldb = None
        try:
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="dbpython_app")
            cur = mysqldb.cursor()
            select_query = """SELECT * FROM person_tab p1 INNER JOIN patient_tab p2 ON p1.person_id=p2.person_id WHERE name = %s AND patient_id = %s"""
            user_input = (self.name,self.person_id)
            cur.execute(select_query, user_input)
            r_rows = cur.fetchall()
            if len(r_rows) < 1:
                print("No patient found")
                return print("*************")
            else:
                for record in r_rows:
                    print(record)
                return print("*************")
        except Exception as e:
            print(e)
        finally:
            if cur is not None:
                cur.close()
            if mysqldb is not None:
                mysqldb.close()

    
    def get_All_details(self):
        cur = None
        mysqldb = None
        try:
            mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="dbpython_app")
            cur = mysqldb.cursor()
            select_query = """SELECT * FROM person_tab """
            cur.execute(select_query)
            r_rows = cur.fetchall()
            if len(r_rows) < 1:
                print("No patient found")
                return print("*************")
            else:
                for record in r_rows:
                    print(record)
                return print("*************")
        except Exception as e:
            print(e)
        finally:
            if cur is not None:
                cur.close()
            if mysqldb is not None:
                mysqldb.close()


class Add_details:
    def add_person(self):
        while True:
            try:
                name,phone_number,gender, address = input('Enter Name   '),int(input('Enter Phone Number  ')),input("Enter Gender  "),input('Enter Address  ')

                mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="dbpython_app")
                cur = mysqldb.cursor()
                select_query = """INSERT INTO person_tab(name,phone_number,gender,address) VALUES(%s,%s,%s,%s)"""
                user_input = (name,phone_number,gender,address)
                cur.execute(select_query, user_input)
                mysqldb.commit()
                print('Data inserted successfully')
                return print('Data inserted successfully')
            except Exception as e:
                print('Try again')
    def add_patient(self):
        while True:
            try:
                name,tratment_id, person_id,dob = input("Enter Name  "),int(input('Enter Tratment ID    ')),int(input('Enter Person ID   ')),input("Enter DOB YYY-MM-DD  ")
                get_data1 = Get_data(name, person_id)
                if not (get_data1.get_person_details()):
                    print("Person details not found\nPlease Add Person Details")
                    self.add_person()
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="dbpython_app")
                cur = mysqldb.cursor()
                select_query = """INSERT INTO patient_tab(tratment_id,person_id,dob) VALUES(%s,%s,%s)"""
                user_input = (tratment_id,person_id,dob)
                cur.execute(select_query, user_input)
                mysqldb.commit()
                print('Data inserted successfully')
                return name
            except Exception as e:
                print('Try again',e)




while True:
    try:
        print("1. Check Person\n2. Check Patient\n3. Show All\n4. Add Person\n5. Add Patient\n\n7. For Exit enter 'exit'")
        user_option = input()
        if user_option == '1':
            p_name,person_id = input('Enter Person Name '),int(input('Enter Person ID '))
            p1 = Get_data(p_name,person_id)
            p1.get_person_details()
            continue
        elif user_option == '2':
            p_name,patient_id = input('Enter Patient Name '),int(input('Enter Patient ID '))
            p1 = Get_data(p_name,patient_id)
            p1.get_patient_details()
            continue
        elif user_option == '3':
            p1 = Get_data(None,None)
            p1.get_All_details()
        add_details = Add_details()
        if user_option == '4':
            add_details.add_person()
        elif user_option == '5':
            add_details.add_patient()
        elif user_option == '7' or user_option == 'exit':
            break
        else:
            print('Choose correct options')
    except Exception as e:
        print('Choose correct options',e)