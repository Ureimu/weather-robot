import matplotlib.pyplot as plt


def draw_fig(xl=-5, xm=5, yl=-5, ym=5, sizex=6, sizey=6,facecolor='white'):
    fig, ax1 = plt.subplots(1, figsize=(sizex, sizey), facecolor=facecolor)
    ax1.set_title("Elevation in y=0")
    ax1.set_ylim(yl, ym)
    ax1.set_xlim(xl, xm)  # x least,x most
    return fig, ax1



