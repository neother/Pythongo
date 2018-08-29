from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import main
from ..models import User
from .forms import LoginForm, RegistrationForm
from app import db

from flask_login import logout_user, login_required, current_user
from ..email import send_email


@main.route('/')
def index():
    flash('WELCOME TO CHEETAHNET')
    return render_template('main/index.html')


''''
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
'''
