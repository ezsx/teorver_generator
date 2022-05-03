# test case
# 1-16
# 1, 2, 3, 4, 5
# 1-2,3
def F(str):
    if str=='':
        return [x for x in range(1,17)]
    str = str.replace(' ', '')  # "1-5,6"
    arr_str = str.split(',')    # ['1-5', '6']
    arr_res = []

    for id in arr_str:
        if '-' in id:
            arr_res += [x for x in range(int((id.split('-'))[0]), int((id.split('-'))[1])+1)]
        else:
            arr_res += [int(id)]
    return arr_res