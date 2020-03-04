
def read_preconfig():  # 读取用户的preconfig文件
    file = open('preconfig.txt', 'r')
    copylist = []
    copy0 = file.readline()
    copylist = copy0.split('\n')
    print(copy0)
    facecolor = file.readline()
    if facecolor == '':
        return 0
    print(copy0,facecolor)
    file.close()
    preconfigdict = {'copy0':copylist[0],'facecolor':facecolor}
    return preconfigdict


def write_preconfig_default():   # 创建一个默认的preconfig文件
    file = open('preconfig.txt','x')
    file.write('pic/\n')
    copy0 = 'pic/'
    file.write('white')
    facecolor = 'white'
    print(copy0,facecolor)
    file.close()
    preconfigdict = {'copy0':copy0,'facecolor':facecolor}
    return preconfigdict
