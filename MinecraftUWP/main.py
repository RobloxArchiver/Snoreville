#-------------------------------------------------------------------------------
# Credits:
#
#     Snaacky @ GitHub (https://github.com/Snaacky) // Used a bit of code from mw2tweaks
#-------------------------------------------------------------------------------

import keyboard
from os import system
from pymem import exception, Pymem

system("title MCBE Module Dumper")

try:
    minecraft_process = Pymem("Minecraft.Windows.exe")
except exception.ProcessNotFound:
    print("Please open Minecraft first")
    input("Press 'ENTER' to exit!")

def main():
    pass

if __name__ == "__main__":
    main()
