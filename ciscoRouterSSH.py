from sys import argv#Allows us to place outside arguments into the program
from netmiko import ConnectHandler#Imports the netmiko libraries
import json#import library to potentially read json files
import csv#import library to read csv files
from clockSetup import ClockSetup #import the datetime module
from saveConfig import saveConfig
from NTPConfig import NTP
script, filename = argv #takes in the scripts name and a filename

clockSetup = ClockSetup()
saveConnect = saveConfig()
NTP = NTP()




routerInfoFile = open(filename)#Opens the text file
fileReader = csv.reader(routerInfoFile)#Reads the text file into a variable
fileData = list(fileReader)#Places the text file into a list row by row
routerInfoFile.close()#closes the text file

print "Here's your configuration file %r:" % filename #prints the filename
def __getConfigInfo__(fileData):#Takes in the list file into the method
    deviceNum = {}#Initiates device dictionary
    ipAdd = {}#Initiates ip address dictionary
    device = {}#Initiates device type dictionary
    usrName = {}#Initiates username dictionary
    passWord = {}#Initiates password dictionary
    secretPW = {}#Initiates enable password dictionary
    k=0#initiates counter for each row
    for i in range(len(fileData)):#goes through each piece of the 2d array and places them into the appropriate list
        for j in range(len(fileData[i])):
            if j==0:
                deviceNum[k]=fileData[i][j]
            elif j==1:
                ipAdd[k]=fileData[i][j]
            elif j==2:
                device[k]=fileData[i][j]
            elif j==3:
                usrName[k]=fileData[i][j]
            elif j==4:
                passWord[k]=fileData[i][j]
            elif j==5:
                secretPW[k] = fileData[i][j]
                str(deviceNum)
                str(ipAdd)
                str(device)
                str(usrName)
                str(passWord)
                str(secretPW)
                k+=1
    return deviceNum, ipAdd, device, usrName, passWord, secretPW#returns the lists

def __DeviceConnect__():#Allows the user to select the device they want to connect to
     print 'Enter in the device number you wish to connect to'
     userDeviceSelect= int(raw_input())
     userDeviceSelect-=1
     str(userDeviceSelect)
     userIp= ipDict.get(userDeviceSelect)#Selects the correct ip from the list
     userDevice= deviceDict.get(userDeviceSelect)
     userUN= usrNameDict.get(userDeviceSelect)
     userPW= passwordDict.get(userDeviceSelect)
     userSecret = secretPWDict.get(userDeviceSelect)
     return userIp, userDevice, userUN, userPW, userSecret

##Start of main application

deviceNumDict, ipDict, deviceDict,usrNameDict, passwordDict, secretPWDict = __getConfigInfo__(fileData)
userFunctSelect=1
while(userFunctSelect!=0):
    print '''Select the function you wish to run on the device,
            1. Connect to a New Device
            2. Disconnect from Device
            3. Show Initial Clock
            4. Set Clock to UTC Format
            5. Configure NTP Master
            6. Configure NTP Client
            7. Verify NTP
            0. Exit Program '''
    userFunctSelect = int(raw_input())
    if userFunctSelect==1:
        userIp, userDevice, userUN, userPW, userSecret = __DeviceConnect__()
        connection = ConnectHandler(ip=userIp, device_type=userDevice, username=userUN, password=userPW, secret=userSecret)
        print "The device with an ip address of %r has been connected" % userIp
        connection.enable()
    elif userFunctSelect==2:
        connection.exit_enable_mode()
        connection.disconnect()
    elif userFunctSelect==3:
        clockSetup.__showClock__(connection)
    elif userFunctSelect==4:
        connection.send_command(clockSetup.__setClock__(connection))
        clockSetup.__showClock__(connection)
    elif userFunctSelect==5:
        NTP.__setNTPMaster__(connection)
        NTP.__showNTPAssociations__(connection)
    elif userFunctSelect==6:
        NTP.__setNTPServer__(connection)
        print "Waiting for NTP to converge"
        NTP.wait_minute()
        NTP.__showNTPStatus__(connection)
    elif userFunctSelect==7:
        NTP.__showNTPStatus__(connection)
    elif userFunctSelect==0:
        saveConnect.__saveConfig__(connection)
        connection.disconnect()
        print 'Thank you Goodbye'
    else:
        print "Enter in a valid option"
