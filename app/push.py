import json

import requests


def work_wx_push(form_data, push_urls):
    headers = {'Content-Type': 'application/json'}
    urls = push_urls.split(",")
    for url in urls:
        res = requests.post(url=url,
                            headers=headers,
                            data=json.dumps(form_data),
                            timeout=5,
                            verify=False)
        print(res)
