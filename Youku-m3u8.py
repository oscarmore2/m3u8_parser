#coding:utf-8
import re
import requests
import base64
import datetime
import time
import urllib

def parse_url(video_url):
	def get_video_id(video_url):
		pattern = re.compile("id_(\w+)")
		match = pattern.findall(video_url)
		if match:
			return match[0]

	def my_encoder(a, c):
		"""str, str->str 
		This is an RC4 encryption."""
		f = h = 0
		b = list(range(256))
		result = ''
		while h < 256:
			f = (f + b[h] + ord(a[h % len(a)])) % 256
			b[h], b[f] = b[f], b[h]
			h += 1
		q = f = h = 0
		while q < len(c):
			h = (h + 1) % 256
			f = (f + b[h]) % 256
			b[h], b[f] = b[f], b[h]
			if isinstance(c[q], int):
				result += chr(c[q] ^ b[(b[h] + b[f]) % 256])
			else:
				result += chr(ord(c[q]) ^ b[(b[h] + b[f]) % 256])
			q += 1
		return result

	vid = get_video_id(video_url)
	if not vid:
		return
	infoUrl = 'http://play.youku.com/play/get.json?vid='+vid+'&ct=12&Type=Folder&ob=1'
	r = requests.get(infoUrl)
	json_result = r.json()
	data = json_result['data']
	sec = data['security']
	video_ip = sec['ip']
	video_ep = sec['encrypt_string']
	#video_ip = json_result['data'][0]['ip']
	#video_ep = json_result['data'][0]['ep']
	template1 = "becaf9be";
	template2 = "bf7e5f01";
	bb = bytes(video_ep)
	print(bb)
	decoded = base64.b64decode(bb)
	#bytess = map(lambda x:ord(x), decoded)
	temp = my_encoder(template1, decoded)
	temp_splited = temp.split('_')
	sid = temp_splited[0]
	token = temp_splited[1]
	whole = sid + '_' + vid + '_' + token
	#new_bytes = map(lambda x:ord(x), whole)
	ep_new = my_encoder(template2, whole)
	ep_new = urllib.quote(ep_new)
	ts = time.mktime(datetime.datetime.now().timetuple())
    #"&type=flv&ts="+str(ts)+"&keyframe=0&ep="+ep_new+"&sid="+str(sid)+"&token="+token+"&ctype=12&ev=1&oip="+str(video_ip)
	final_url = "http://pl.youku.com/playlist/m3u8?vid="+vid+"&type=mp4&ts="+str(ts)+"&keyframe=0&ep="+ep_new+"&sid="+str(sid)+"&token="+token+"&ctype=12&ev=1&oip="+str(video_ip)
	return final_url


def test():
	# print parse_url("http://v.youku.com/v_show/id_XODMyNTI2ODI4.html")
	print parse_url("http://v.youku.com/v_show/id_XMTgxODc5MjgzMg==.html")

if __name__ == '__main__':
	test()