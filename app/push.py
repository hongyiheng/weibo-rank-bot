import json

import requests


def work_wx_push(form_data, push_urls):
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=push_urls,
                        headers=headers,
                        data=json.dumps(form_data),
                        timeout=5,
                        verify=False)
    print(res)
