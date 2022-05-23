a='happier'
def most_frequent(a):
    d= dict()
    for b in a:
        if b not in d:
            d[b] = 1
        else:
             d[b] += 1
    print(d)
most_frequent(a)    



