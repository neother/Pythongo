from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import auth

from ..models import User, Post, Comment
from .forms import *
from app import db

from flask_login import logout_user, login_required, current_user
from ..email import send_email
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
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
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


########################## common def will run before every request##########################
@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))
########################## common def will run before every request##########################


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        flash('You have confirmed your account for more than 2 times')
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your accout. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:

        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():

    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


#######################################password change###############################################################


@auth.route('/password_change', methods=['GET', 'POST'])
@login_required
def password_change():
    form = ChangepasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.new_password.data
            db.session.add(current_user)
            db.session.commit()
            flash('Password has been changed successfully')
            return redirect(url_for('auth.login'))
        else:
            flash('Old Password is not correct')

    return render_template('auth/password_change.html', form=form)

#######################################password change###############################################################
#######################################password reset###############################################################


@auth.route('/password_reset_request', methods=['GET', 'POST'])
def password_reset_request():
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None:
            flash('Invalid email address, check again')
        else:
            token = user.generate_resetpassword_token()
            send_email(form.email.data, 'Reset Your Password',
                       'auth/email/resetpassword', user=user, token=token)
            flash('A password reset email has been sent to your registered email')
            return redirect(url_for('main.index'))

    return render_template('auth/password_reset.html', form=form)


@auth.route('/password_reset/<token>', methods=['GET', 'POST'])
def password_reset(token):

    form = PasswordResetForm()

    if form.validate_on_submit():

        if User.reset_password(token, form.new_password.data):
            flash('Password has been reset, Please loggin again')
            return redirect(url_for('auth.login'))
        else:
            flash('Token does not match')
            return redirect(url_for('auth.login'))

    return render_template('auth/password_reset.html', form=form)


#######################################password reset###############################################################


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))


@auth.route('/deleteself')
def deleteself():

    db.session.delete(current_user)
    db.session.commit()
    flash('current user has been deleted')
    return redirect(url_for('auth.login'))


@auth.route('/removeallpost')
def removeallpost():

    allthepost = Post.query.all()
    for post in allthepost:
        db.session.delete(post)

    db.session.commit()
    flash('all the posthas been deleted')
    return redirect(url_for('main.index'))


@auth.route('/removealluser')
def removealluser():

    alltheuser = User.query.all()
    for user in alltheuser:
        if user.email != '401316161@qq.com':
            db.session.delete(user)
    db.session.commit()
    flash('all the uses have been deleted')
    return redirect(url_for('main.index'))


@auth.route('/removeallcomment')
def removeallcomment():

    removeallcomment = Comment.query.all()
    for comment in removeallcomment:
        db.session.delete(comment)

    db.session.commit()
    flash('all the comment has been deleted')
    return redirect(url_for('main.index'))


@auth.route('/followadmin')
def followadmin():
    adminuser = User.query.filter_by(email='401316161@qq.com').first()
    allusers = User.query.all()
    for user in allusers:
        user.follow(adminuser)
    db.session.commit()

    flash('all the user followers 40131616@qq.com')
    return redirect(url_for('main.index'))

@auth.route('/fakepost')
def fakepost():
    Post.generate_fake(77)
   

    flash('77 posts have been faked by 40131616@qq.com')
    return redirect(url_for('main.index'))

@auth.route('/showaboutme')
def showaboutme():
    allusers = User.query.all()
    for user in allusers:
        user.showaboutme = True
    db.session.commit()
    flash('showaboutme is activated')
    return redirect(url_for('main.index'))


@auth.route('/notshowaboutme')
def notshowaboutme():
    allusers = User.query.all()
    for user in allusers:
        user.showaboutme = False
    db.session.commit()
    flash('showaboutme is de-activated')
    return redirect(url_for('main.index'))



'''no need this route, email is not changeable
@auth.route('/change_email_request')
@login_required
def change_email_request():
    return '<h1>changed email address</h1>'
'''

'''
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
'''
