import json
import jdcloud_sdk
from wx_sdk.build.lib import wx_sdk

def get_weather_dict(city: str):
    url = 'https://way.jd.com/he/freeweather'
    params = {
        'city': city,
        'appkey': '786d6924659f6b4f6ee40287cb5c25c8'
    }
    res = wx_sdk.wx_post_req(url, params)
    msg_dict = {}
    text = json.loads(res.text)
    msg_dict['city'] = city
    msg_dict['weather'] = (text['result']['HeWeather5'][0]['now']['cond']['txt'])
    msg_dict['max_tep'] = (text['result']['HeWeather5'][0]['daily_forecast'][0]['tmp']['max'])
    msg_dict['min_tep'] = (text['result']['HeWeather5'][0]['daily_forecast'][0]['tmp']['min'])
    msg_dict['dress_suggest'] = (text['result']['HeWeather5'][0]['suggestion']['drsg']['txt'])
    return msg_dict


def return_str(msg:dict):
    return f'你好～现在{msg["city"]}的天气是{msg["weather"]},最高温度为{msg["max_tep"]}' \
           f'度,最低温度为{msg["min_tep"]}度,{msg["dress_suggest"]}'
