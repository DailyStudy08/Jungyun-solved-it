while True:
    n = int(input())
    # pseudo random number
    prn = []
    prn.append(n)
    #FUCK this shit made me to spend 30min in midnight
    if n == 0:
        break
    else:
        done = 0
        while True:
            #check last of prn
            new = prn[-1] * prn[-1]
            #convert it into single list for easy slicing and indexing
            news = list(str(new))
            #print(news)
            #adding 0 to news when it's lenth is shorter than 8
            while len(news) < 8:
                news.insert(0, '0')
                #slice the required 4 numbers in mid range 
                tada = news[2:6]
                #print(tada)
            else:
                tada = news[2:6]
                #print(tada)
            #make it in to integer again
            done = int(''.join(tada))
            #print(done)
            #print(prn)
            #check if done is in prn
            #yes : print answer and break
            if done in prn:
                print(len(prn))
                break
            else:
                prn.append(done)