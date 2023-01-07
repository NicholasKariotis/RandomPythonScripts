#!/usr/bin/dev/
# Nicholas Kariotis
# September 9, 2022

import os
import subprocess
import time # All time.sleep()'s are too slow down the output for the user

def main():
    os.system('clear')
    date = os.system('date')
    print("\n--------PING TEST TROUBLESHOOTER--------")

    while(True): # Loop that continues until break in selection 0
        selection = prompt_user()
        while(selection > 4 or selection < 0): # Makes sure the number is a valid number
            print("Enter a valid input", end = ' ')
            time.sleep(2)
            selection = prompt_user()
        if(selection == 0):
            print("Goodbye")
            break;
            # Break exits infinite while loop
        elif(selection == 1): # Hard Coded default gateway of pfsense gateway.
            print("Beginning test for connectivity to your gateway...")
            response = subprocess.Popen(['ping', '192.168.1.254', '-c', '5', "-W", "4"])
            response.wait()
            if(response.poll() == 0):
                print("\nTest Successful! Notify your system admin of the test status.")
            else:
                print("\nTest was UNSUCCESSFUL, please notify your system admin.")
            time.sleep(2)
        elif(selection == 2): # Test remote with RIT DNS
            print("Beginning test for remote conenctivity...")
            time.sleep(2)
            response = os.system('ping 129.21.3.17 -c 3')
            if(response == 0):
                print("\nTest Successful! Notify your system admin of the test status.")
            else:
                print("\nTest was UNSUCCESSFUL, please notify your system admin.")
            time.sleep(2)
        elif(selection ==3): # Test DNS with google
            print("Resloving DNS: trying url www.google.com...")
            time.sleep(2)
            response = os.system('ping google.com -c 3')
            if(response == 0):
                print("\nTest Successful! Notify your system admin of the test status.")
            else:
                print("\nTest was UNSUCCESSFUL, please notify your system admin.")
            time.sleep(2)
        elif(selection ==4): # Hard Coded Default gateway
            print("\nYour default gateway IP address is: 192.168.1.254")
            time.sleep(2)



        
    
def prompt_user():
    # Function for user prompt
    print("\nEnter your selection: \n")
    print("\t1 - Test Connectivity To Gateway")
    print("\t2 - Test for Remote Connectivity")
    print("\t3 - Test for D!/usr/bin/dev/NS Resolution")
    print("\t4 - Display Gateway IP\n")
    try:
        selection = int(input("Enter a number (1-4 or 0 to exit): "))
    except: # Makes sure the user inputs a number
        print("You must input a number")
        selection = prompt_user() # Recursively continues to prompt the user until it is a number
    return selection


main()
