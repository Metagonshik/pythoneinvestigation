from mysql.connector import connect, Error 

def dbExec(sql_database, sql_query):

    db1 = connect(host="localhost", user="root", password="root")

    db_cursor = db1.cursor()
    db_cursor.execute(f'''use {sql_database}''')
    try:
        db_cursor.execute(sql_query)
    except Error as e:
        print(e)
    data = db_cursor.fetchall()
    db1.commit()
    db1.disconnect()
    return data