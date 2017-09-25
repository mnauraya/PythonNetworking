#import datetime
from datetime import datetime

def __setClock__():
    utcLinuxTime = str((datetime.utcnow()))
    timeDateList = utcLinuxTime.split(" ")
    print timeDateList
    dateList=timeDateList[0].split("-")
    timeList=timeDateList[1].split(":")
    print dateList
    year= dateList[0]
    monthNum = dateList[1]
    day = dateList[2]
    hour = timeList[0]
    minute = timeList[1]
    seconds = timeList[2]
    noDecimalSecond = seconds.split(".")
    finalSecond= noDecimalSecond[0]
    monthNames = {'01':'January',
                  '02':'February',
                  '03':'March',
                  '04':'April',
                  '05':'May',
                  '06':'June',
                  '07':'July',
                  '08':'August',
                  '09':'September',
                  '10':'October',
                  '11':'November',
                  '12':'December',
        }
    return ('clock set '+hour+':'+minute+':'+finalSecond+' '+day+' '+monthNames[monthNum]+' '+year)


output =__setClock__()
print output
