from pymem import Pymem, pattern, process

minecraft_process = Pymem("Minecraft.Windows.exe")
minecraft_module = process.module_from_name(minecraft_process.process_handle, "Minecraft.Windows.exe")

IsBanned = pattern.pattern_scan_module(minecraft_process.process_handle, minecraft_module, rb"\x48\x8D\x15....\x48\x8B\xCF\xE8....\x48\x8B\xC8\x48\x8D\x55\xB8\xE8....\x81\x65.....")

print(minecraft_process.read_string(minecraft_process.process_handle + IsBanned))