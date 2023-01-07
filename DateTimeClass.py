import datetime

def getAgora():
    agora = str(datetime.datetime.now())
    agora = agora[0:-7]
    agora = agora.replace(":","_")
    return agora