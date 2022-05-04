import random
import itertools
import math
res = {}
v = {}

def F(task, variant, answer):
    contents = ''
    with open('C:/Users/scdco/PycharmProjects/gen3/tasks/' + str(task) + '_' + str(variant) + '.txt',
              encoding='utf-8') as f:
        contents = f.read()
    tsk = contents.split('&&&')
    exec(compile(tsk[2], 'test', 'exec')) # 1) что компилируем 2) как называем 3) в каком "моде" компилим
    if answer:
        return str("    Задание: " + str(tsk[1]) + tsk[1].format(**v) + "Ответ: " + str(res['tsk']))
    else:
        return str(str("    Задание " + str(tsk[0]) + ": ") + "\r"+tsk[1].format(**v)).replace("\n",""), str(res['tsk'])
