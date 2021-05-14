llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я', ' ']

def key_dict (key):
    dictt = [0*llst]*len(key)
    count = 0
    for i in key:
        ret = ''
        if i in llst:
            ind = llst.index(i)
            for a in range(ind, len(llst)):
                if a >= len(llst):
                    a = a % len(llst)
                    ret += llst[a]
                else:
                    ret += llst[a]
            dictt[count] = ret 
        count += 1
    return dictt

key = input('input key: ')
print(key_dict(key))
