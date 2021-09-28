import datetime
import requests
import time
from plyer import notification
import os
import win32gui, win32con


hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)
#plyer.platforms.win.notification

#functions

#reload
def delayed():
    with open("files/delay.txt",'r') as delay:
        for i in delay:
            return int(eval(i))

#timer
def timer(delay):
    i = 0
    j=0
    while (i< delay/2):
        i+=1
        j+=2
        os.system('cls')#clear console
        print(j,'seconds')
        time.sleep(2) #twice the condition hence time not change
        try:
            delay = delayed()
        except Exception:
            pass        

#read previous date
def readPreviousDate():
    with open("files/previousDate.txt",'r') as previousDate:
        for i in previousDate:
            return int(i)

#get date
def getDate():
    return datetime.date.today()-datetime.timedelta(days=readPreviousDate())

def printHash():
    print("#################################################")
    time.sleep(1)


def modifiedFunction(names,urls):
    printHash()
    modifiedList = []
    for i in range(len(urls)):
        try:
            r = requests.get(urls[i], stream=True)
            r.headers['Last-Modified']
            print(names[i], "Modified", r.headers['Last-Modified'])
            modifiedList.append(i)
        except Exception:
            print(names[i], "Not modified")

    time.sleep(1)
    return modifiedList

def savingModifiedFiles(names,urls):

    modifiedList = modifiedFunction(names,urls)
    printHash()
    
    for i in modifiedList:

        r = requests.get(urls[i], allow_redirects=True)
        link = urls[i]
        extension = link[len(link)-4:len(link)]

        open("files/"+names[i] + extension, 'wb').write(r.content)
        print(names[i], "Saved")

    time.sleep(1)

    return modifiedList

def notifier(title,message):
    notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)

def notifyModified(names,urls,modifiedList):
    printHash()
    
    title = 'Modified files'
    message= ''
    

    for i in modifiedList:

        r = requests.get(urls[i], stream=True)
        message += names[i] +" "
            
        date = r.headers['Last-Modified']
        message += date[5:17]
            
        message += '\n'


    if (len(message)==0):
        message = "no Files are changed"
    else:
        print(message)
        messageList = message.split("\n")

        j=0
        for i in range(len(messageList)):
            if i%4!=0 or i==0:
                message1 = "\n".join(messageList[j:i+1])
            else:
                j += 4
                notifier(title,message1)
        notifier(title,message1)

    time.sleep(1)




#main method
def main():


    names = ["Local Cotton",
            "GOPIS Prices",
            "PIB-FRR Prices",
            "PIB Trade Data",
            "TFC Prices",
            "SBP Customer Rates",
            "SBP Reval Rates",
            "SBP FE25 Rates",
            "W.Avg.Repo Rate"
            ]


    while (True):
        try:
            month = "{:%B}".format(getDate())
            month = month[:4]
            urls=['http://www.kcapk.com/Docs/DMR dated {:%d.%m.%Y}.pdf'.format(getDate()),
                'https://mufap.com.pk/pdf/PKISRVs/{:%Y}/{}/PKISRV{:%d%m%Y}.csv'.format(getDate(),month,getDate()),
                'https://mufap.com.pk/pdf/PKFRVs/{:%Y}/{}/PKFRV{:%d%m%Y}.csv'.format(getDate(),month,getDate()),
                'https://www.sbp.org.pk/ecodata/EBND.pdf',
                'https://mufap.com.pk/pdf/PricesDebtSecurities/{:%Y}/{}/v{:%d%m%Y}.pdf'.format(getDate(),month,getDate()),
                'https://www.sbp.org.pk/ecodata/rates/war/{:%Y}/{:%b}/{:%d-%b-%Y}.pdf'.format(getDate(),getDate(),getDate()),
                'https://www.sbp.org.pk/ecodata/rates/m2m/{:%Y}/{:%b}/{:%d-%b-%y}.pdf'.format(getDate(),getDate(),getDate()),
                'https://www.sbp.org.pk/ecodata/crates/{:%Y}/{:%b}/{:%d-%b-%y}.pdf'.format(getDate(),getDate(),getDate()),
                'https://www.sbp.org.pk/ecodata/OvernightsRepoRates2.pdf']
            modifiedList = savingModifiedFiles(names,urls)
            notifyModified(names,urls,modifiedList)
            timer(delayed())
        except Exception:
            pass

main()
