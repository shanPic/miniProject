from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)


    @app.route('/getSoreWithImg')
def hello_world():
    result = {'value' : random.randint(0,10)}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
