from sys import argv#Allows us to place outside arguments into the program
from clockSetup import ClockSetup #import the datetime module
import json#import library to read json
import netmiko #Imports the netmiko libraries


class FunctionLibrary():

    def __init__(self):
        with open("/home/matt/Documents/PythonNetworking/DeviceLibrary.json", "r") as json_data:#Loads the Device Library
            self.router_info = json.load(json_data)
            json_data.close()

    def get_config_info(self):#Takes in the list file into the method
        self.hostname = self.router_info['router 1']['Hostname']
        self.ipAdd = self.router_info['router 1']['IP Address']
        self.os = self.router_info['router 1']['OS']
        self.username = self.router_info['router 1']['Username']
        self.ln_pass = self.router_info['router 1']['Ln_Pass']
        self.en_pass = self.router_info['router 1']['En_Pass']

    def device_connect(self):#Sets up the device connection
        print self.hostname
        print self.ipAdd
        print self.os
        print self.username
        print self.ln_pass
        print self.en_pass
        self.connection = netmiko.ConnectHandler(ip=self.ipAdd, device_type=self.os, username=self.username,
                                                 password=self.ln_pass, secret=self.en_pass)
        print "The device with an ip address of %r has been connected" % self.ipAdd
        output=self.connection.enable()
        print output

    def device_disconnect(self):#Disconnects the connection
        output=self.connection.disconnect()
        print "You have been disconnected"
        print output

    def __setNTPMaster__(self):
        connection = connectHandle
        print 'Enter your desired stratum-level'
        stratumLevel= str(raw_input())
        output = self.connection.send_config_set("ntp master "+ stratumLevel)
        print output

    def __setNTPServer__(self):
        connection = connectHandle
        print 'Enter the ip address of your NTP Master'
        ntpServer = str(raw_input())
        output = self.connection.send_config_set("ntp server "+ntpServer)
        print output

    def __showNTPStatus__(self):
        connection = connectHandle
        output= self.connection.send_command("Show ntp status")
        print output

    def __showNTPAssociations__(self):
        connection = connectHandle
        output = self.connection.send_command("Show ntp associations")
        print output

    def wait_minute(self):
        import time
        time.sleep(120)
