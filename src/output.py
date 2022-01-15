# Author        : Tyler Johnson
# Date          : 2022/01/14
# Description   : Helps with colored output

import colorama

class Output:

    # Start colorama
    def __init__(self):
        colorama.init()

    def __reset(self) -> None:
        
        print(colorama.Fore.WHITE + colorama.Back.BLACK, end='')
        return

    def warning(self, string: str, endline='\n') -> None:

        print(colorama.Fore.YELLOW + string, end=endline)
        self.__reset()
        return
    
    def input(self, request: str) -> str:

        print(colorama.Fore.GREEN + request, end='')
        result = input()
        self.__reset()
        print()
        return result
    
    def fatal(self, string: str, endline='\n') -> None:

        print(colorama.Fore.BLACK + colorama.Back.RED + "ERROR:" + colorama.Fore.RED + colorama.Back.BLACK + ' ' + string, end=endline)
        self.__reset()
        return