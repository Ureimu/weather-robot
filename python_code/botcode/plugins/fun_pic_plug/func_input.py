def func_to_list(text,default,data):
    '''
    给定字典data和需要的key名text,从字典获取对应的值,如果没有,则使用default作为值.
    :param text: 键
    :param default: 作为键的默认值
    :param data: 字典
    :return: 用spilt切好的表(用逗号隔开)
    '''
    get_data = data.get(text,default)
    data_list = get_data.split('\n')
    return data_list


def getfunctions(setdata):
    x_fm_list=func_to_list('x_fm','',setdata)
    y_gm_list=func_to_list('y_gm','',setdata)
    list0 = []
    xfunlist = []
    yfunlist = []
    paralist = []
    for x_fm in x_fm_list:
        xfuninput = x_fm
        if xfuninput == '':
            break
        else:
            xfunction = xfuninput
            xfunlist.append(xfunction)
    xlenfunlist = len(xfunlist)

    for y_gm in y_gm_list:
        yfuninput = y_gm
        if yfuninput == '':
            break
        else:
            yfunction = yfuninput
            yfunlist.append(yfunction)
    ylenfunlist = len(yfunlist)
    # 输入参变量
    for i in range(1):  # 该功能暂时弃用
        parainput = 'f'
        print()
        if parainput == 'f':
            break
        else:
            parameter = parainput
            print(parameter)
            paralist.append(parameter)
    paralistall = ''
    for i in range(len(paralist)):
        paralistall += paralist[i] + '\n'
    if xlenfunlist != ylenfunlist:
        print('the number of the function f(m) and g(m) is not equal')
        return 0
    else:
        lenfunlist = xlenfunlist
        list0.append(xfunlist)
        list0.append(yfunlist)
        list0.append(lenfunlist)
        list0.append(paralistall)
        return list0


def makefunlist(xfunlist, yfunlist, configdict):
    gifname, fps, duration = configdict['gifname'], int(configdict['fps']), float(configdict['duration'])
    # 准备funlist
    xfunlist = xfunlist * int(fps * duration+1)
    yfunlist = yfunlist * int(fps * duration+1)
    return xfunlist, yfunlist
