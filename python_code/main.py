import nonebot
import config
from os import path

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(path.join(path.dirname(__file__), 'botcode', 'plugins'),
    'botcode.plugins'
    )
    nonebot.run()
