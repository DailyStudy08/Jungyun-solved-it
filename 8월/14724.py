n=input()
dongari=['PROBRAIN','GROW','ARGOS','ADMIN','ANT','MOTION','SPG','COMON','ALMIGHTY']
dongarimax=[]
for i in range(9):
    dongarimax.append (max( list(map(int, input().split()))))
checkmax=max(dongarimax)
for i in range(9):
    if checkmax ==dongarimax[i]: print (dongari[i]); break