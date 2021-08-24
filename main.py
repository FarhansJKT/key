import time
import os

nu = input("SHORTCUT TERMUX - ENTER -")
key = ["CTRL","ALT","FN","SPACE","ESC","TAB","HOME","END","PGUP","PGDN","INS","DEL","BKSP","UP","LEFT","RIGHT","DOWN","ENTER","BACKSLASH","QUOTE","APOSTROPHE","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","KEYBOARD","DRAWER"]
keys = f"extra-keys = {key}"
open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
os.system('termux-reload-settings')
print("sukses menambahkan shortcut")
os.system('cd')
os.system('login')
