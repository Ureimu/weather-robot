import json


def get_pythonlic_json(res:str):
    text = json.loads(res)
    msg = text['result']['HeWeather5'][0]['now']['cond']['txt']
    return msg
