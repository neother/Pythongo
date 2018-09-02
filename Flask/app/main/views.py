from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import main
from ..models import User
#from .forms import LoginForm, RegistrationForm
from app import db

from flask_login import logout_user, login_required, current_user
from ..email import send_email


@main.route('/')
def index():
    flash('WELCOME TO CHEETAHNET')
    return render_template('main/index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    '''
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    '''
    # return render_template('user.html', user=user, posts=posts,pagination=pagination)
    return render_template('main/user.html', user=user)
