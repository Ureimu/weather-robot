import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([712,653,625,605,617,635,677,762,800,872,947,1025,1111,1218,1309, 500])
y1 = np.array([2022,1876,1710,1544,1347,1309,1025,995,850,723,705,710,761,873,1050, 2000])

x_start = np.min(x1)
x_end = np.max(x1)+1

x_line = x1.copy()
y_line = x_line * 0.9 + 500

y=y1-y_line
nLen=len(x1)
xzero=np.zeros((nLen,))
yzero=np.zeros((nLen,))
for i in range(nLen-1):
    if np.dot(y[i], y[i+1]) == 0:#   %等于0的情况
        if y[i]==0:
            xzero[i]=i
            yzero[i]=0
        if y[i+1] == 0:
            xzero[i+1]=i+1
            yzero[i+1]=0
    elif np.dot(y[i],y[i+1]) < 0:# %一定有交点，用一次插值
        yzero[i] = np.dot(abs(y[i]) * y_line[i+1] + abs(y[i+1])*y_line[i], 1/(abs(y[i+1])+abs(y[i])))
        xzero[i] = (yzero[i]-500)/0.9
    else:
        pass

for i in range(nLen):
    if xzero[i]==0 and (yzero[i]==0):#     %除掉不是交点的部分
        xzero[i]=np.nan
        yzero[i]=np.nan

print(xzero)
print(yzero)

plt.plot(x1, y1, 'o-')
plt.plot(x_line,y_line,xzero,yzero,'o')
plt.show()
