from flask import Flask
from flask import render_template
name = ''
app = Flask(name)

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

if name == 'main':
  app.run(debug=True) # debug true задаем специально для разработки (в данном случае при обновление/изменение кода приложение автоматически само обновит данные на сайте)