import time
import traceback

def update_log_fun(dict, func):
    print('update log...')
    file = open('historylog.txt', 'a+')
    file.write(str(dict)+'\n')
    file.write(str(func)+'\n')
    file.close()
    print('finish')


def update_log_time(t0, t1):
    file = open('historylog.txt', 'a+')
    file.write('The progess begins at '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0)))
    file.write(',ends at '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1))+'.\n')
    file.write('It takes %s s to finish' % (t1-t0)+'.\n\n')
    file.close()


def get_time():
    return time.clock(), time.time()


def update_log_error():
    file = open('historylog.txt', 'a+')
    file.write(traceback.format_exc()+'\n\n')
    file.close
