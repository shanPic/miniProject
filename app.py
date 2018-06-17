from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)


@app.route('/getSoreWithImg')
def hello_world():

    score = 0   #!TODO 此处调用后端算法接口得到分数
    result = {'value' : score}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
