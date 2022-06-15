from actions_toolkit import core

from app.push import work_wx_push
from app.weibo import get_rank

if __name__ == '__main__':
    push_url = core.get_input('webhook')
    weibo_rank = get_rank()
    work_wx_push(weibo_rank, push_url)
