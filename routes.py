from flask import render_template, flash, redirect, url_for
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
    form = LoginForm()
    if form.validate_on_submit():  # если форма отправляется
        flash(f'Login requested for user {form.username.data}')
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login page', form=form)



