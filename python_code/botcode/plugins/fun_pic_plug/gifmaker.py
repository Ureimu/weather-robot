from moviepy.video.io.bindings import mplfig_to_npimage
from PIL import Image
import matplotlib.pyplot as plt
import imageio
import numpy as np
from .movefile import mymovefile
# 引进一些常用np数学函数以简化输入,勿删
from numpy import sin
from numpy import cos
from numpy import tan
from numpy import pi
from numpy import arcsin
from numpy import arccos
from numpy import arctan
from numpy import around  # 取整函数
from numpy import floor  # 向下取整
from numpy import ceil  # 向上取整
from numpy import exp  # 以e为底的指数函数
from numpy import log as ln  # 自然对数函数


def create_gif(image_list, gif_name, duration=1.0):
    '''
    :param image_list: 这个列表用于存放生成动图的图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param duration: 图像间隔时间
    :return:
    '''
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def make_gif(fig, ax1, list0, coo_rangelist, m_rangelist, setdata: dict, logic2, path: str):
    xfunlist, yfunlist, lenfunlist, paralistall = list0[0], list0[1], list0[2], list0[3]
    m = np.arange(m_rangelist[0], m_rangelist[1], float(setdata['precision']))
    xl, xm, yl, ym = coo_rangelist[0], coo_rangelist[1], coo_rangelist[2], coo_rangelist[3]
    gifname, fps, duration = setdata['gifname'], float(setdata['fps']), float(setdata['duration'])
    xt, yt, datax, datay = 0, 0, [], []
    pic_list, t_list = [], []
    if logic2 == 'y':
        # 用MoviePy制作动画（为每个t更新曲面）。制作一个GIF,保留函数轨迹(速度较快)
        def make_frame_mpl(t):
            exec(compile(paralistall, '', 'exec'))
            for m0 in range(lenfunlist):
                m = np.arange(m_rangelist[0], m_rangelist[1], float(setdata['precision']))  # don't change,or bugs
                xt = eval(xfunlist[int(fps * t * lenfunlist + m0)])
                yt = eval(yfunlist[int(fps * t * lenfunlist + m0)])
                datax.append(xt)
                datay.append(yt)
                line, = ax1.plot(datax[int(fps * t * lenfunlist + m0)], datay[int(fps * t * lenfunlist + m0)],
                                 color='tab:red')
            print(int(fps * t))
            return mplfig_to_npimage(fig)  # 图形的RGB图像
    elif logic2 == 'y0':
        # 用MoviePy制作动画（为每个t更新曲面）。制作一个GIF.支持打表式绘制图像.
        line = []
        for i in range(lenfunlist):
            line.append(ax1.plot(m, m * 0 - xl * 1000, color='tab:red'))
            # 不要去掉line后面的逗号,会报错
            line[i], = ax1.plot(m, m * 0 - xl, color='tab:red')

        def make_frame_mpl(t):
            exec(compile(paralistall, '', 'exec'))
            for m0 in range(lenfunlist):
                m = np.arange(m_rangelist[0], m_rangelist[1], float(setdata['precision']))
                eval(xfunlist[int(fps * t * lenfunlist + m0)])
                eval(yfunlist[int(fps * t * lenfunlist + m0)])
                datax.append(xt)
                datay.append(yt)
                line[m0].set_xdata(datax[int(fps * t * lenfunlist + m0)])
                line[m0].set_ydata(
                    datay[int(fps * t * lenfunlist + m0)])  # 更新曲面
                NUM = int(t * 1000)
                plt.title(f'{NUM} ms')
            print()
            return mplfig_to_npimage(fig)  # 图形的RGB图像
    else:
        # 用MoviePy制作动画（为每个t更新曲面）。制作一个GIF.
        line = []
        for i in range(lenfunlist):
            line.append(ax1.plot(m, m * 0 - xl, color='tab:red'))
            # 不要去掉line后面的逗号,会报错
            line[i], = ax1.plot(m, m * 0 - xl, color='tab:red')

        def make_frame_mpl(t):
            m = np.arange(m_rangelist[0], m_rangelist[1], float(setdata['precision']))
            exec(compile(paralistall, '', 'exec'))
            for m0 in range(lenfunlist):
                xt = eval(xfunlist[int(fps * t * lenfunlist + m0)])
                yt = eval(yfunlist[int(fps * t * lenfunlist + m0)])
                datax.append(xt)
                datay.append(yt)
                line[m0].set_xdata(datax[int(fps * t * lenfunlist + m0)])
                line[m0].set_ydata(datay[int(fps * t * lenfunlist + m0)])  # 更新曲面
                NUM = int(t * 1000)
                plt.title(f"{NUM} ms")
            return mplfig_to_npimage(fig)  # 图形的RGB图像
    for i in range(int(fps * duration)):
        t_list.append(i / fps)
    for t in t_list:
        Image.fromarray(make_frame_mpl(t)).save(str(int(t * fps)) + ".jpeg")
        mymovefile(str(int(t * fps)) + ".jpeg", 'cache_pic/' + str(int(t * fps)) + ".jpeg")
        pic_list.append('cache_pic/' + str(int(t * fps)) + ".jpeg")
        step = int((t * fps) / (duration * fps)) * 100
    create_gif(pic_list, gifname + '.gif', 1 / fps)
    mymovefile(gifname + '.gif', path + gifname + '.gif')


# 定义一些numpy没有的初等函数方便输入
def lnxy(x, y):
    return np.log(y) / np.log(x)


def sec(x):
    return np.reciprocal(cos(x))


def csc(x):
    return np.reciprocal(sin(x))


def cot(x):
    return np.reciprocal(tan(x))


e = exp(1)
