from nonebot import on_command, CommandSession
from nonebot.session import BaseSession
from .main import main_fun
from .movefile import mymovefile


def get_id(session: CommandSession):
    user_id = session.event['user_id']
    print(user_id)
    print(dir(session))
    file = open(f'logging/{user_id}_log.txt', 'a+')
    file.write(f'id:{user_id}'+'\n')
    file.close()
    print('finish')


@on_command('fun_pic', aliases=('函数', '画函数', '画函数动图'))
async def fun_pic(session: CommandSession):
    get_id(session)
    
    func_dict = {'x_fm': session.get('x_fm', prompt='输入函数x=f(m),输入f结束'),
                 'y_gm': session.get('y_gm', prompt='输入函数y=g(m),输入f结束'),
                 'gifname': session.get('gifname', prompt='请输入图像名称')}
    # 子进程制作函数图像
    func_pict = await make_progress(func_dict)
    # 向用户发送图像
    await session.send(func_pict)


@fun_pic.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            arg_list = stripped_arg.split('.')
            session.state['x_fm'] = arg_list[0]
            session.state['y_gm'] = arg_list[1]
            session.state['gifname'] = arg_list[2]
        return
    if not stripped_arg:
        session.pause('函数不能为空')
    session.state[session.current_key] = stripped_arg


# 启动子进程,绘制图像,并返回相应的CQ码
async def make_progress(make_func_dict: dict) -> str:
    setdata = {'duration': 5, 'fps': 30, 'pic_size': '2,2', 'gifname': 'testgif',
               'coo_range': '-5,5,-5,5','m_range':'-5,5', 'keep_track': 'n',
               'bk_color': 'white', 'precision': 0.01}
    print(make_func_dict)
    setdata.update(make_func_dict)
    print(setdata)
    main_fun(setdata)
    gifname = setdata['gifname']
    return '[CQ:image,file=funpic/' + gifname + '.gif]'
