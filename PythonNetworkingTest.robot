*** Settings ***
Library           FunctionLibrary.py

*** Test Cases ***
Establish Device Connection
    Get Config Info
    Device Connect
    Device Disconnect
