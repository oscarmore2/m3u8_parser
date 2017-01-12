#!/usr/bin/python3 
import threading
import os
import sys 
import urllib
import urllib2
from time import ctime,sleep
import xml.dom.minidom
import re

baseUrl = "http://www.dark-holic.co.kr/product/detail.html?product_no=";
total = 3000

def Crawl(fromStr, toStr):

	for index in range(fromStr, toStr):
		try:
			url = baseUrl + str(index);
			req = urllib2.Request(url)
			req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)') 
			response = urllib2.urlopen(req)  
			html = response.read()

		except IOError as err:
			print('Catch Error:'+str(err))
			continue

		'''
		if html.find("http://img.cafe24.com/images/common/warn/logo_cafe24.gif") == -1:
			WriteJson(url)
			print "Got Real Url" + url
		else:
			print "Skip"
		'''
		#UniHtml = html.encode('utf-8')
		rr = re.compile(r'<!--(.+)-->')
		rr2 = re.compile(r'<!--(.+)')
		rr3 = re.compile(r'(.+)-->')
		rr4 = re.compile(r'<script(.+?)</script>', re.S)
		
		html = rr.sub('', html)
		html = rr2.sub('<!--', html)
		html = rr3.sub('-->', html)
		html = rr4.sub('', html)
		print html

		UniHtml = html.encode('utf-8')
		dom = xml.dom.minidom.parseString(html)
		root = dom.documentElement
		ParseHtml(root)

def ParseHtml(root):
	bodyDiv = root.getElementsByTagName('body')[0].getElementsByTagName('div')
	imgNode = []
	for div in bodyDiv:
		if (div.getAttribute('class') == '-image'):
			imgNode.append(div)

	for div in imgNode:
		imagepath = div.getElementsByTagName('img')[0].getAttribute('src')
		print imagepath

def WriteJson(str):
	output = open('data', 'a+')
	try:
		output.writelines(str)
	finally:
		output.close()
	print "Saving Url"

threads = []
th1 = threading.Thread(target=Crawl, args=(0, 1000))
th2 = threading.Thread(target=Crawl, args=(1001, 2000))
th3 = threading.Thread(target=Crawl, args=(2001, 3000))
threads.append(th1)
threads.append(th2)
threads.append(th3)

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('UTF-8')
	'''
	for th in threads:
		th.setDaemon(True)
		th.start()

	th.join()
	'''
	Crawl(1763, 1764)
	print "all over %s" %ctime()