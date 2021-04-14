from bs4 import BeautifulSoup
import requests

url = 'http://tianqi.2345.com/today-54774.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

file = open('result.csv', 'w')
# find_all函数，返回符合attrs的所有a字符串标题和内容，其中标题部分可以用字典的方式查询
msg_list = soup.find_all('a', attrs={"class": "hours24-list-item"})
for msg in msg_list:
    # select函数，返回内容中所选标签类型列表
    dis = msg.select('b')[0].text
    # 字典方式获取标题中的属性
    describe = msg.get('title')
    level = msg.select('b')[1].text
    quantity = msg.select('span')[0].text
    content = dict()
    content["风向"] = dis
    file.write("风向:"+dis+" 等级:"+level+" 质量:"+quantity+" 描述:"+describe + '\n')
