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
    # 1)что компилируем 2)как называем 3)в каком "моде" компилим
    x = compile(tsk[2], 'test', 'exec')
    exec(x)
    if answer:
        return str("    Задание: " + str(task[1]) + tsk[1].format(**v) + "Ответ: " + str(res['tsk']) + "\n")
    else:
        return str("    Задание: " + str(task[1]) + tsk[1].format(**v) + "\n"), str(res['tsk'])


print(F('t1', 'v5', True))
print(F('t1', 'v5', False)[0])
