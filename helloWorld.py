import psycopg2
from config import postgreconf
try:
    conn = psycopg2.connect(
    database=postgreconf.db_name, 
    user=postgreconf.user,
    password=postgreconf.password, 
    host=postgreconf.host)
    cur = conn.cursor()
    cur.execute("select * from sp;")
    data=cur.fetchall()
    conn.commit()
    print(data)
    cur.close()
    conn.close()
except:
    cur.close()
    conn.close()
    print('Error')