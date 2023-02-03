#-------------------------------------------------------------------------------
# Credits:
#
#     Snaacky @ GitHub (https://github.com/Snaacky) // Used a bit of code from mw2tweaks
#-------------------------------------------------------------------------------

import keyboard
from Utility.Signatures import *
from os import system
from pymem import exception, Pymem, pattern

try:
    minecraft_process = Pymem("Minecraft.Windows.exe")
except exception.ProcessNotFound:
    print("Please open Minecraft first")
    input("Press 'ENTER' to exit")
