import requests
from lxml import etree

urls = "https://nba.hupu.com/stats/players"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
resp = requests.get(urls, headers=headers)

e = etree.HTML(resp.text)

# 排名
nos = e.xpath('//*[@id="data_js"]/div[4]/div/table/tbody/tr/td[1]/text()')
# 球员
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
# 球队
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
# 得分
scores = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')

for no, name, team, score in zip(nos, names, teams, scores):
    print(f'排名:{no}, 球员:{name},球队:{team}, 得分:{score}')
