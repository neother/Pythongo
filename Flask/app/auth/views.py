from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import auth
from . import main
from ..models import User
from .forms import LoginForm, RegistrationForm
from app import db

from flask_login import logout_user, login_required, current_user
from ..email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
       #     return redirect(request.args.get('next') or url_for('auth.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        flash('mulitple time clicking the confirm link')
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your accout. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    flash('WELCOME TO CHEETAHNET')
    return render_template('index.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))


'''
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
'''
