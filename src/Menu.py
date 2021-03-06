#-*- coding:utf8 -*-
import re as r
from tabulate import tabulate

class Menu:
    def __init__(self):
        pass
    
    def validateOption(self, opt):
        """ Validar opcion ingresada por el usuario con expresiones regulares """
        try:
            if r.match("^[0-9]*$", opt):
                if (int(opt) > 0 and int(opt) <= 2) or (int(opt) > 99 and int(opt) <= 102) or (int(opt) > 199 and int(opt) <= 201):
                    return opt
                else:
                    print("\n***** Invalid option: '%s' *****\n" % opt)
                    print("***** Select a valid option *****")
                    return True
            else:
                print("\n***** Invalid option: '%s' *****\n" % opt)
                print("***** Select a valid option *****")
                return True
        except:
            print("\n***** Error rise in option validation *****")
            return False
    
    def printIntro(self):
        """ Imprimir introduccion """
        intro = [
            ["Project 1 - Data Structures"],
            ["File manipulation"],
            ["Available lists"],
            ["Indices"],
            ]
        print(tabulate(intro, headers="firstrow", tablefmt='psql'))
        
    def printOpts(self):
        """ Imprimir opciones del usuario """
        print("\n")
        opts = [
            ["Index", "Option"],
            ["0", "Exit"],
            ["1", "Show all records"],
            ["2", "Show detail of a record"],
            ["100", "Add a record"],
            ["101", "Add a record in position"],
            ["102", "Delete a record"],            
            ["200", "Avaible list"],            
            ["201", "Index list"],            
        ]
        print(tabulate(opts, headers="firstrow", tablefmt='psql'))
        opt = input("\n***** Choose an option: *****\n")
        # Validar opcion es un numero con expresiones regulares
        validation = self.validateOption(opt)
        return validation
        
    