#!/usr/bin/env python
# -*- coding:UTF-8 -*-# 导入扩展库
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库

# 读取文件
fn = open('article.txt','r',encoding='UTF-8') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
remove_words = [u',', u'time',u'{', u'}', u'text', u'ago', u'author',u'cid',u'months',u'years',u':',u' ',u'.',u'1',u'2',u'month',
                u'year',u'the',u'to',u'and',u'\\',u'!',u'is',u'of',u'"',u'_',u'in',u'you',u'a',u'are',u's',u'that',u'I',u'for',u'/',
                u'n',u'@',u'it',u'from',u'not',u't',u'with',u'have',u'they',u'on',u'😂',u'your',u'will',u'all',u'be',u'as',u'this',
                u'The',u'can',u'like',u'3',u'about',u'by',u'so',u'but',u'know',u'what',u'’',u'‘',u'do',u' ',u'he',u'or',u'was',u'their',
                u',',u'，',u'more',u'has',u'don',u'edited',u'who',u'me',u'them',u'we',u'no',u'one',u'de',u'You',u'just',u'&',u'at',u'other',
                u'的',u'u',u'only',u'china',u'if',u'countries',u'up',u'í',u'why',u'an',u'my',u'out',u'even',u'than',u'very',u'。',u'there',u'👍' ,
                u'how',u'see',u'want',u'go',u'que',u'、',u'also',u'any',u'Khan',u'make',u'would',u'4',u'its',u'never',u'r',u'his',u'get',u'because',
                u'many',u'those',u'when',u'That',u'then',u'most',u'still',u'It',u'been',u'👹',u'👏',u'\'',u'i',u'A',u'THE',u'We',u'm',u'He',u'unfir',u'Ugyl6RHEdBX1a5joTB4AaABAg',
                u'nJRMbG0Ore',u'Ugy9Z',u'YGCLdXlmmhS1x4AaABAg',u'nFt',u'PGgmFw',u're',u'too',u'á',u'am',u'us',u' ＋',u'And',u'CHINA',u'This',u'O7',u'some',u'ing',
                u'Muhamad',u'Arole',u'Flynn',u'chinese',u'Baloch',u'SKJP',u'Sanky',u'en',u'Aiman',u'But',u'same',u'é',u'If',u'la',u'Leow',u'JS',u'S',u'these',u'\xa0',u'Why']# 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(75) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('wordcloud.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/Arial.ttf', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=75, # 最多显示词数
    max_font_size=233, # 字体最大值
    width=1920,
    height=1080,
    background_color=(255,255,255)
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.savefig("temp.png",dpi=500,bbox_inches = 'tight')
plt.show() # 显示图像
plt.close()

