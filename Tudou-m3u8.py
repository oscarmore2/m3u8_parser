#coding:utf-8
import re
import requests
import base64
import datetime
import time
import sys
import re
import json
import urllib
import urllib2

fake_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0'
}

def r1(pattern, text):
	m = re.search(pattern, text)
	if m:
		return m.group(1)

def parse_url(video_url):

	def get_decoded_html(url, faker = True):
		request = urllib2.Request(url)
		request.add_header("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D5145e Safari/9537.53")
		response = urllib2.urlopen(request)
		data = response.read()
		
		charset = r1(r'charset=([\w-]+)', response.headers['content-type'])
		if charset:
			return data.decode(charset, 'ignore')
		else:
			return data

	def parse_plist(url):
		html = get_decoded_html(url)
		#print(html)
		iid = r1(r"iid:*\s(\d*)", html)
		print(iid)
		result = 'http://vr.tudou.com/v2proxy/v2.m3u8?it=%s' % iid
		return result

	return parse_plist(video_url)


def test():
	# print parse_url("http://v.youku.com/v_show/id_XODMyNTI2ODI4.html")
	if (len(sys.argv)>1):
		print parse_url(sys.argv[1])
	else:
		print parse_url("http://www.tudou.com/programs/view/ou5lK2ZrHxg/?spm=a2h0k.8191414.ou5lK2ZrHxg.A")

if __name__ == '__main__':
	test()