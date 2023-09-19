from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():  # 网站渲染
    return render_template('index.html')

@app.route('/index')
def home():
    # return render_template('index.html')
    return index()

@app.route('/comment')
def comment():  # 网站渲染
    datalist = []
    # 连接数据库
    con = sqlite3.connect('JDcomment1000.db')
    cur = con.cursor()         # 获得游标
    sql = 'select * from comment1000'
    data = cur.execute(sql)
    # 把数据放到列表中
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('comment.html',comments = datalist)

@app.route('/types')
def types():  # 网站渲染
    types = []  #评分区间
    num = []    #每个评分的数量
    # 连接数据库
    con = sqlite3.connect('JDcomment1000.db')
    cur = con.cursor()  # 获得游标
    sql = 'select types,count(types) from comment1000 group by types' #查询分数和分数数量
    data = cur.execute(sql)
    for item in data:
        types.append(str(item[0]))
        num.append(item[1])
    cur.close()
    con.close()
    return render_template('types.html',types = types,nums = num)

@app.route('/word')
def word():  # 网站渲染
    return render_template('word.html')

@app.route('/author')
def author():  # 网站渲染
    return render_template('author.html')

if __name__ == '__main__':
    app.run()
