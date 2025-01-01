from flask import Flask,redirect,session,render_template,url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,IntegerField,SubmitField,RadioField,BooleanField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

class tarkov (FlaskForm):
    fmap = RadioField("Favourite map:  ",choices=[("woods","Woods"),("customs","Customs"),("labs","Labs"),("interchange","Interchange"),("light","Lighthouse"),("Ground","Ground Zero"),("reserve","Reserve"),("Streets","Streets"),("shorline","Shoreline")])
    ftrader = RadioField("Favourite Trader:  ",choices=[("Prapor","Prapor"),("therapist","Therapist"),("skeir","Skeir"),("peacekeeper","PeaceKeeper"),("mechanic","Mechanic"),("jager","Jager"),("Ref","Ref")])
    wmap = RadioField("Worse map:  ",choices=[("woods","Woods"),("customs","Customs"),("labs","Labs"),("interchange","Interchange"),("light","Lighthouse"),("Ground","Ground Zero"),("reserve","Reserve"),("Streets","Streets"),("shorline","Shortline")])
    deaths = IntegerField("How many deaths do you think you have had over the time you have been playing: ")
    submit = SubmitField("Submit")


@app.route('/',methods=["GET","POST"])
def index():
    form = tarkov()

    if form.validate_on_submit():
        session['fmap']= form.fmap.data
        session['ftrader']= form.ftrader.data
        session['wmap']= form.wmap.data

        session['deaths']= form.deaths.data

        return redirect(url_for('stats'))
    return render_template("home.html", form = form)

@app.route('/stats')
def stats():

    return render_template("stats.html")

if __name__ == '__main__':
    app.run(debug=True)