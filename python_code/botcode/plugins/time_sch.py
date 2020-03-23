from datetime import datetime
import handle_json.handle_weather_json
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

city = '绵阳'
msg = handle_json.handle_weather_json.get_weather_dict(city)


@nonebot.scheduler.scheduled_job('cron',day='*', hour='7', minute='20')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_private_msg(user_id=1090693441,
                                   message=f'早安～现在{now.hour}点{now.minute}分啦！现在{city}的天气是'
                                           f'{msg["weather"]},最高温度为{msg["max_tep"]}度,最低温度为{msg["min_tep"]}度.')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='22', minute='15')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_private_msg(user_id=1090693441,message=f'晚安～')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='7', minute='10')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_private_msg(user_id=1090693441,message=f'早啊～')
    except CQHttpError:
        pass
