from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def meet_hello():
    return render_template('site_site.html')


@app.route('/registr')
def reg_hel():
    return render_template('registration.html')



if __name__ == '__main__':
    app.run(port=8087, host='127.0.0.1')


