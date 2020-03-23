import io
import matplotlib.style as mplstyle
from .gifconfig import *
from .func_input import *
from .gifmaker import *
from .historylog import *
from .preconfig import *

mplstyle.use('fast')

'''
在这里注明一下用到的第三方模块:
numpy,moviepy,matplotlib,imageio...
'''


def get_settings(setting_data: dict):
    """
    setting_data = {'duration': ui_set.duration.text(), 'fps': ui_set.fps.text()}
    setting_data['pic_size'] = ui_set.pic_size.text()
    setting_data['gifname'] = ui_set.gif_name.text()
    setting_data['storage_path'] = ui_set.storage_path.text()
    setting_data['coo_range'] = ui_set.coo_range.text()
    setting_data['m_range'] = ui_set.m_range.text()
    setting_data['keep_track'] = ui_set.keep_track.isChecked()
    setting_data['x_fm'] = ui_set.x_fm.toPlainText()
    setting_data['y_gm'] = ui_set.y_gm.toPlainText()
    """
    detect_text(setting_data, 'duration', setting_data['duration'], '5')  # 必须要传
    detect_text(setting_data, 'fps', setting_data['fps'], '30')  # 必须要传
    detect_text(setting_data, 'pic_size', setting_data['pic_size'], '')
    detect_text(setting_data, 'coo_range', setting_data['coo_range'], '')
    detect_text(setting_data, 'm_range', setting_data['m_range'], '')
    detect_text(setting_data, 'keep_track', setting_data['keep_track'], '')
    detect_text(setting_data, 'bk_color', setting_data['bk_color'], 'white')  # 后续还需要添加text
    detect_text(setting_data, 'precision', setting_data['precision'], '0.01')
    detect_text(setting_data, 'gifname', setting_data['gifname'], 'testgif')
    return setting_data


def main_fun(set_data):
    try:  # 读取本地存储设置
        preconfigdict = read_preconfig()
    except FileNotFoundError or io.UnsupportedOperation or TypeError:
        preconfigdict = write_preconfig_default()
    setdata_got = get_settings(set_data)
    logic2 = setdata_got['keep_track']
    coo_rangelist = data_to_list('coo_range', '-5,5,-5,5', setdata_got)
    pic_sizelist = data_to_list('pic_size', '3,3', setdata_got)
    m_rangelist = data_to_list('m_range', '-5,5', setdata_got)  # 数据预处理
    fig, ax1 = draw_fig(coo_rangelist[0], coo_rangelist[1], coo_rangelist[2], coo_rangelist[3],
                        pic_sizelist[0], pic_sizelist[1], setdata_got.get('bk_color', 'white'))  # 生成图片基本格式
    funclist = getfunctions(setdata_got)  # 接受用户输入的函数
    recvfunlist = funclist[0] + funclist[1]
    update_log_fun(setdata_got, recvfunlist)  # 更新日志
    try:
        t0, tl0 = get_time()  # 开始计时
        funclist[0], funclist[1] = makefunlist(funclist[0], funclist[1], setdata_got)  # 制作每一帧对应的函数表
        make_gif(fig, ax1, funclist, coo_rangelist, m_rangelist, setdata_got, logic2,
                 preconfigdict['copy0'])  # 编译函数表并制作gif
        t1, tl1 = get_time()  # 计时结束
        update_log_time(tl0, tl1)  # 更新日志
    except FileNotFoundError:
        print('file not found\n')
    except:
        update_log_error()  # 在日志中记录错误
        print(traceback.format_exc())
    else:
        return setdata_got['gifname']


if __name__ == '__main__':
    setdata = {'duration': 5, 'fps': 30, 'picsize': '3,3', 'gifname': '009', 'x_fm': 'cos(m)+t\nm+t',
               'y_gm': 'sin(m)-t\nm-t'}
    main_fun(setdata)
