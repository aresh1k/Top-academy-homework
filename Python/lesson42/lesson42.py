from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(__name__)

menu = [
    {"name": "Каталог курсов", "url": "/"},
    {"name": "Добавить курс", "url": "add_course"},
    {"name": "Информация", "url": "info"}
]


@app.route("/")
def main():
    return render_template('catalog.html', title='Каталог', menu=menu)


@app.route("/add_course")
def about():
    return render_template('add_course.html', title='Добавить', menu=menu)


@app.route("/info")
def contacts():
    return render_template('info.html', title='Информация', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
