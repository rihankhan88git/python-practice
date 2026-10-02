# import mysql.connector
# from mysql.connector.aio import cursor
#
#
# def get_connection():
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Admin@123",
#             database="developers",
#             port="3306",
#             use_pure=True
#         )
#         return connection
#
#     except mysql.connector.Error as error:
#         print("Failed to create database:", error)
#         return None
#
#
# def create_table():
#     try:
#         connection = get_connection()
#
#         if connection is None:
#             return
#
#         cursor = None
#
#         try:
#             cursor = connection.cursor()
#
#             sql = """CREATE TABLE IF NOT EXISTS development (
#                 employee_id INT PRIMARY KEY AUTO_INCREMENT,
#                 employee_name VARCHAR(255),
#                 employee_email VARCHAR(255),
#                 employee_address VARCHAR(255),
#                 employee_phone VARCHAR(15)
#             )"""
#
#             cursor.execute(sql)
#             connection.commit()
#
#             print("Table created successfully")
#
#         finally:
#             if cursor:
#                 cursor.close()
#             connection.close()
#
#     except mysql.connector.Error as error:
#         print("Failed to create table:", error)
#
#
# create_table()
#
# # inpt data in development table
#
# def add_employee():
#     connection = get_connection()
#     cursor=connection.cursor()
#
#     employee_name=(input("Enter employee name: "))
#     employee_email=(input("Enter employee email: "))
#     employee_address=(input("Enter employee address: "))
#     employee_phone=(input("Enter employee phone: "))
#     sql="""
#         insert into development(employee_name,employee_email,employee_address,employee_phone) values(%s,%s,%s,%s)
#         """
#     values=(employee_name,employee_email,employee_address,employee_phone)
#     cursor.execute(sql, values)
#     connection.commit()
#
#     print("developers data inserted successfully")
#     connection.close()
#
# # **------FETCH ALL EMPLOYEES--------****
#
# def fetch_all_employee():
#     connection = get_connection()
#     cursor = connection.cursor()
#     sql= "select * from development"
#     cursor.execute(sql)
#     students=cursor.fetchall()
#     for student in students:
#         print(student)
#
# fetch_all_employee()
#
# # ***-------FETCH SINGLE EMPLOYEE-------****
#
# def fetch_single_employee():
#     connection = get_connection()
#     cursor = connection.cursor()
#
#     try:
#         employee_id = int(input("Enter employee id: "))
#
#         sql = "SELECT * FROM development WHERE employee_id = %s"
#
#         cursor.execute(sql, (employee_id,))
#
#         single_student = cursor.fetchone()
#
#         if single_student:
#             print("Employee ID:", single_student[0])
#             print("Employee Name:", single_student[1])
#             print("Employee Email:", single_student[2])
#             print("Employee Address:", single_student[3])
#             print("Employee Phone:", single_student[4])
#         else:
#             print("Employee not found")
#
#     finally:
#         cursor.close()
#         connection.close()
#
#
# fetch_single_employee()
#
#
# # **-------UPDATE EMPLOYEE--------***
#
# def update_employee():
#     connection= get_connection()
#     cursor = connection.cursor()
#     employee_name = (input("Enter employee name: "))
#     employee_email = (input("Enter employee email: "))
#     employee_address = (input("Enter employee address: "))
#     employee_phone = (input("Enter employee phone: "))
#     sql = """
#             insert into development(employee_name,employee_email,employee_address,employee_phone) values(%s,%s,%s,%s)
#             """
#
#     values=(employee_name,employee_email,employee_address,employee_phone)
#     cursor.execute(sql, values)
#     connection.commit()
#
#     print("developers data updated successfully")
#     connection.close()
#
# # update_employee()
#
