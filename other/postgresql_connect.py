import psycopg2

# Параметры подключения
conn = psycopg2.connect(
    dbname="specpro",
    user="tpyiioed",
    password="Ng554wr9",
    host="localhost",
    port="5432"
)

# Создание курсора для выполнения операций с базой данных
cur = conn.cursor()

# Закидываем данные в бд
def data_add(id,product,quntity,weight):
    cur.execute('''
        INSERT INTO orders.test (id,product,quntity,weight)
        VALUES (?,?,?,?)
        ''',(id,product,quntity,weight))
    conn.commit()

data_add(2, 'Бекон', 2, 1)
# Выполнение запроса
cur.execute("SELECT * from orders.test;")
db_version = cur.fetchone()
print(db_version)



# Закрываем курсор и соединение
cur.close()
conn.close()







