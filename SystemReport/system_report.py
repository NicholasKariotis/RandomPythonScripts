#!/usr/bin/env python3
# Nicholas Kariotis
# Sept 26 2022

import os
import subprocess as sp
import datetime

def main():
    # Clear Terminal
    os.system('clear')
    
    # Display title and date
    date = datetime.datetime.now();
    print("\tSystem Report - ", date.day, "-", date.month, "-", date.year, sep="");
    
    # Display hostname and domain
    print("\nDevice Information\nHostname:\t        ", end="")
    os.system('hostname -s')

    print("Domain:                ", sp.getoutput('hostname -y'))
    
    # Display Network Information
    print("\nNetwork Information")
    ip = (sp.getoutput("ip a | grep inet | awk 'FNR == 3 {print $2}'"))
    print("IP Address:            ", ip[0:(len(ip)-3)])
    print("Gateway Address:       ", sp.getoutput("ip route | grep default | awk '{print $3}'"))
    print("Network Mask:          ", sp.getoutput("netstat -nr | grep 255 | awk '{print $3}'"))
    print("DNS1:                  ", sp.getoutput("cat /etc/resolv.conf | grep nameserver | awk 'FNR == 1{print $2}'"))
    print("DNS2:                  ", sp.getoutput("cat /etc/resolv.conf | grep nameserver | awk 'FNR == 2{print $2}'"))

    # Display Operating System Info
    print("\nOS Information")
    OS = sp.getoutput("cat /etc/os-release | grep NAME= | awk 'FNR == 2{print $1}'")
    print("Operating System:      ", OS[6::])
    version = sp.getoutput("cat /etc/os-release | grep VERSION | awk 'FNR ==1{print$1}'")
    print("Operating Version:     ", version[9:len(version)-1])
    print("Kernel Version:        ", sp.getoutput('uname -r'))

    # Display Storage Information
    print("\nStorage Information")
    hdsize = int(sp.getoutput("lsblk | awk 'FNR == 2{print $4}'")[0:-1])
    print("Hard Drive Capacity:    ", hdsize, "G", sep = "")
    hdavail = int(sp.getoutput("df | grep /dev/ | awk 'FNR == 1{print $4}'")[0:-1])//100000
    print("Available Space:        ", hdavail, "G", sep="")

    # Display Processor Information
    print("\nProcessor Information")
    print("CPU Model:             ", sp.getoutput("cat /proc/cpuinfo | grep 'model name' | awk 'FNR == 1'")[13::])



    
    
main()
