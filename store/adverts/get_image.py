import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://img-pre.ivsky.com/img/tupian/pre/202104/03/'

#def get_image(link, file):
	#url2 = 'https://img-pre.ivsky.com'
	#req = urllib.request.Request(link)
	#req.add_header("User-Agent", \
	#	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
	#page = urllib.request.urlopen(req)
	#html_data = page.read().decode('utf-8')


def percentage(a, b, c):
	per = 100.0 * a * b / c
	if per > 100:
		per = 100
	print('%.2f%%' % per)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)


for n in range(13, 30):
	url = 'https://img-pre.ivsky.com/img/tupian/pre/202104/03/sunyunzhu_duanxiushan_baotunqun-%03d.jpg' % (n)
	filename = 'pic-%03d.jpg' % n
	print(url)
	urllib.request.urlretrieve(url, filename, percentage)
	print("Done.")
