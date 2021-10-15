import bs4
import execjs
import requests
import init

url = 'http://202.204.122.1/checkLogin.jsp'


def connect():
    try:
        with requests.sessions.Session() as s:
            r = s.get('http://202.204.122.1')
            md5_f = s.get('http://202.204.122.1/public/js/md5.js')

            soup = bs4.BeautifulSoup(r.content, 'lxml')
            no = soup.find("input", id='no')
            ip = soup.find("input", id='ip')
            passwd = execjs.compile(md5_f.text).call('hex_md5', init.internet_account[1])
            passwd = execjs.compile(md5_f.text).call('hex_md5', passwd + no['value'])
            data = {
                'username8': init.internet_account[0],
                'password8': passwd,
                'ip': ip['value'],
                'no': no['value'],
                'action': 'connect'
            }
            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '107',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': '202.204.122.1',
                'Origin': 'http://202.204.122.1',
                'Referer': 'http://202.204.122.1/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
            }
            log = s.post(url=url, headers=header, data=data)

            soup = bs4.BeautifulSoup(log.text, 'lxml')
            ls = soup.findAll("frame")

            for i in ls:
                if 'main' in i.__str__():
                    result = s.get('http://202.204.122.1/user/' + i['src'], headers=header)
                    if "联网成功" in result.text:
                        return 1
                    elif "用户已在本主机上登录，不需要重新登录" in result.text:
                        return 1

            return -1
    except:
        return -1
