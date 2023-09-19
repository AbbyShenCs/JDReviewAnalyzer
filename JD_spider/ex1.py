# -*- coding = utf-8 -*-
# @Time : 2021/5/24 17:46
# @Author : 沈奥 
# @File : ex1.py
# @Software : PyCharm

# 导入包
import requests
import json
# 指定url
url = 'https://club.jd.com/comment/productPageComments.action?productId=100016138846&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'

# 伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

# 发起请求
response = requests.get(url,headers=headers)

# 将json格式字符串转换成字典，才能以键值对的形式将想要的信息提取出来

# 方式一：使用json包中内置的函数loads
# js_data = json.loads(response.text)
# print(js_data)
# print(type(js_data))

# 方式二 使用response.json方法提取json里面的字符串
js_data = response.json()

# 从字典中取出值————解析数据
# 提取comment字典里的值
comment_list = js_data['comments']
#print(comment_list)

for comment in comment_list:
    # 商品id
    goods_id = comment.get('id')
    # 用户昵称
    nickname = comment.get('nickname')
    # 评分
    score = comment.get('score')
    # 商品尺寸
    productSize = comment.get('productSize')
    # 商品颜色
    productColor = comment.get('productColor')
    # 评论时间
    creationTime = comment.get('creationTime')
    # 评论内容
    content = comment.get('content')
    content = ' '.join(content.split('\n'))  # 处理换行符

    print(content)
