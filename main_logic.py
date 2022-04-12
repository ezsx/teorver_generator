import random

res = {}
v = {}
contents = ''
with open('C:/Users/scdco/PycharmProjects/gen3/tasks/t1_v4.txt', encoding='utf-8') as f:
    contents = f.read()
tsk = contents.split('&&&')
# 1)что компилируем 2)как называем 3)в каком "моде" компилим
x = compile(tsk[2], 'test', 'exec')
exec(x)
f_res=str(tsk[1].format(**v)+"\n"+"Ответ: " + str(res['tsk']))
print(f_res)
