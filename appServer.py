# encoding: utf-8
from flask import Flask,request,redirect,url_for
from flask import render_template
from dbManage import dbManage

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello world")
    return 'Hello World!'
    result = {"code":0, "data":{"msg":"Hello World"}}
    return result
    return render_template("index.html")

# 点餐
@app.route('/orderFood')
def orderFood():
    foodsdb = dbManage()
    foodsdb.connect()
    food = dict()
    food[1] = ["宫保鸡丁", "红烧肉"]
    food[2] = ["宫保鸡丁", "红烧肉"]
    food[3] = ["宫保鸡丁", "红烧肉"]
    food[4] = ["宫保鸡丁", "红烧肉"]
    week = [1, 2, 3, 4, 5]
    for day in week:
        menuresult = foodsdb.selectmenusBynew(day)
        print(menuresult)
    foodsdb.close()
    return render_template("orderFood.html", week=week, food = food)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
       result = request.form
       for key, value in result.items():
          print(key, value)
       return render_template("result.html",result = result)

# 管理员输入菜单
@app.route('/enterMenu')
def enterMenu():
    week = [1,2,3,4,5]
    return render_template("enterMenu.html", week=week)

@app.route('/dealMenu', methods=['POST', 'GET'])
def delMenu():
    foodsdb = dbManage()
    foodsdb.connect()
    menu = ""
    result = request.form
    print(result)
    week = -1
    for key, value in result.items():
        if key == "week":
           week = value
        if value:
            print(value)
            foodsdb.insertfoods(value)
            tmp = foodsdb.selectfoods(value)
            menu += str(tmp[0]) + ','

    menu = menu[:-2]
    print(menu)
    foodsdb.insertmenu(menu, week, None)
    # menuresult = foodsdb.selectmenusBynew()
    # print(menuresult)
    # print(url_for(""))
    foodsdb.close()
    return redirect("/")
    
  

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True, threaded=True)
    #app.run(host='0.0.0.0',port=8000, debug=False, threaded=True, ssl_context=('/home/junkings/214854703950213/public.crt', '/home/junkings/214854703950213/214854703950213.key'))
