#coding:utf-8
import re
import requests
import base64
import datetime
import time
import re
import sys
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

	def parse_plist(url):
		id = r1(r'http://\w+.yinyuetai.com/video/(\d+)', url) or r1(r'http://\w+.yinyuetai.com/video/h5/(\d+)', url)
		#print(id)
		html = requests.get("http://www.yinyuetai.com/insite/get-video-info?json=true&videoId=%s" % id).json()
		#print(html)
		result = html['videoInfo']['coreVideoInfo']['videoUrlModels'][-1]['videoUrl']
		return result

	return parse_plist(video_url)


def test():
	# print parse_url("http://v.youku.com/v_show/id_XODMyNTI2ODI4.html")
	if (len(sys.argv)>1):
		print parse_url(sys.argv[1])
	else:
		print parse_url("http://v.yinyuetai.com/video/2704064")

if __name__ == '__main__':
	test()