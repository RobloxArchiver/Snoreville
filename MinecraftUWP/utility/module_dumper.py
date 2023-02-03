#-------------------------------------------------------------------------------
# Credits:
#
#     Snaacky @ GitHub (https://github.com/Snaacky) // Used a bit of code from mw2tweaks
#-------------------------------------------------------------------------------

from os import system
from pymem import exception, Pymem

def __init__():
    system("cls") # Clear console
    system("title Dumping Modules...")
    minecraft_process = Pymem("Minecraft.Windows.exe")

    modules = list(minecraft_process.list_modules())

    for module in modules:
        print(f"{module.name}: {module.filename}")
        
    system("title Dump Finished")
    input("Press 'ENTER' to exit!")
