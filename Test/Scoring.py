import sqlite3
def score(r):
    L = []
    for tpl in r :
        L.append([tpl,tpl[3]-tpl[4]])

    for i in range(len(L)):
        j=i
        atrie = L[i]

        while (j>0 and atrie[1]>L[j-1][1]) :
            L[j] = L[j-1]
            j = j - 1
        L[j] = atrie
    rinf =[]
    for i in L:
        rinf.append(i[0])

    return rinf

