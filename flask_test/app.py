from flask import Flask, render_template, redirect, url_for, request
# Flask - библиотека для запуска приложения Flask - app
# render_template - нужен для то чтобы страница html отобразилась корреткно
# redirect - понадобится для обработки запроса формы где мы перенаприм пользователя на страницу админ панели
# url_for - вспомогательна библиотека для того чтобы сделать правильный переход по ссылке в нашем случеш мы будем ссылаться на adm_panel
# request - обработчик запросов GET/POST и дргуих 

app = Flask(__name__)

#  наша корневая страиницу лендинда 
@app.route('/')
def home():
    # Загрузка и отображение главной страницы (landing page)
    return render_template('landing.html') 

# страница формы логина в админ панель  
@app.route('/adm_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # Здесь должна быть логика аутентификации
        # Если аутентификация прошла успешно, перенаправляем на /admin_panel
        return redirect(url_for('admin_panel'))
    # Если GET запрос, показываем форму входа
    return render_template('login_adm.html')

# страница админ панели
@app.route('/admin_panel')
def admin_panel():
    # Загрузка и отображение админ-панели
    return render_template('admin_panel.html')

if __name__ == '__main__':
    app.run(debug=True)