import requests
import re
import numpy as np

def get_one_page(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	return None

def parse_one_page(html):
	pattern = re.compile('<div class="price"><span>(.*?)</span>万</div>.*?(\d)室(\d)厅<span>/</span>(.*?)平米<span>', re.S)
	items = re.findall(pattern, html)
	return items

url = 'https://bj.lianjia.com/ershoufang/pg1/'
html = get_one_page(url)
print(parse_one_page(html))
m = 10

X0 = np.arange(1, m+1).reshape(m, 1)
X1 = np.arange(1, m+1).reshape(m, 1)
X2 = np.arange(1, m + 1).reshape(m, 1)
y = np.arange(1, m+1).reshape(m, 1)
X = np.hstack((X0, X1, X2))

theta = np.array([1, 1, 1]).reshape(3, 1)

diff = np.dot(X, theta)

X9 = np.ones((1, 20)).reshape(20, 1)
print(X9)