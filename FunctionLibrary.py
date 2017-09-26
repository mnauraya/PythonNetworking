from sys import argv#Allows us to place outside arguments into the program
from netmiko import ConnectHandler#Imports the netmiko libraries
from clockSetup import ClockSetup #import the datetime module
from DeviceLibrary import DeviceLibrary
import netmiko

class FunctionLibrary(DeviceLibrary):

    def __init__(self, device):
        self.device = device

    def __getConfigInfo__(self):#Takes in the list file into the method
        self.hostname = self.device.router1.get('Hostname')
        self.ipAdd = self.device.router1.get('IP Address')
        self.os = self.device.router1.get('OS')
        self.usrName = self.device.router1.get('Username')
        self.ln_pass = self.device.router1.get('Ln_Pass')
        self.en_pass = self.device.router1.get('En_Pass')

    def __DeviceConnect__(self):#
        self.connection = netmiko.ConnectHandler(ip=self.ipAdd, device_type=self.os, username=self.usrName, password=ln_pass, secret=self.en_pass)
        print "The device with an ip address of %r has been connected" % self.ipAdd
        output=connection.enable()
        print output

    __Device
