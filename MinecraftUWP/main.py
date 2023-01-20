#-------------------------------------------------------------------------------
# Credits:
#
#     Snaacky @ GitHub (https://github.com/Snaacky) // Used a bit of code from mw2tweaks
#-------------------------------------------------------------------------------

from os import system
from pymem import exception, Pymem

system("title MCBE Module Dumper")

try:
    minecraft_process = Pymem("Minecraft.Windows.exe")
except exception.ProcessNotFound:
    print("Please open Minecraft first")
    input("Press 'ENTER' to exit!")

def main():
    print("Minecraft Process Grabbed...\nDumping...\n\n")

    modules = list(minecraft_process.list_modules())

    for module in modules:
        print(f"{module.name}: {module.filename}")

    input("\nDump Finished! Press 'ENTER' to exit!")

if __name__ == "__main__":
    main()