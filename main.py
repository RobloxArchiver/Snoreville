import pymem # This uses Pymem!!!

pm = pymem.Pymem("Windows10Universal.exe") # Roblox UWP???
modules = list(pm.list_modules())

for module in modules:
    print(module.name)
