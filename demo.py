import urllib.request
import time
import datetime
from multiprocessing import Process

def fun_timer():  # 取代原来的IE定时重启refresh.bat 2020年6月14日23:12:22
    # global timer
    count = 0
    while True:
        url = 'https://oa.hbrc.gov.cn/wxrczfb/AutoReceipt.asp'
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
        response = urllib.request.urlopen(url)
        html = response.read().decode()
        if 'template_id' in html:  # 发出待办提醒后记录
            print(html)
            with open('log/' + str(datetime.date.today()) + '.html', 'a') as f:
                f.write(str(datetime.datetime.now()) + ',' + html + '<br>')
        time.sleep(30)
        count += 1
        print(count)
# if __name__ == '__main__':
#
#     p = Process(target=fun_timer)  # 提醒进程
#     p.start()  # 仅仅给操作系统发送了一个信号
li = [1, 2, 3, 4]
for i in enumerate(li):
    print(i)

