from flask import Flask
from flask import jsonify
# import random
from flask import request
from PIL import Image
import chardet

app = Flask(__name__)

def errorReturn(arg,result):
    result['value'] = -1
    result['error'] = arg
    return jsonify(result)


@app.route('/getSoreWithImg',methods=['GET', 'POST'])
def getScoreWithImg():
    if request.method=='POST':
        result = {}

        #获取url中传递过来的参数，若无此参数，则返回一个包含错误信息字段，与value键值为-1的json
        benchmark = request.form.get('benchmark') #基准视频编号
        if benchmark == None:
            return errorReturn('not have benchmark',result)

        timeStamp = request.form.get('timestamp') #图片时间戳
        if timeStamp == None:
            return errorReturn('not have timestamp',result)

        try:
            imgOri = request.files.get('img')
            if(imgOri==None):
                return errorReturn('the image is null',result)
        except:
            return errorReturn('can\'t get image in this connect',result)


        imgComp = Image.open(imgOri)
        # imgOri.save('D:/CodeAndProject/Python/miniProject//src/test.jpg')
        # f = open('D:/CodeAndProject/Python/miniProject//src/erro.log','w+')
        # f.write(str(type(imgOri))+'\n')
        # f.write(print(imgOri)
        # f.close()

        try:
            imgBenchmark = Image.open('/src/'+str(benchmark)+'/'+str(timeStamp)+'.jpg')
        except:
            return errorReturn('can\'t find the timeStmp in this benchmark video',result)


        score = 0   #!TODO 此处调用后端算法接口得到分数
        result['value'] = score
        return jsonify(result)

@app.route('/')
def test():
    return app.send_static_file('test.html')
if __name__ == '__main__':
    app.run()
