from nonebot import on_command, CommandSession
from botcode.plugins.fun_pic.main import *
import subprocess

subprocess.run('python .\__init__.py')


@on_command('fun_pic', aliases=('函数', '画函数', '画函数动图'))
async def fun_pic(session: CommandSession):
    func_x = session.get('func_x', prompt='输入函数x=f(m),输入f结束')


@fun_pic.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['func_x'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('函数不能为空')

    session.state[session.current_key] = stripped_arg
