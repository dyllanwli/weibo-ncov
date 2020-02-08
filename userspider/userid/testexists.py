import requests


def get_json(params):
        url = 'https://m.weibo.cn/api/container/getIndex?'
        r = requests.get(url, params=params)
        return r.json()

def get_user_info(user_id):
    params = {'containerid': '1076030' + str(user_id)}
    js = get_json(params)
    if js['ok']:
        return True


result = get_user_info("xiaopapi")
print(result)