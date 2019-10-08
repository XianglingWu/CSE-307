import datetime


def getNumDays(month,year):
    numDays = {1:31,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30}
    if month!=2:
        return numDays[month]
    else:
        if year%400==0:
            return 29
        elif year%100==0:
            return 28
        elif year%4==0:
            return 29
        else:
            return 28

def validDate(day,month,year):
    return day>=1 and month>=1 and month<=12 and year>=0 and day<=getNumDays(month,year)


if __name__ == "__main__":
    dateStr = input()
    dateStr = dateStr.split('/')
    if len(dateStr)==3:
        if dateStr[0].isdigit() and len(dateStr[0])==2 and dateStr[1].isdigit() and len(dateStr[1])==2 and dateStr[2].isdigit():
            month = int(dateStr[0])
            day = int(dateStr[1])
            year = int(dateStr[2])
            if validDate(day,month,year):
                #take strings and parse into datetime
                date = datetime.datetime(year,month,day)
                weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
                monthList = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                weekday = weekDays[date.weekday()]
                print(weekday+', '+monthList[month-1]+' '+str(day)+', '+str(year))
            else:
                print(None)
        else:
            print(None)
    else:
        print(None)