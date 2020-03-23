
def read_preconfig():  # 读取用户的preconfig文件
    file = open('preconfig.txt', 'r')
    copylist = []
    copy0 = file.readline()
    copylist = copy0.split('\n')
    facecolor = file.readline()
    if facecolor == '':
        return {}
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

def data_to_list(text,default,data):
    '''
    给定字典data和需要的key名text,从字典获取对应的值,如果没有,则使用default作为值.
    :param text: 键
    :param default: 作为键的默认值
    :param data: 字典
    :return: 用split切好的表(用逗号隔开)
    '''
    datam_list = []
    if data[text] == '':
        get_data = default
    else:
        get_data = data.get(text,default)
    data_list = get_data.split(',')
    for i in data_list:
        datam_list.append(float(i))
    return datam_list

def detect_text(data,dataname,text,default):
    '''
    get text for data,if it is '',return a default text
    :return:
    '''
    if text != '':
        try:
            data[dataname] = text
        except KeyError: # text不存在
            data[dataname] = default
    else:
        data[dataname] = default
    return data[dataname]
