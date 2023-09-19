# -*- coding = utf-8 -*-
# @Time : 2020/11/24 22:57
# @Author : 沈奥 
# @File : testCloud.py
# @Software : PyCharm

import string
from zhon.hanzi import punctuation
import jieba  # 分词
from matplotlib import pyplot as plt # 绘图，数据可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库

# 准备词云所需的文字(词)
con = sqlite3.connect('JDcomment1000.db')
cur = con.cursor()
sql = 'select info from comment1000'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
    print(item[0])
print(text)
cur.close()
con.close()

cut = jieba.cut(text)
s = ' '.join(cut)
dicts={i:'' for i in punctuation}
punc_table=str.maketrans(dicts)
new_s=s.translate(punc_table)
print(new_s)
print(len(new_s))

fp=open('comment_word.txt','w',encoding='utf-8')
fp.write(new_s)
fp.close()

img = Image.open(r'.\static\assets\img\JDdog.jpg')  # 打开遮罩图片
img_array = np.array(img)  # 将图片转化成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='msyhbd.ttc'  # 字体所在位置 C:\Windows\Fonts
)
wc.generate_from_text(s)

# 绘制图片
fig = plt.figure(1) # 第一个位置
plt.imshow(wc)
plt.axis('off')
# plt.show()   # 显示生成的词云图片

# 输出词云的图片到文件
plt.savefig(r'.\static\assets\img\JD_word1.jpg',dpi=1000)