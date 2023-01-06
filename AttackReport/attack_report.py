#!/usr/bin/python3
# Nicholas Kariotis
# November 2 2022
#

import datetime
import os
import re
import requests

def main():
    os.system('clear')
    
    # Print Title
    date = datetime.datetime.now()
    print("Attack Report - ", date.strftime("%B"), " ", date.day, " ", date.year, "\n", sep = "")
    # strftime method used to format the string, the %B specifies month in words

    # Identify attacks
    #   Dictionary -> {IP:attack count}
    PATH = "./syslog.log"
    # Hard coded path to log file
    attacks = getAttacks(PATH)
    
    # Sort attacks in ascending order
    # Found at https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/#:~:text=To%20correctly%20sort%20a%20dictionary,with%20the%20item()%20method
    # Created a sorted list of tuples (ip,count) sorted by count
    sortedAttacks = sorted(attacks.items(), key=lambda x:x[1])
    
    # Remove IPs with attack count < 10
    notAttacks = []
    for attack in sortedAttacks:
        if attack[1] < 10:
            notAttacks.append(attack)
    for notAttack in notAttacks:
        sortedAttacks.remove(notAttack)

    # Output attack info
    print("COUNT     IP ADDRESS       COUNTRY")
    for attack in sortedAttacks:
        print(attack[1], end = "")
        for i in range(0, 10-len(str(attack[1]))):
            print(" ", end = "")
        print(attack[0], end = "")
        for i in range(0, 17-len(attack[0])):
            print(" ", end = "")

        URL = "https://geolocation-db.com/json/"+attack[0]+"&position=true"
        response = requests.get(URL).json()
        print(response['country_code'])
        # I could not get geolite2 to work so I used a method found here:
        #   - https://stackoverflow.com/questions/24678308/how-to-find-location-with-ip-address-in-python
        

    

    

def getAttacks(path):
    """
    This function parses a log file identifying attacks as failed password attempts
    as well as authentication failures and returns a dictionary mapping
    the ip to the attack count.

    'Failed passwword', 'authentication failure;', and 'x more authentication failures'
    will all cause an increase in the attack count.
        - 'x more authentication failures' will add x to the count for the associated ip
    """
    attacks = {}
    with open(path, 'r') as logfile:
        for line in logfile:
            # Find 'Failed password' and add 1 to attack count for that IP
            if line.find("Failed password") != -1:
                # Regular expression for identifying an IP address found at:
                # https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html
                ip = re.search("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", line)[0]
                if ip in attacks.keys():
                    attacks[ip] = attacks[ip] + 1
                else:
                    attacks[ip] = 1

            # Find 'authentication failure;' and add 1 to attack count for that IP
            elif line.find("authentication failure;") != -1:
                ip = re.search("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", line)[0]
                if ip in attacks.keys():
                    attacks[ip] = attacks[ip] + 1
                else:
                    attacks[ip] = 1

            # Find 'more authentication failures' and add the amount of failures specified to the attack count
            elif line.find("more authentication failures") != -1:
                splitLine = line.split(" ")
                failuresIndex = splitLine.index("PAM") + 1
                failures = splitLine[failuresIndex]

                ip = re.search("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", line)[0]
                if ip in attacks.keys():
                    attacks[ip] = attacks[ip] + int(failures)
                else:
                    attacks[ip] = int(failures)


    return attacks

main()