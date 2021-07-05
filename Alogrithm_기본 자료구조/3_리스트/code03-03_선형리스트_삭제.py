katok = ['다현','정연','쯔위','사나','지효']

def delete_Data(position):
    klen = len(katok)
    katok[position] = None

    for i in range(position+1, klen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])

delete_Data(1)
print(katok)
delete_Data(3)
print(katok)
