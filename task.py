"""
Задание №9
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/dress/')
def dress():
    context = {'title': 'Одежда'}
    return render_template('dress.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь!'}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртка!'}
    return render_template('jacket.html', **context)


@app.route('/')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
