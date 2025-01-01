from flask import Flask,redirect,session,render_template,url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,IntegerField,SubmitField,RadioField,BooleanField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

class tarkov (FlaskForm):
    fmap = RadioField("favourite map:  ",choices=[("woods","Woods"),("customs","Customs"),("labs","Labs"),("interchange","Interchange"),("light","Lighthouse"),("Ground","Ground Zero"),("reserve","Reserve"),("Streets","Streets"),("shorline","Shortline")])
