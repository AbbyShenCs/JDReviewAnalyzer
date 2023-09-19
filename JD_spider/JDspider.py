# -*- coding = utf-8 -*-
# @Time : 2021/5/24 17:44
# @Author : 沈奥 
# @File : JDspider.py
# @Software : PyCharm

# 导入所需库
import requests
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


class Jdcomment_spider(object):


    # 实例化类的时候运行初始化函数
    def __init__(self, file_name='jd_comment'):
        self.headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
        self.datalist = []

        # 打开文件
        self.fp = open(f'./{file_name}.txt', 'w', encoding='utf-8')
        print(f'正在打开文件{file_name}.txt文件!')


    #解析一页的方法
    def parse_one_page(self, url):
        # 指定url
        # url = 'https://club.jd.com/comment/productPageComments.action?productId=100016138846&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
        # print(url)
        # 发起请求
        response = requests.get(url, headers=self.headers)
        # 获取响应
        js_data = response.json()

        # 提取评论列表
        comments_list = js_data['comments']

        for comment in comments_list:
            data = []
            # 商品id
            goods_id = comment.get('id')
            data.append(goods_id)
            # 用户昵称
            nickname = comment.get('nickname')
            data.append(nickname)
            # 评分
            score = comment.get('score')
            data.append(score)
            # 商品尺寸
            productSize = comment.get('productSize')
            data.append(productSize)
            # 商品颜色
            productColor = comment.get('productColor')
            data.append(productColor)
            # 评论时间
            creationTime = comment.get('creationTime')
            data.append(creationTime)
            # 评论内容
            content = comment.get('content')
            content = ' '.join(content.split('\n'))  # 处理换行符
            data.append(content)
            print(content)

            # 循环写出数据
            self.fp.write(f'{goods_id}\t{nickname}\t{score}\t{productSize}\t{productColor}\t{creationTime}\t{content}\n')
            self.datalist.append(data)

    def parse_max_page(self):
        for page_num in range(100):  # 抓包获得最大页数
            # 指定通用的url模板
            new_url = f'https://club.jd.com/comment/productPageComments.action?productId=100007254183&score=0&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&rid=0&fold=1'
            print(f'正在获取第{page_num}页')

            # 调用函数
            self.parse_one_page(url=new_url)


    def close_files(self):
        self.fp.close()
        print('爬虫结束，关闭文件！')

    def saveData(self,savepath = '.\\京东评论1000条1.xls'):
        print('save...')
        book = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
        sheet = book.add_sheet('京东评论1000条', cell_overwrite_ok=True)  # 创建工作表
        col = ('商品id', '用户昵称', '评分', '商品型号', '商品系列', '评论时间','评论内容')
        for i in range(0, 7):
            sheet.write(0, i, col[i])  # 列名
        for i in range(0, 4):
            print('第%d条' % (i + 1))
            data = self.datalist[i]
            for j in range(0, 7):
                sheet.write(i + 1, j, data[j])  # 数据
        book.save(savepath)  # 保存数据表

    def saveDataToDB(self, dbpath):
        self.init_db(dbpath)
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()  # 得到游标
        # 将每一条的电影信息组成一个sql语句
        for data in self.datalist:
            for index in range(len(data)):
                # if index == 4:
                #     continue
                # 数据库中字符串需要加引号
                data[index] = '"' + str(data[index]) + '"'
            sql = '''
                    insert into comment1000(
                    user_id,nickname,score,types,series,times,info)
                    values(%s)''' % ','.join(data)
            print(sql)
            cur.execute(sql)
            conn.commit()
        cur.close()
        conn.close()

    def init_db(self, dbpath):
        sql = '''
               create table comment1000
               (
               id integer primary key autoincrement,
               user_id text,
               nickname text,
               score text,
               types text,
               series text,
               times text,
               info text 
               )
           '''
        # 创建
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    # 实例对象
    jd_spider = Jdcomment_spider()
    # 开始爬虫
    jd_spider.parse_max_page()
    # 保存数据
    dbpath='JDcomment1000.db'
    jd_spider.saveData()
    #jd_spider.init_db('comment_test.db')
    jd_spider.saveDataToDB(dbpath)
    # 关闭文件
    jd_spider.close_files()
