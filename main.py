import requests


if __name__ == "__main__":

    # step 1: 爬取网页数据

    url = 'https://www.pixiv.net/'

    home_text = requests.get(url).text

    # step 2: 解析爬取数据

    # step 3: 存储爬取数据
    save_path = './pixiv1.html'
    with open(save_path, 'w', encoding='utf-8') as fp:
        fp.write(home_text)
        print("下载成功!")