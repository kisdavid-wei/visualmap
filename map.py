from flask import Flask
from flask import render_template
import configparser

app = Flask(__name__)

@app.route('/')
def index():
    config = configparser.ConfigParser()
    path = 'app.config'
    config.read(path)
    gaodekey = config.get('key', 'gaodekey')
    return render_template('map.html',gaodekey=gaodekey)

if __name__ == '__main__':
    app.run()