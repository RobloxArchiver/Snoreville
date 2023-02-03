import pymem

minecraft_process = pymem.Pymem("Minecraft.Windows.exe")

## Basic format of how it works
# OFFSET_FROM_SIG = pymem.pattern.pattern_scan_all(rb"\xB0\xB5....\xC5\xB8\xB4\xB2.\F4....")
## In theory via running
# print("Offset: {}".format(hex(OFFSET_FROM_SIG)))
## It will give us an offset!
## This is the way the sys backend will work for now

minecraft_process.close_process()
