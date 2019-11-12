# 导入Flask类
from flask import Flask, request, render_template, redirect, url_for, session
import database
from flask_cors import CORS
import os, time, random
import base64,data
from Model.models import User,News

from PIL import Image

# 实例化，可视为固定格式
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.debug = True
app.config['SECRET_KEY'] = "mjwebsite"


# ****新闻相关接口****
# 默认的地址
@app.route('/')
def defaultPage():
    return render_template('index.html')


# 获取该类全部新闻
@app.route('/allnews/<id>')
def getAllNewsByType(id):
    newsArr = database.getAllnewsByType(id)
    print("length===", len(newsArr))
    return render_template('newsList.html', newsArr=newsArr)


# 根据新闻id获取新闻信息
@app.route('/news/<id>')
def getNewsByid(id):
    idd = request.args.get('id', 15)
    news = database.getDataById(idd)
    baseUrl = "/static/newsImages/"
    picUrl = '20190717142047.jpg'
    if news['picurl']:
        picUrl = news.picture
    url = baseUrl + picUrl
    return render_template('newsdetail.html', url=url, news=news, newTypes=data.types)


# 更改新闻内容
@app.route('/change/', methods=['POST'])
def changeNewsData():
    fileName = uploadFile()
    if fileName == '0':
        return '0'
    news = News()
    news.picture=fileName
    news.title = request.form.get('title')
    news.content = request.form.get('content')
    news.writer = request.form.get('writer')
    news.time = request.form.get('time')
    news.id = request.form.get('id')
    news.ntype = request.form.get('type')
    success = "0"
    if database.changeNewsData(news):
        success = "1"
    return success


# 插入新闻接口
@app.route('/insert/', methods=['POST'])
def insertNesData():
    fileName = uploadFile()
    if fileName == '0':
        return '0'
    title = request.form.get('title')
    content = request.form.get('content')
    writer = request.form.get('writer')
    time = request.form.get('time')
    ntype = request.form.get('type')

    success = "0"
    if database.insertData(title, content, writer, time, ntype, fileName):
        success = '1'
    return success


# 上传文件
@app.route('/upload', methods=['POST'])
def uploadFile():
    print("length==", request.form)
    if request.form.get("filedata"):
        imgBase64 = request.form.get("filedata").split(',')[1];
        imgBase64 = imgBase64.replace(' ', "+")
        fileSuffix = "." + request.form.get('filename').split('.')[1]
        imgdata = base64.b64decode(imgBase64)
        newfileName = time.strftime('%Y%m%d%H%M%S') + str(random.randint(0, 9)) + fileSuffix
        print('filename==', newfileName)
        file = open('./static/newsImages/' + newfileName, 'wb')
        file.write(imgdata)
        file.close()
        return newfileName
    elif request.form.get("filename"):
        return request.form.get("filename")
    else:
        return '0'


# 删除新闻
@app.route('/delete', methods=['POST'])
def deleteNews():
    id = request.form.get('id')
    return database.deleteNews(id)


# 后台新闻列表
@app.route('/bknewslist/<typeCode>')
def bkNewsListByType(typeCode):
    newsArr = database.getAllnewsByType(typeCode)
    name = session['name']
    return render_template('bknewsList.html', newsArr=newsArr, name=name)


# 展示新闻详情
@app.route('/showdetail/<nid>')
def showNewsDetail(nid):
    print('nid==', nid)
    news = database.getDataById(nid)
    baseUrl = "/static/newsImages/"
    picUrl = '20190717142047.jpg'
    if news.picture:
        picUrl = news.picture
    url = baseUrl + picUrl
    return render_template('showNewsDetail.html', url=url, news=news)


# 后台展示新闻详情
@app.route('/bkshowdtetail/<nid>')
def showbkNewsDetail(nid):
    print('nid==', nid)
    news = database.getDataById(nid)
    baseUrl = "/static/newsImages/"
    picUrl = '20190717142047.jpg'
    if news.picture:
        picUrl = news.picture
    url = baseUrl + picUrl
    url = url
    name = session['name']
    return render_template('newsdetail.html', url=url, newTypes=data.types, name=name, news=news)


# 检查文件类型
def check_file_type(filename):
    file_type = ['jpg', 'doc', 'docx', 'png', 'txt', 'pdf', 'PDF',
                 'png', 'PNG', 'xls', 'rar', 'exe', 'md', 'zip', 'xlsx']
    # 获取文件后缀
    ext = filename.split('.')[1]
    # 判断文件是否是允许上传得类型
    if ext in file_type:
        return True
    else:
        return False


# ****用户信息相关接口****
# 用户登录 (1：成功；0：失败)
@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


# 用户信息
@app.route('/userInfo', methods=['POST', 'GET'])
def userInfo():
    if request.method == 'POST':
        user = User()
        user.name = request.form.get("name")
        session['name'] = user.name;
        user.pwd = request.form.get("password")
        result = database.checkUser(user.name, user.pwd)
        if result:
            user.pNumber = result[0][3]
            user.age = result[0][2]
            user.sex = "male"
            if not result[0][5]:
                user.sex = "femail"
            return render_template("userInformation.html", user=user)
        return redirect(url_for('login'))


# 错误处理 404错误
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404


# 错误处理 500错误
@app.errorhandler(500)
def serverError(e):
    return render_template('500.html'), 500


# main方法
if __name__ == '__main__':
    # 运行项目并设置host(地址)及port(端口)
    # app.run(host="10.237.168.103", port=int("8080"))
    app.run(host="0.0.0.0", port=8080)
