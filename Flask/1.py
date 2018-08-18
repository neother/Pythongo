# virtual enviroment path C:\Users\moochergaga\Envs\Pyflask\Scripts\
# activate the envi first
from flask import Flask
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import Flask, render_template, session, redirect, url_for, flash
app = Flask(__name__)
#manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hardtoguess'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
        #form.name.data = ''

    return render_template('index.html', name=session.get('name'), form=form, current_time=datetime.utcnow())


@app.route('/user/<id>')
def get_user(id):

    return render_template('user.html', name=id)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
