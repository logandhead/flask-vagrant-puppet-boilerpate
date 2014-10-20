from os import listdir
from flask import Flask, render_template
from assets import asset_register

app = Flask(__name__)
# register asset bundles
asset_register(app)

@app.route('/')
def hello():
    return render_template('base.html')
