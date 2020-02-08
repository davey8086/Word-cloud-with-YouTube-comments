# Word-cloud-with-YouTube-comments
## 功能：
下载YouTube视频下的评论，并将其另存为TXT文本。您可以将这些TXT文本转换为excel表，也可以直接使用注释的内容生成词云。

## 环境说明：
download.py的运行环境为python2.7.  
运行之前需要安装以下库:  
``` python 
pip install requests
pip install lxml
pip install cssselect
```
ciyun.py的运行环境为python3.7.  
建议使用conda创建虚拟环境使用。  
运行之前需要安装以下库：
``` python 
pip install numpy
pip install jieba
pip install wordcloud
```
此外PIL、matplotlib是常用库，就不加以说明了。  
  
txt2excel.py的运行环境为python2.7.  
依赖环境与download.py一致。  
## 使用说明及功能：
### download.py
``` python
conda activate py27
python download.py -y z0Acp6GNuuc # which is the SHORT ID of youtube website
python download.py -y z0Acp6GNuuc -o OutputFileName # which is the name of output file
```
结果保存的格式形如：
``` python 
{"text": "Shanghai looks beautiful, I hope to visit it the next year!", "time": "1 month ago", "author": "taxi driver", "cid": "Ugzgj0xbi2kdm6ggabl4AaABAg"}
```
### ciyun.py
首先说明，默认的编码方式为utf-8，将待处理的txt文件打开，文件-另存为-最下方编码格式-utf8 即可。  
``` python
python ciyun.py
```
在python文件中可以设置屏蔽词、显示词频最高的词的数量、输出格式。  
输出图片的色彩根据输入的wordcloud.jpg确定。
### txt2excel.py
根据设定好的分隔符来将文本切割为excel表格进行处理，注意同样需要更改txt的编码方式。  
暂时没有写parser，直接在py文件中更改待处理的文件名。
``` python
python txt2excel.py
```
