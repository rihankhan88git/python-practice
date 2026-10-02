import mysql.connector



# MySQL connection
def get_connection():
    print("Trying to connect with MySQL...")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        password="Admin@123",
        database="rest_api",
        use_pure=True
    )

    print("MySQL connected successfully")
    return connection


# Create table
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS users (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(255) NOT NULL,
            ADDRESS VARCHAR(255) NOT NULL,
            COURSE VARCHAR(255) NOT NULL,
            FEE DECIMAL(10,2) NOT NULL,
            EMAIL VARCHAR(255) NOT NULL
        )
    """

    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()

    print("Table created successfully")


# Create user
def create_user(user):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO users
        (NAME, ADDRESS, COURSE, FEE, EMAIL)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            user.name,
            user.address,
            user.course,
            user.fee,
            user.email
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "success": True,
        "message": "User created successfully",
        "data": user
    }


# Get all users
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users"

    cursor.execute(query)
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "success": True,
        "message": "Users fetched successfully",
        "data": users
    }


# Get user by ID
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE ID = %s"

    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return {
            "success": True,
            "message": "User found successfully",
            "data": user
        }

    return {
        "success": False,
        "message": "User not found",
        "data": None
    }


# Update user
def update_user(user_id, user):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE users
        SET NAME = %s,
            ADDRESS = %s,
            COURSE = %s,
            FEE = %s,
            EMAIL = %s
        WHERE ID = %s
    """

    cursor.execute(
        query,
        (
            user.name,
            user.address,
            user.course,
            user.fee,
            user.email,
            user_id
        )
    )

    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()

        return {
            "success": False,
            "message": "User not found",
            "data": None
        }

    cursor.close()
    conn.close()

    return {
        "success": True,
        "message": "User updated successfully",
        "data": user
    }


# Delete user
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM users WHERE ID = %s"

    cursor.execute(query, (user_id,))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()

        return {
            "success": False,
            "message": "User not found",
            "data": None
        }

    cursor.close()
    conn.close()

    return {
        "success": True,
        "message": "User deleted successfully",
        "data": None
    }