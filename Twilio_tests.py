from twilio.rest import TwilioRestClient
account_sid = "AC2527e5cd9318823eeae67082fc8f0cfb"
auth_token = "1756bdc8319de713187a53a552e3b2a6"
client = TwilioRestClient(account_sid, auth_token)
import datetime
day = datetime.date.today()
time = datetime.datetime.now()
print time
strtime = str(time)
strtime = strtime[:11] + str(int(strtime[12])+5) + strtime[13:]
texted = True
while texted:
    time = datetime.datetime.now()
    if str(time)[:16] == "2015-05-15 14:41":
        print 'hi'
        if texted:
            texted = False    
            break