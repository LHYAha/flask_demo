#-*- coding = utf-8-*-
#@Time : 2020/6/26 11:02
#@Author :Ella
#@File :app.py
#@Software : PyCharm

import time
import datetime

from flask import Flask,render_template,request  #render_template渲染模板
app = Flask(__name__)  #初始化的对象

#路由解析，通过用户访问的路径，匹配想要的函数
@app.route('/')
def hello_world():
    return '你好'

#通过访问路径，获取用户的字符串参数
@app.route('/test1/<name>')
def test1(name):
    return '你好，%s'%name

#通过访问路径，获取用户的整形参数    此外，还有float类型
@app.route('/test2/<int:id>')
def test2(id):
    return '你好，%d'%id

#返回给用户渲染后的网页文件
# @app.route('/index1')
# def index1():
#     return render_template("index.html")

#向页面传递变量
@app.route('/index1')
def index2():
    time = datetime.date.today()  #普通变量
    name = ['小新','小英','小红'] #列表类型
    task = {"任务":"打扫卫生","时间":"3小时"} #字典类型
    return render_template("index.html",var = time,list = name,task = task)

#表单提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")

#接受表单提交的路由，需要指定methods为post
@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html",result = result)

if __name__ == '__main__':
    app.run(debug=True)