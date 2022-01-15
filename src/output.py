# Author        : Tyler Johnson
# Date          : 2022/01/14
# Description   : Helps with colored output

import colorama

class Output:

    # Start colorama
    def __init__(self):
        colorama.init()

    def reset(self) -> None:
        
        print(colorama.Fore.WHITE + colorama.Back.BLACK)
        return

    def warning(self, string: str) -> None:

        print(colorama.Fore.LIGHTYELLOW_EX + string)
        self.reset()
        return
    
    def input(self, request: str) -> str:

        result = input(colorama.Fore.GREEN + request, end='')
        self.reset()
        return result
    
    def fatal(self, string: str) -> None:

        print(colorama.Fore.BLACK + colorama.Back.RED + "ERROR: " + colorama.Fore.RED + colorama.Back.BLACK + string)
        self.reset()
        return