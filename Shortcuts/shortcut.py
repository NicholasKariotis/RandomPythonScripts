#!/usr/bin/env python3
# Nicholas Kariotis
# Oct 20 2022

import os
import subprocess as sp
import time

def main():
    
    # Loop until user quits
    while(True):
        # Menu
        os.system("clear")
        print("\t*******************************")
        print("\t******* Shortcut Center *******")
        print("\t*******************************\n")

        print("Enter a Selection: \n")
        print("\t1 - Create a shortcut in your home directory.")
        print("\t2 - Remove a shortcut from your home directory.")
        print("\t3 - Run shortcut report.\n")
        selection  = input("Enter a number (1-3) or 'quit'/'Quit' to quit the program: ")

        if(selection == "quit" or selection == "Quit"):
            break
        elif(selection == "1"):
            create_shortcut()
        elif(selection == "2"):
            delete_shortcut()
        elif(selection == "3"):
            shortcut_report()
        else:
            print("Invalid selection!")

def shortcut_report():
    # Displays all of the shortcuts in the users home directoryeval echo
    os.system("clear")
    print("\t*******************************")
    print("\t******* Shortcut Report *******")
    print("\t*******************************\n")
    print("Your current directory is /home/"+os.getlogin())
    print("\nShortcut -> Path\n")
    os.system("ls -la /home/"+os.getlogin()+" | grep '\->' | awk '{print $9,$10, $11}'")
    input("\nPress enter to return to the menu ")

def delete_shortcut():
    os.system('clear')
    filename = input("Please enter a shortcut to delete:\t")
    try:
        print("Deleting Shortcut...")
        time.sleep(3)
        # Deletes the link if it exists
        os.unlink("/home/"+os.getlogin()+"/"+filename)
        print("Shortcut Deleted! Press enter to return to the menu ", end = "")
        input()
    except:
        # If the link does not exist, gives and error and goes back to the menu
        print("This file does not exist, press enter to return to the menu ", end = "")
        input()

def create_shortcut():
    os.system('clear')

    filename = input("Please enter a filename to create a shortcut:\t")
    print("\nFinding File...")
    time.sleep(1)
    foundfile = find(filename, "/home/")

    if(foundfile == None): 
        print("Could not find the file, press enter to continue", end = "")
        input()
    else:
        print("Found File: ", foundfile, end = "  ")
        option = input("Do you wont to create a shortcut? y/n: ")
        if(option == "y"):
            username = os.getlogin()
            print("Creating Shorcut...")
            time.sleep(3)
            try:
                os.symlink(foundfile, "/home/"+username+"/"+filename)
                print("Shorcut Created! Press enter to return to the menu", end = "")
                input()
            except:
                print("That shortcut already exists, press enter to return to the menu", end = "")
                input()
        

def find(name, path):
    # Searches for the file(name) in the path given and returns the whole file path
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
main()
