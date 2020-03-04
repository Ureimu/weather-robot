from moviepy.video.io.bindings import mplfig_to_npimage
import matplotlib.pyplot as plt
import moviepy.editor as mpy
import numpy as np
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


def make_gif(fig, ax1, list0, configdict):
    xfunlist, yfunlist, lenfunlist, paralistall = list0[0], list0[1], list0[2], list0[3]
    m = configdict['m']
    xl, xm, yl, ym = configdict['xl'], configdict['xm'], configdict['yl'], configdict['ym']
    gifname, fps, duration = configdict['gifname'], configdict['fps'], configdict['duration']
    logic2 = configdict['logic2']
    xt, yt, datax, datay = 0, 0, [], []
    if logic2 == 'y':
        # 用MoviePy制作动画（为每个t更新曲面）。制作一个GIF,保留函数轨迹(速度较快)
        def make_frame_mpl(t):
            exec(compile(paralistall, '', 'exec'))
            for m0 in range(lenfunlist):
                m = configdict['m']  # don't change,or bugs
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
        NUM = 0

        def make_frame_mpl(t):
            exec(compile(paralistall, '', 'exec'))
            for m0 in range(lenfunlist):
                m = configdict['m']
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
        NUM = 0

        def make_frame_mpl(t):
            m = configdict['m']
            exec(compile(paralistall, '', 'exec'))
            for m0 in range(lenfunlist):
                xt = eval(xfunlist[int(fps * t * lenfunlist + m0)])
                yt = eval(yfunlist[int(fps * t * lenfunlist + m0)])
                datax.append(xt)
                datay.append(yt)
                line[m0].set_xdata(datax[int(fps * t * lenfunlist + m0)])
                line[m0].set_ydata(
                    datay[int(fps * t * lenfunlist + m0)])  # 更新曲面
                NUM = int(t * 1000)
                plt.title(f"{NUM} ms")
            print()
            return mplfig_to_npimage(fig)  # 图形的RGB图像
    animation = mpy.VideoClip(make_frame_mpl, duration=duration)
    animation.write_gif(gifname, fps=fps)  # 将一系列图片制作成gif

# 定义一些numpy没有的初等函数方便输入


def lnxy(x, y):
    return np.log(y)/np.log(x)


def sec(x):
    return np.reciprocal(cos(x))


def csc(x):
    return np.reciprocal(sin(x))


def cot(x):
    return np.reciprocal(tan(x))


e = exp(1)
