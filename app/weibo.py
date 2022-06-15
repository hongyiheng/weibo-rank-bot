import json
import re

import requests


def get_tid():
    res = requests.post("https://passport.weibo.com/visitor/genvisitor?cb=gen_callback")
    obj = json.loads(str(res.content)[38:-3])
    return obj['data']['tid']


def get_cookie(tid):
    params = {
        'a': 'incarnate',
        't': tid,
        'w': 3,
        'c': 100,
        'cb': 'cross_domain',
        'from': 'weibo'
    }
    res = requests.get("https://passport.weibo.com/visitor/visitor", params)
    obj = json.loads(str(res.content)[38:-3])
    return "SUB=" + str(obj['data']['sub']) + ";SUBP=" + str(obj['data']['subp'])


def get_html(cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': cookie
    }
    res = requests.get("https://s.weibo.com/top/summary", headers=headers)
    return res.text


def parse(content):
    match = re.compile('<td class="td-02">(.*?)</td>', re.DOTALL)
    data = match.findall(content)
    rank = []
    for i in range(10):
        link_data = re.search('<a href="(.*?)" target', data[i].strip())
        title_data = re.search('>(.*?)</a>', data[i].strip())
        if not link_data or not title_data:
            continue
        link = "https://s.weibo.com/" + link_data.group(1)
        title = title_data.group(1)
        rank.append(f'> - [{title}]({link})\n')
    return rank


def get_rank():
    tid = get_tid()
    cookie = get_cookie(tid)
    content = get_html(cookie)
    rank = parse(content)
    return {
        'msgtype': 'markdown',
        'markdown': {
            'content': f'### 微博当前热搜\n{"".join(rank)}'
        }
    }
