def GetI020():
 Data =  open('i020.TXFA8').readlines()
 Data1 = [ i.strip('\n').split(',') for i in Data ]
 return Data1

def GetI030():
 Data =  open('i030.TXFA8').readlines()
 Data1 = [ i.strip('\n').split(',') for i in Data ][1:]
 return Data1