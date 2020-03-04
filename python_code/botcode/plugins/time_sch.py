from datetime import datetime
import handle_json.handle_json
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from wx_sdk.build.lib import wx_sdk

url = 'https://way.jd.com/he/freeweather'
params = {
    'city': '绵阳',
    'appkey': '786d6924659f6b4f6ee40287cb5c25c8'
}

response = wx_sdk.wx_post_req(url, params)
print(response.text)
msg = handle_json.handle_json.get_pythonlic_json(response.text)


@nonebot.scheduler.scheduled_job('cron', hour='*',minute='15')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_private_msg(user_id=1090693441,
                                   message=f'你好～现在{now.hour}点{now.minute}分啦！现在绵阳的天气是'
                                           f'{msg}')
    except CQHttpError:
        pass
