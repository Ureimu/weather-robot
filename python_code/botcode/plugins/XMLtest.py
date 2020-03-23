from nonebot import on_command, CommandSession
import handle_json.handle_weather_json


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」


@on_command('XML', aliases=('新冠'))
async def weather(session: CommandSession):
    await session.send(
        '{"app":"com.tencent.miniapp","desc":"","view":"notification","ver":"0.0.0.1","prompt":"[应用]","appID":"","sourceName":"","actionData":"","actionData_A":"","sourceUrl":"","meta":{"notification":{"appInfo":{"appName":"全国疫情数据统计","appType":4,"appid":1109659848,"iconUrl":"http:\\/\\/gchat.qpic.cn\\/gchatpic_new\\/719328335\\/-2010394141-6383A777BEB79B70B31CE250142D740F\\/0"},"data":[{"title":"确诊","value":"80932"},{"title":"今日确诊","value":"28"},{"title":"疑似","value":"72"},{"title":"今日疑似","value":"5"},{"title":"治愈","value":"60197"},{"title":"今日治愈","value":"1513"},{"title":"死亡","value":"3140"},{"title":"今**亡","value":"17"}],"title":"中国加油，武汉加油","button":[{"name":"病毒：SARS-CoV-2，其导致疾病命名 COVID-19","action":""},{"name":"传染源：新冠肺炎的患者。无症状感染者也可能成为传染源。","action":""}],"emphasis_keyword":""}},"text":"","sourceAd":""}')

