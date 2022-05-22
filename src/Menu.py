#-*- coding:utf8 -*-
import re as r
from tabulate import tabulate

class Menu:
    def __init__(self):
        pass

    def printIntro(self):
        """ Print Intro """
        intro = [
            ["Project 1 - Data Structures"],
            ["File manipulation"],
            ["Available lists"],
            ["Indices"],
            ]
        print(tabulate(intro, headers="firstrow", tablefmt='psql'))
        
    def printOpts(self):
        """ Print options to user """
        print("\n")
        opts = [
            ["Index", "Option"],
            ["0", "Exit"],
            ["1", "Show all records"],
            ["2", "Show detail of a record"],
            ["100", "Add a record"],
            ["101", "Delete a record"],
            ["102", "Modify a record"],
            
        ]
        print(tabulate(opts, headers="firstrow", tablefmt='psql'))
        opt = input("\n***** Choose an option: *****\n")
        # Validar opcion es un numero con expresiones regulares
        valopt = validateOption(opt)
        
    def validateOption(self, opt):
        """ Valdiate option inserted by user with regex """
        try:
            if r.match("^[0-9]*$", opt):
                if int(opt) > 0 and int(opt) <= 2:
                    return opt
                else:
                    return False
            else:
                print("\n***** Invalid option: '%s' *****\n" % opt)
                print("***** Select a valid option *****")
                return True
        except:
            
    