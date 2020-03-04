from typing import Dict, Any, Union

import numpy as np
import matplotlib.pyplot as plt


def draw_fig(xl=-5, xm=5, yl=-5, ym=5, sizex=6, sizey=6,facecolor='white'):
    fig, ax1 = plt.subplots(1, figsize=(sizex, sizey), facecolor=facecolor)
    ax1.set_title("Elevation in y=0")
    ax1.set_ylim(yl, ym)
    ax1.set_xlim(xl, xm)  # x least,x most
    return fig, ax1


def gif_config():
    """Get a config for this gif.

    It is a config,including name,fps,duration,the length of the picture and sth about math.
    """
    xl, xm, yl, ym = -5, 5, -5, 5  # 预设值
    xlfw, xmfw = xl, xm
    sizex, sizey = 6, 6
    jd = 0.01
    # gif基本属性设置
    gifname = input('输入gif名称:') + '.gif'
    print('输入fps值:')
    fps = int(input())
    print('输入持续时间(s):')
    duration = float(input())
    # 独立设置
    logic1 = input('输入y进行高级设置,否则继续')
    logic2 = 0
    if logic1 == 'y':
        lixy = ((input('设置图像框坐标取值范围(xl, xm, yl, ym),m的取值区间(xlfw,xmfw),图像像素大小(1 size = 100px)(sizex,sizey),用空格分割')).split())
        xl, xm, yl, ym, xlfw, xmfw, sizex, sizey = float(lixy[0]), float(lixy[1]), float(lixy[2]), float(lixy[3]), float(
            lixy[4]), float(lixy[5]), float(lixy[6]), float(lixy[7])
        logic2 = input('输入y以使得函数运动时覆盖的区域留下痕迹,输入y0来使用列表绘制多个方程,列表参量为m0,函数应传入xt和yt')
        jd = float(input('设置函数精度'))
        m = np.arange(xlfw, xmfw, jd)
    else:
        m = np.arange(xlfw, xmfw, jd)  # m在这里预定义
    configdict: Dict[Union[str, Any], Union[Union[str, int, float], Any]] = {'gifname': gifname,  # 这里是需要传出的参数表
                                                                             'fps': fps,
                                                                             'duration': duration,
                                                                             'logic2': logic2,
                                                                             'xl': xl,
                                                                             'xm': xm,
                                                                             'yl': yl,
                                                                             'ym': ym,
                                                                             'xlfw': xlfw,
                                                                             'xmfw': xmfw,
                                                                             'jd': jd,
                                                                             'm': m,
                                                                             'sizex': sizex,
                                                                             'sizey': sizey
                                                                             }
    return configdict
