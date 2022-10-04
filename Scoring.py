import sqlite3
def score(r):
    L = []
    for tpl in r : # Pour chaque idée
        L.append([tpl,tpl[3]-tpl[4]]) # Nous mettons dans la liste une sous liste contenant les informations de l'idée et son score de popularité

    for i in range(len(L)): #tri par insertion dans l'odre du score de popularité décroissant de la liste
        j=i
        atrie = L[i]

        while (j>0 and atrie[1]>L[j-1][1]) :
            L[j] = L[j-1]
            j = j - 1
        L[j] = atrie


    rinf =[]
    for i in L: # Creation de la liste avec uniquement les informations des idées triées
        rinf.append(i[0])

    return rinf

