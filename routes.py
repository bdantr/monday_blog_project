from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, login
from forms import LoginForm
from models import User


@login.user_loader
def load_user(id):
    return User.query.get(int(id))  # достает пользователя из базы данных и запоминает его


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = LoginForm()
    if form.validate_on_submit():  # если форма отправляется
        user = User.query.filter_by(username=form.username.data)  # пытаюсь найти пользователя в БД по логину
        if user is None or not user.check_password(form.password.data):
            # если пользователь не найден в БД или пароль не совпал
            return redirect(url_for('login'))  # вернуть пользователя на страницу входа
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login page', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page'))


@app.route('/support')
@login_required
def support():
    return render_template('support.html')
