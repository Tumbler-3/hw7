def binary(val, list_bin: list):
    N = len(list_bin)
    resultOk = False
    first = 0 
    last = N - 1
    pos = ''

    while first < last:
        middle = (first+last)//2

        if val == list_bin[middle]:
            resultOk = True
            pos = middle
            first = middle
            last = first
        elif val > list_bin[middle]:
            first = middle + 1
        else:
            last = middle - 1
    
    if resultOk == True:
        return pos
    else:
        return f'элемент не найден'

a = 6
l = list(range(1, 96))
print(binary(a, l))

def bubble(lst: list):
    N = len(lst) - 1
    x = 0
    y = -1
    while x != N:
        try:
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]
                x += 1
            else:
                x += 1
            if lst[x] == lst[y]:
                x = 0 
                y -= 1
        except:
            break
    return print(lst)

k = [1, 2, 4, 7, 2, 76, 3, 5, 1, 8, 1, 2, 5, 8, 6]

bubble(k)