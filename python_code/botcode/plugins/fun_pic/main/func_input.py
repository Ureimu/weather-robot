def getfunctions():
    list0 = []
    xfunlist = []
    yfunlist = []
    paralist = []
    while True:
        xfuninput = input('输入函数x=f(m),输入f结束:')
        print()
        if xfuninput == 'f':
            break
        else:
            xfunction = xfuninput
            print(xfunction)
            xfunlist.append(xfunction)
    print(xfunlist)
    xlenfunlist = len(xfunlist)

    while True:
        yfuninput = input('输入函数y=g(m),输入f结束:')
        print()
        if yfuninput == 'f':
            break
        else:
            yfunction = yfuninput
            print(yfunction)
            yfunlist.append(yfunction)
    print(yfunlist)
    ylenfunlist = len(yfunlist)
    # 输入参变量
    while True:
        parainput = input('输入参变量,输入f结束:')
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
    gifname, fps, duration = configdict['gifname'], configdict['fps'], configdict['duration']
    # 准备funlist
    xfunlist = xfunlist * int(fps * duration+1)
    yfunlist = yfunlist * int(fps * duration+1)
    return xfunlist, yfunlist
