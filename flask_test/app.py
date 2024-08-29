from flask import Flask, render_template, redirect, url_for, request,session
import sqlite3  
import hashlib  
# Flask - библиотека для запуска приложения Flask - app
# render_template - нужен для то чтобы страница html отобразилась корреткно
# redirect - понадобится для обработки запроса формы где мы перенаприм пользователя на страницу админ панели
# url_for - вспомогательна библиотека для того чтобы сделать правильный переход по ссылке в нашем случеш мы будем ссылаться на adm_panel
# request - обработчик запросов GET/POST и дргуих 
# подключаем Sqlite в наш проект
# библиотека для хеширования

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # подствавьте свой секретный ключ
# секретный ключ для хеширования данных сессии при авторизации

# Устанавливаем соединение с Базой Данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#  наша корневая страиница лендинда 
@app.route('/')
def home():
    # Загрузка и отображение главной страницы (landing page)
    return render_template('landing.html') 

# страница формы логина в админ панель  
@app.route('/adm_login', methods=['GET', 'POST'])
def admin_login():
    error = None # обнуляем переменную ошибок 
    if request.method == 'POST':
        username = request.form['username'] # обрабатываем запрос с нашей формы который имеет атрибут name="username"
        password = request.form['password'] # обрабатываем запрос с нашей формы который имеет атрибут name="password"
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest() # шифруем пароль в sha-256

        # устанавливаем соединение с БД
        conn = get_db_connection() 
        # создаем запрос для поиска пользователя по username,
        # если такой пользователь существует, то получаем все данные id, password
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        # закрываем подключение БД
        conn.close() 
        
        # теперь проверяем если данные сходятся формы с данными БД
        if user and user['password'] == hashed_password:
            # в случае успеха создаем сессию в которую записываем id пользователя
            session['user_id'] = user['id']
            # и делаем переадресацию пользователя на новую страницу -> в нашу адимнку
            return redirect(url_for('admin_panel'))

        else:
            error = 'Неправильное имя пользователя или пароль'

    return render_template('login_adm.html', error=error)

# страница админ панели
@app.route('/admin_panel')
def admin_panel():
    # Загрузка и отображение админ-панели
    # делаем доп проверку если сессия авторизации была создана 
    if 'user_id' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin_panel.html')

if __name__ == '__main__':
    app.run(debug=True)