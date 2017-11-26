##
##目前使用的格里曆閏年規則如下：
##    西元年份除以4不可整除，為平年。
##    西元年份除以4可整除，且除以100不可整除，為閏年。
##    西元年份除以100可整除，且除以400不可整除，為平年
##    西元年份除以400可整除，為閏年。

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def leapyear(year):
    if (( year % 400 == 0) or (( year % 4 ==0) and (year % 100 !=0))):
        ##print('{} is leap year!'.format(year))
        ##print('yes')
        return 1
    else:
        ##print('no')
        return 0

a=0

##while (a != 'bye'):
##    a = input('input a year>>')
##    leapyear(int(a))
    
y = np.array(range(1900,2018))
##print(y)

yyy=[]
for yy in y:
    yyy.append([yy,leapyear(yy)])
print(yyy)
