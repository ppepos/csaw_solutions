with open('eps1.1_ones-and-zer0es_c4368e65e1883044f3917485ec928173.mpeg', 'r') as fd:
    data = fd.read().strip()
    print data
    print 
    print 

    flag = [data[idx:idx+8] for idx in xrange(0, len(data), 8)]
    print flag
    print 
    print 

    flag = [int(chunk, 2) for chunk in flag]
    print flag
    print 
    print 

    flag = [chr(chunk) for chunk in flag]
    print flag
    print 
    print 

    flag = "".join(flag)
    print flag


