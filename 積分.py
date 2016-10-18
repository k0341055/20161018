# -*- coding: utf-8 -*-
import numpy as np
dx = float(input('Please input dx'))
area=0
y=0
for x in np.arange(2,5,dx):
    y=x*x+1
    area=area+y*dx
print('area = ',area)    