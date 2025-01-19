from flask import Flask, render_template, request, session
from database import Database



# инициализация приложения
app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'


# запуск базы данных
db = Database()


# элементы навигации
navigation = [
    {'name': 'Информация', 'url': '/info'},
    {'name': 'Регистрация', 'url': '/registration'},
    {'name': 'Авторизация', 'url': '/login'},
]
auth_nav = [
    {'name': 'Информация', 'url': '/info'},
    {'name': 'Добавить новость', 'url': '/add_news'},
    {'name': 'Смотреть новости', 'url': '/news'},
]


@app.route('/')
@app.route('/index')
def index():
    if session.get('username', 0) != 'logout' or session.get('username', 0) == 0:
        return render_template(template_name_or_list='base.html', title='Главная',
                               navigation=auth_nav,  logout=True)
    return render_template(template_name_or_list='base.html', title='Главная', navigation=navigation)

@app.route('/info')
def info():
    if session.get('username', 0) != 'logout' or session.get('username', 0) == 0:
        return render_template(template_name_or_list='info.html', title='Информация',
                               navigation=auth_nav,  logout=True)
    return render_template(template_name_or_list='info.html', title='Информация', navigation=navigation)

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        is_add = db.create_user(username=username, password=password, email=email)
        # print(is_add)
        if is_add:
            return render_template('base.html', title='Главная', navigation=navigation)
        else:
            return {'status': 'registered'}

    if session.get('username') == request.form.get('username'):
        return render_template( template_name_or_list='registration.html', title='Регистрация', navigation=auth_nav)

    return render_template( template_name_or_list='registration.html', title='Регистрация', navigation=navigation)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('username', 0) != 'logout' or session.get('username', 0) == 0:
        print(session.get('username', 0))
        return render_template( template_name_or_list='base.html', title='Главная',
                                navigation=auth_nav, logout=True)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        exists = db.get_user(username, password)
        print(exists)
        if exists:
            session['username'] = username
            return {'status': 'autorized'}
        else:
            return {'status': 'not autorized'}

    return render_template( template_name_or_list='login.html', title='Авторизация', navigation=navigation)


@app.route('/log_out')
def log_out():
    session['username'] = 'logout'
    return render_template(template_name_or_list='base.html', title='Главная', navigation=navigation)


@app.route('/add_news', methods=['POST', 'GET'])
def add_news():
    if request.method == "POST":
        username = session['username']
        title = request.form['title']
        content = request.form['content']
        db.create_post(username, title, content)
        return {'status': 'post created'}

    return render_template(template_name_or_list='add_news_form.html', title='Добавить новость',
                           navigation=auth_nav, logout=True)


@app.get('/news')
def news():
    if session.get('username', 0) != 'logout' or session.get('username', 0) == 0:
        data = db.get_posts(session.get('username', 0))
        return render_template(template_name_or_list='news.html', title='Новости',
                               navigation=auth_nav, logout=True, news=data)

    return render_template(template_name_or_list='base.html', title='Вы не авторизованы', navigation=navigation)


if __name__ == '__main__':
    app.run()

