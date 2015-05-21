import datetime
tin = True
while tin:
    rn = datetime.datetime.now()
    if str(rn)[:16] == "2015-05-15 14:17":
        print str(datetime.datetime.now())
        break
    else: 
        print 'hi'