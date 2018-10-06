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

def gradient_func(X, y, theta, m):
	diff = np.dot(X, theta) - y
	return (1. / m) * np.dot(np.transpose(X), diff)

def gradient_descent(X, y, alpha, m):
	theta = np.array([1, 1, 1]).reshape(3, 1)
	gradient = gradient_func(X, y, theta, m)
	while not np.all(np.absolute(gradient) <= 1e-2):
		theta = theta - alpha * gradient
		gradient = gradient_func(X, y, theta, m)
	return theta

def main():
	url = "https://bj.lianjia.com/ershoufang/pg1/"
	html = get_one_page(url)
	items = parse_one_page(html)

	m = len(items)

	X0 = np.ones((1, m)).reshape(m, 1)
	X1 = np.ones((1, m)).reshape(m, 1)
	X2 = np.ones((1, m)).reshape(m, 1)
	y = np.ones((1, m)).reshape(m, 1)

	for i in range(len(items)):
		y[i] = float(items[i][0])
		X1[i] = float(items[i][3]) #price
		X2[i] = float(items[i][1]) #bedroom
	X = np.hstack((X0, X1, X2))

	print(gradient_descent(X, y, 0.0001, m))




main()
