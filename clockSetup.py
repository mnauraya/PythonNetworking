from datetime import datetime#import the datetime module
class ClockSetup():
  def __showClock__(self, connectHandle):
      self.connection = connectHandle
      currentClock = self.connection.send_command('show clock')
      print currentClock


  def __setClock__(self, connectHandle):
      connection = connectHandle
      utcLinuxTime = str((datetime.utcnow()))
      timeDateList = utcLinuxTime.split(" ")#Used to separate date and time
      dateList=timeDateList[0].split("-")#separates years months and days
      timeList=timeDateList[1].split(":")#separates hours minutes and seconds
      year= dateList[0]
      monthNum = dateList[1]
      day = dateList[2]
      hour = timeList[0]
      minute = timeList[1]
      seconds = timeList[2]
      noDecimalSecond = seconds.split(".")
      finalSecond= noDecimalSecond[0]
      monthNames = {'01':'January',#Equivalent of a switch statement to correlate month number with a name
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
