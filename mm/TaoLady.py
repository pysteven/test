#coding:utf-8
#python3
import requests
import json
from urllib.request import urlopen

# 发送请求，得到JSON数据，将其加工并转化为Python的字典类型返回
def getInfo(pageNum):
    tao_data = {"viewFlag":"A", "currentPage": pageNum}
    try:
        r = requests.post("https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8", data = tao_data)
    except:
        return None
    raw_datas = json.loads(r.text)
    datas = raw_datas['data']['searchDOList']
    return datas

def main():
    # 淘女郎一共有410页，所以我们可以抓取从1到第411页的内容，这取决于你的硬盘容量，这里我只抓取第一页。
	for pageNum in range(1, 2):
		print(pageNum)
		datas = getInfo(pageNum)
		if datas:
			for data in datas:
				name = data['realName']
				url = "http:" + data['avatarUrl']
				pic = urlopen(url)
				#在桌面项目文件夹mm下再新建一个文件夹，取名picture，并把其路径复制过来
				with open("C://Users/Administrator/Desktop/mm/picture/" + name + ".jpg", "wb") as file:
					print(name)
					file.write(pic.read())

if __name__ == '__main__':
    main()
