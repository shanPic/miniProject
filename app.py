from flask import Flask
from flask import jsonify
from random import randint
from flask import request
from PIL import Image

app = Flask(__name__)

def errorReturn(arg,no,result):
    result['value'] = no
    result['error'] = arg
    return jsonify(result)


@app.route('/getSoreWithImg',methods=['GET', 'POST'])
def getScoreWithImg():
    if request.method=='POST':
        result = {}

        #获取url中传递过来的参数，若无此参数，则返回一个包含错误信息字段，与value键值为-1的json
        benchmark = request.form.get('benchmark') #基准视频编号
        if benchmark == None:
            return errorReturn('not have benchmark',-1,result)

        timeStamp = request.form.get('timestamp') #图片时间戳
        if timeStamp == None:
            return errorReturn('not have timestamp',-2,result)

        try:
            imgOri = request.files.get('img')
            if(imgOri==None):
                return errorReturn('the image is null',-3,result)
        except:
            return errorReturn('can\'t get image in this connect',-4,result)


        imgComp = Image.open(imgOri)
        # imgOri.save('')
        # f = open('','w+')
        # f.write(str(type(imgOri))+'\n')
        # f.write(print(imgOri)
        # f.close()

        # try:
        #     imgBenchmark = Image.open('/src/'+str(benchmark)+'/'+str(timeStamp)+'.jpg')
        # except:
        #     return errorReturn('can\'t find the timeStmp in this benchmark video',-5,result)


        score = randint(0,100)   #!TODO 此处调用后端算法接口得到分数
        result['value'] = score
        return jsonify(result)

@app.route('/')
def test():
    return app.send_static_file('test.html')
if __name__ == '__main__':
    app.run()
