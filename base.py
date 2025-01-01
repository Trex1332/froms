from flask import Flask,redirect,session,render_template,url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,IntegerField,SubmitField,RadioField,BooleanField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

class tarkov (FlaskForm):
    fmap = RadioField("favourite map:  ",choices=[("woods","Woods"),("customs","Customs"),("labs","Labs"),("interchange","Interchange"),("light","Lighthouse"),("Ground","Ground Zero"),("reserve","Reserve"),("Streets","Streets"),("shorline","Shortline")])
    ftrader = RadioField("favourite Trader:  ",choices=[("Prapor","Prapor"),("therapist","Therapist"),("skeir","Skeir"),("peacekeeper","PeaceKeeper")("mechanic","Mechanic"),("jager","Jager","Ref","Ref")])
    wmap = RadioField("favourite map:  ",choices=[("woods","Woods"),("customs","Customs"),("labs","Labs"),("interchange","Interchange"),("light","Lighthouse"),("Ground","Ground Zero"),("reserve","Reserve"),("Streets","Streets"),("shorline","Shortline")])
    wgun = StringField("Worse Gun in game: ")
    deaths = IntegerField("How many deaths do you think you have had over the time you have been playing: ")
    submit = SubmitField("Submit")


@app.route('/',methods=["GET","POST"])
def index():
    form = tarkov()

    if form.validate_on_submit():
        session['fmap']= form.fmap.data
        session['ftrader']= form.ftrader.data
        session['wmap']= form.wmap.data
        session['wgun']= form.wgun.data
        session['deaths']= form.deaths.data

        return redirect(url_for('stats'))
    return render_template("home.html")

@app.route('/stats')
def stats():
    
    return render_template("stats.html")
                         