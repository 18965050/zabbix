import sys
from suds.client import Client

def sendsms(to_list,content):
    myClient=Client('http://xxx.abc.com:80/sms/services/MessageTransferWebService')
    for mobile in to_list:
        res=myClient.service.sendMessageX('xyz','XuBm9sdC',mobile,'sms/mt',None,content,None,'999','20161125114000',None)
        print(res)

if __name__=='__main__':
    #sendsms(sys.argv[1],sys.argv[2])
    sendsms(['13811111111'],'hello world')