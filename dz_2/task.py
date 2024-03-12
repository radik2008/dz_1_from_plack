"""
Задание №9
Создать страницу, на которой будет форма для ввода имени и электронной почты При отправке которой будет создан
cookie файл с данными пользователя Также будет произведено перенаправление на страницу приветствия,
где будет отображаться имя пользователя. На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""


from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    return render_template('user_form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Создание cookie файла с данными пользователя
    response = make_response(redirect(url_for('greet')))
    response.set_cookie('user_data', f'{name}:{email}')

    return response


@app.route('/greet')
def greet():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, email = user_data.split(':')
        return render_template('welcome.html', name=name)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # Удаление cookie файла при нажатии на кнопку "Выйти"
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', '', expires=0)

    return response


if __name__ == '__main__':
    app.run(debug=True)
