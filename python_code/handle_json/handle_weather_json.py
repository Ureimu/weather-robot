import json
import jdcloud_sdk
from wx_sdk.build.lib import wx_sdk

def get_weather_str(city: str):
    url = 'https://way.jd.com/he/freeweather'
    params = {
        'city': city,
        'appkey': '786d6924659f6b4f6ee40287cb5c25c8'
    }
    res = wx_sdk.wx_post_req(url, params)
    msg_dict = {}
    text = json.loads(res)
    msg_dict['weather'] = (text['result']['HeWeather5'][0]['now']['cond']['txt'])
    msg_dict['max_tep'] = (text['result']['HeWeather5'][0]['daily_forecast'][0]['tmp']['max'])
    msg_dict['min_tep'] = (text['result']['HeWeather5'][0]['daily_forecast'][0]['tmp']['min'])
    return msg_dict
