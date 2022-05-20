import random
import itertools
import math
from decimal import Decimal, ROUND_FLOOR
import scipy
from scipy import stats
from scipy.special import erf
from exrex import getone
import os
res = {}
v = {}
def F(task, variant):
    contents = ''
    with open(os.path.dirname(__file__)+'\\tasks\\' + str(task) + '_' + str(variant) + '.txt', encoding='utf-8') as f:
        contents = f.read()
    tsk = contents.split('&&&')
    x = exec(compile(tsk[2], 'test', 'exec')) # 1) что компилируем 2) как называем 3) в каком "моде" компилим
    return (str(str("    Задание " + str(tsk[0]) + ": ") + "\r"+tsk[1].format(**v)).replace("\n", "")), (str(res['tsk']))