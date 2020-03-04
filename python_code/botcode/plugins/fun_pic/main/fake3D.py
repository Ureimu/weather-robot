
str2 = ''
listfx = []
while True:
    fx = input('put in f(X)')
    if fx != 'f':
        listfx.append(fx)
    else:
        break
logic0 = input('choose one to use:+ x n')
if logic0 == '+':
    m = float(input('i'))
    s = float(input('s'))
    list0 = []
    for i in range(int(m/s)):
        list0.append(s*i)
    for i in list0:
        str2 += '\n'
        for q in listfx:
            if q != listfx[-1]:
                str2 += q + '+%.2f'%(i)
            else:
                str2 += q
    print(str2)
elif logic0 == 'x':
    m = int(input('i'))
    for i in range(m):
        str2 += str1 + '*%d'%(i) + '\n'
        str2 += str1 + '*1/%d'%(i) + '\n'
    print(str2)
elif logic0 == 'n':
    m = int(input('i'))
    for i in range(m):
        str2 += str1+ '\n'
    print(str2)
else:
    end
