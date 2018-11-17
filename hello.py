from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/owca')
def owca():
    return '<h1> Owce sa fajne yo </h1>'
@app.route('/animal/<name>')
def kotki(name):
    animals = {
        'kotki': 'https://bit.ly/2NT8EBm',
        'psy' : 'linkDoPsow'
    }
    return render_template('animals.html', link=animals[name] )
@app.route('/piesely')
def piesely():
    return '<img src="https://i.wpimg.pl/623x467/e5.pudelek.pl.sds.o2.pl/5bb3ccbd2e9c29a37000b82a590cd124a3e3370b">'

@app.route('/kotely')
def kotely():
    return '<img src="http://i.kinja-img.com/gawker-media/image/upload/s--H09kaYPk--/c_fit,fl_progressive,q_80,w_636/b7wucih6xfq6b8wjuurb.jpg">'