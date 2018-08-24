from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
