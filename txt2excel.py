#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
env:
Python 2.7
pip install requests
pip install lxml
pip install cssselect

usage:
python download.py -y z0Acp6GNuuc # which is the id of youtube website

description:
Results will be saved in youtube_id.txt. 
{"text": "Shanghai looks beautiful, I hope to visit it the next year!", "time": "1 month ago", "author": "taxi driver", "cid": "Ugzgj0xbi2kdm6ggabl4AaABAg"}

'''

import xlwt
import sys
#可以用中文
#reload(sys)
#sys.setdefaultencoding('utf-8')

def txt_xls(filename,xlsname):
	try:
		f=open(filename,'r',encoding='UTF-8')
		xls=xlwt.Workbook()
		sheet=xls.add_sheet('sheet1',cell_overwrite_ok=True)
		x=0
		while True:
			line=f.readline()
			if not line:
				break
			for i in range(len(line.split('"'))):	#设置分隔符为"
				item = line.split('"')[i]
				sheet.write(x,i,item)
			x+=1
		f.close()
		xls.save(xlsname)
	except:
		raise

if __name__=="__main__":
	filename="comments/6Gjm0zUncZY.txt"
	xlsname="excel/6Gjm0zUncZY.xls"
	txt_xls(filename,xlsname)


	