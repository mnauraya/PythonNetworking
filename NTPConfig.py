##Methods that Setup and Verify Network Time Protocol

class NTP():

  def __setNTPMaster__(self, connectHandle):
      connection = connectHandle
      print 'Enter your desired stratum-level'
      stratumLevel= str(raw_input())
      output = connection.send_config_set("ntp master "+ stratumLevel)
      print output


  def __setNTPServer__(self, connectHandle):
      connection = connectHandle
      print 'Enter the ip address of your NTP Master'
      ntpServer = str(raw_input())
      output = connection.send_config_set("ntp server "+ntpServer)
      print output

  def __showNTPStatus__(self, connectHandle):
      connection = connectHandle
      output=connection.send_command("Show ntp status")
      print output
      #ntpStatList= output.split(",")
      #ntpSyncCheckOne= ntpStatList[0]
      #ntpSyncCheckOneList= ntpSyncCheckOne.split(" ")
      #ntpSyncCheckFinal= ntpSyncCheckOneList[2]
      #print ntpSyncCheckFinal
      #Future for loop to check for Synchronization using if statement comparisons

  def __showNTPAssociations__(self, connectHandle):
      connection = connectHandle
      output=connection.send_command("Show ntp associations")
      print output

  def wait_minute(self):
      import time
      time.sleep(120)
